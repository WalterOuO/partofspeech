import os
import glob
import numpy as np
import pandas as pd
from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker

def pos(filename):
    file_path = os.path.join('/content/drive/MyDrive/逐字稿/所有逐字稿excel', filename)

    pos_EtoC = { "A":"形容詞" ,"Caa":"X", "Cab":"X", "Cba":"X", "Cbb":"X", "D":"副詞", "Da":"X", "Dfa":"副詞", "Dfb":"副詞",
            "Di":"X", "Dk":"X", "DM":"X", "I":"X", "Na":"名詞", "Nb":"名詞", "Nc":"名詞", "Ncd":"名詞", "Nd":"X", # "Nd":"時間詞",
            "Nep":"代名詞", "Neqa":"形容詞", "Neqb":"X", "Nes":"X", "Neu":"X", # "Neu":"數詞定詞",
            "Nf":"X", "Ng":"X", "Nh":"代名詞", "Nv":"X", "P":"X", # "P":"介詞",
            "T":"X", # "T":"語助詞",
            "VA":"動詞", "VAC":"動詞", "VB":"動詞", "VC":"動詞", "VCL":"X", "VD":"動詞", "VF":"動詞", "VE":"動詞", "VG":"動詞", "VH":"形容詞", "VHC":"動詞", "VI":"動詞",
            "VJ":"動詞", "VK":"動詞", "VL":"動詞", "V_2":"有", "DE":"的之得地", "SHI":"是","FW":"X",
            "COLONCATEGORY":"X", "COMMACATEGORY":"X", "DASHCATEGORY":"X", "DOTCATEGORY":"X", "ETCCATEGORY":"X", "EXCLAMATIONCATEGORY":"X", "PARENTHESISCATEGORY":"X",
            "PAUSECATEGORY":"X", "PERIODCATEGORY":"X", "QUESTIONCATEGORY":"X", "SEMICOLONCATEGORY":"X", "SPCHANGECATEGORY":"X", "WHITESPACE":"X", "X":"X"}

    # Initialize drivers
    ws_driver  = CkipWordSegmenter(model="bert-base")
    pos_driver = CkipPosTagger(model="bert-base")
    ner_driver = CkipNerChunker(model="bert-base")

    template_df = pd.DataFrame().assign(
        字數=0,
        詞彙數=0,
        名詞=0,
        代名詞=0,
        動詞=0,
        形容詞=0,
        副詞=0,
        名詞比例=0.0,
        代名詞比例=0.0,
        動詞比例=0.0,
        形容詞比例=0.0,
        副詞比例=0.0
    )

    # for file_path in file_paths:
    data = pd.read_excel(file_path) #pd.read_excel(file_path, usecols=["Content"])
    df = pd.DataFrame(data)
    df = df.reindex(columns=df.columns.tolist() + template_df.columns.tolist(), fill_value=0)

    # Save transcripts to list
    text = []
    for i in range(len(data)):
        text.append(df["Content"].iloc[i])

    # Enable sentence segmentation
    ws  = ws_driver(text, use_delim=True)
    ner = ner_driver(text, use_delim=True)
    pos = pos_driver(ws, delim_set='\n\t')

    # Show results
    exclude = ["(", ")", "（", "台", "）", "，", "。", "...", "..", ".", " ", "?", "？", "!", "、"]
    kuo_exclude = ["經", "通", "穿", "走"]
    total_counts = [0]*8

    for index, (sentence_ws, sentence_pos) in enumerate(zip(ws, pos)): #會迭代每句的分詞、詞性(英文)
        sen_counts = [0]*7
        pos_ch = []
        for i in range(len(sentence_pos)):
            if sentence_ws[i]=="有":
                if sentence_ws[i-1] == "還":
                    sentence_pos[i] = "X"
                elif pos_EtoC[sentence_pos[i+1]] == "動詞":
                    sentence_pos[i] = "X"
                else:
                    sentence_pos[i] = "VA"
            if sentence_ws[i] == "台":
                sentence_pos[i] = "X"
            if sentence_ws[i] == "過":
                if sentence_ws[i-1] not in kuo_exclude:
                    sentence_pos[i] = "VA"
            pos_ch.append(pos_EtoC[sentence_pos[i]])
        
        new_sentence_ws = []                  # 新的分詞和詞性列表
        new_sentence_pos = []
        i = 0
        while i < len(sentence_ws):              # 遍歷詞和詞性，進行合併操作
            if pos_ch[i] == '形容詞' and i + 1 < len(sentence_ws) and pos_ch[i + 1] == '的之得地':
                new_sentence_ws.append(sentence_ws[i] + sentence_ws[i + 1])   # 合併形容詞和的之得地
                new_sentence_pos.append('形容詞')
                i += 2  # 跳過下一個詞
            if sentence_ws[i]=="就" and i + 1 < len(sentence_ws) and sentence_ws[i+1]=="是":
                new_sentence_ws.append(sentence_ws[i] + sentence_ws[i + 1])   # 合併就是
                new_sentence_pos.append('副詞')
                i += 2  # 跳過下一個詞
            if sentence_ws[i] in kuo_exclude and i + 1 < len(sentence_ws) and sentence_ws[i+1]=="過":
                new_sentence_ws.append(sentence_ws[i] + sentence_ws[i + 1])
                new_sentence_pos.append('動詞')
                i += 2    
            else:
                new_sentence_ws.append(sentence_ws[i])  # 否則正常添加
                new_sentence_pos.append(pos_ch[i])
                i += 1

        for i in range(len(new_sentence_pos)):
            if new_sentence_ws[i] not in exclude:      #不計算台語標註的(台)為字數統計量
                sen_counts[0] += len(new_sentence_ws[i])
                sen_counts[1] += 1
            if new_sentence_pos[i] == "名詞":
                sen_counts[2] += 1
            elif new_sentence_pos[i] == "代名詞":
                sen_counts[3] += 1
            elif new_sentence_pos[i] == "動詞":
                sen_counts[4] += 1
            elif new_sentence_pos[i] == "形容詞":
                sen_counts[5] += 1
            elif new_sentence_pos[i] == "副詞":
                sen_counts[6] += 1
            else:
                continue

        df.at[index, '字數'] = sen_counts[0]
        df.at[index, '詞彙數'] = sen_counts[1]
        df.at[index, '名詞'] = sen_counts[2]
        df.at[index, '代名詞'] = sen_counts[3]
        df.at[index, '動詞'] = sen_counts[4]
        df.at[index, '形容詞'] = sen_counts[5]
        df.at[index, '副詞'] = sen_counts[6]
        if sen_counts[1] > 0:
            df.at[index, '名詞比例'] = round(sen_counts[2] / sen_counts[1], 4)*100
            df.at[index, '代名詞比例'] = round(sen_counts[3] / sen_counts[1], 4)*100
            df.at[index, '動詞比例'] = round(sen_counts[4] / sen_counts[1], 4)*100
            df.at[index, '形容詞比例'] = round(sen_counts[5] / sen_counts[1], 4)*100
            df.at[index, '副詞比例'] = round(sen_counts[6] / sen_counts[1], 4)*100
        
        for i in range(len(sen_counts)):
            total_counts[i] += sen_counts[i]
        total_counts[7] += 1

    total_row = {
        'Start': '',
        'End': '',
        'Content': '',
        '字數': total_counts[0],
        '詞彙數': total_counts[1],
        '名詞': total_counts[2],
        '代名詞': total_counts[3],
        '動詞': total_counts[4],
        '形容詞': total_counts[5],
        '副詞': total_counts[6],
        '名詞比例': round(total_counts[2] / total_counts[1] if total_counts[1] > 0 else 0 ,4)*100,
        '代名詞比例': round(total_counts[3] / total_counts[1] if total_counts[1] > 0 else 0 ,4)*100,
        '動詞比例': round(total_counts[4] / total_counts[1] if total_counts[1] > 0 else 0 ,4)*100,
        '形容詞比例': round(total_counts[5] / total_counts[1] if total_counts[1] > 0 else 0 ,4)*100,
        '副詞比例': round(total_counts[6] / total_counts[1] if total_counts[1] > 0 else 0 ,4)*100,
        '總句數': total_counts[7]
    }

    total_row_df = pd.DataFrame([total_row])
    df = pd.concat([df, total_row_df], ignore_index=True)
    # print(df)

    output_folder = '/content/drive/MyDrive/詞性分析逐字稿'
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, filename)

    # 保存 DataFrame 到 Excel 文件
    columns_of_text = ['Content']
    columns_of_partio = ['名詞比例', '代名詞比例', '動詞比例', '形容詞比例', '副詞比例']
    with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        worksheet = writer.sheets['Sheet1']
        for col in columns_of_text:
            max_len = df[col].astype(str).map(len).max()
            col_index = df.columns.get_loc(col)
            worksheet.set_column(col_index, col_index, max_len + 2)
        for col in columns_of_partio:
            max_len = df[col].astype(str).map(len).max()
            col_index = df.columns.get_loc(col)
            worksheet.set_column(col_index, col_index, max_len)

    return "Your file has been saved to " + output_file_path
