# Part of Speech
This project is a system to analysize traditional Chinese Part of Speech (POS) based on [CKIP Transformers](https://github.com/ckiplab/ckip-transformers) released by [CKIP Lab](https://github.com/ckiplab).  
The 62 kinds of part of speech tag listed by CKIP Lab is condensed to 5 kinds to focus on the five most common parts of speech.  
The remaining 5 pos is Noun, Pronoun, Verb, Adjective, Adverb.  
這是一個基於CKIP Lab推出之CKIP Transformers所建立的繁體中文詞性分析系統，我們將CKIP Lab列出的詞性種類從62種整併至5種以聚焦在五種最常見的詞性，分別是名詞、代名詞、動詞、形容詞、副詞。

## Demo video
https://github.com/user-attachments/assets/dccf8657-a266-43e9-a3b8-34ae24a316f6

## Input and Output
### Input
Input should be a excel file recording every sentence spoken by the person. Each sentence includes three columns: Start time, End time and Content. The transcripts are manually made by Praat.
![Input 示範檔](https://github.com/user-attachments/assets/b9c9df26-d3c0-47a6-bb54-7948fe42b6ea)


### Output
In Mode 1, system will make a excel file to record every count and proportion of each part of speech.  
![Output mode1示範檔](https://github.com/user-attachments/assets/e454f1b1-6a28-405b-8253-e9947e58f630)

In Mode 2, system will directly show the part of speech result for every sentence.  
In the end, system will analyze total count and total proportion of each part of speech for this person.
![Output mode2-1示範圖](https://github.com/user-attachments/assets/f3bc133a-4d2b-4499-8fd6-046a2881d03a)
![Output mode2-2示範圖](https://github.com/user-attachments/assets/c22e4fab-0ba5-4c51-8dad-e530230ff1f5)

## Part of Speech Tag Conversion
Adjust from: https://ckip-transformers.readthedocs.io/en/stable/main/tag.html  
This is a table to map 62 kinds of pos to 5 kinds of pos, which can be tunned by personal used.  
<table>
  <tr>
    <td>Tag</td>
    <td>Description</td>
    <td>New Tag</td>
  </tr>
  <tr>
    <td>A</td>
    <td>形容詞</td>
    <td>形容詞</td>
  </tr>
  <tr>
    <td>Caa</td>
    <td>對等連接詞</td>
    <td></td>
  </tr>
  <tr>
    <td>Cad</td>
    <td>連接詞，如:等等</td>
    <td></td>
  </tr>
  <tr>
    <td>Cba</td>
    <td>連接詞，如：的話</td>
    <td></td>
  </tr> 
  <tr>
    <td>Cbb</td>
    <td>關聯連接詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>D</td>
    <td>副詞</td>
    <td>副詞</td>
  </tr> 
  <tr>
    <td>Da</td>
    <td>數量副詞</td>
    <td></td>
  </tr>
  <tr>
    <td>Dfa</td>
    <td>動詞前程度副詞</td>
    <td>副詞</td>
  </tr>
  <tr>
    <td>Dfb</td>
    <td>動詞後程度副詞</td>
    <td>副詞</td>
  </tr>
  <tr>
    <td>Di</td>
    <td>時態標記</td>
    <td></td>
  </tr>
  <tr>
    <td>Dk</td>
    <td>句副詞</td>
    <td></td>
  </tr>
  <tr>
    <td>DM</td>
    <td>定量式</td>
    <td></td>
  </tr>
  <tr>
    <td>I</td>
    <td>感嘆詞</td>
    <td></td>
  </tr>  
  <tr>
    <td>Na</td>
    <td>普通名詞</td>
    <td>名詞</td>
  </tr> 
  <tr>
    <td>Nb</td>
    <td>專有名詞</td>
    <td>名詞</td>
  </tr> 
  <tr>
    <td>Nc</td>
    <td>地方詞</td>
    <td>名詞</td>
  </tr> 
  <tr>
    <td>Ncd</td>
    <td>位置詞</td>
    <td>名詞</td>
  </tr> 
  <tr>
    <td>Nd</td>
    <td>時間詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>Nep</td>
    <td>指代定詞</td>
    <td>代名詞</td>
  </tr> 
  <tr>
    <td>Neqa</td>
    <td>數量定詞</td>
    <td>形容詞</td>
  </tr> 
  <tr>
    <td>Neqb</td>
    <td>後置數量定詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>Nes</td>
    <td>特指定詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>Neu</td>
    <td>數詞定詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>Nf</td>
    <td>量詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>Ng</td>
    <td>後置詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>Nh</td>
    <td>代名詞</td>
    <td>代名詞</td>
  </tr> 
  <tr>
    <td>Nv</td>
    <td>名物化動詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>P</td>
    <td>介詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>T</td>
    <td>語助詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>VA</td>
    <td>動作不及物動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VAC</td>
    <td>動作使動動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VB</td>
    <td>動作類及物動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VC</td>
    <td>動作及物動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VCL</td>
    <td>動作接地方賓語動詞</td>
    <td></td>
  </tr> 
  <tr>
    <td>VD</td>
    <td>雙賓動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VF</td>
    <td>動作謂賓動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VE</td>
    <td>動作句賓動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VG</td>
    <td>分類動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VH</td>
    <td>狀態不及物動詞</td>
    <td>形容詞</td>
  </tr> 
  <tr>
    <td>VHC</td>
    <td>狀態使動動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VI</td>
    <td>狀態類及物動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VJ</td>
    <td>狀態及物動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VK</td>
    <td>狀態句賓動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>VL</td>
    <td>狀態謂賓動詞</td>
    <td>動詞</td>
  </tr> 
  <tr>
    <td>V_2</td>
    <td>有</td>
    <td>有</td>
  </tr> 
  <tr>
    <td>DE</td>
    <td>的之得地</td>
    <td>的之得地</td>
  </tr> 
  <tr>
    <td>SHI</td>
    <td>是</td>
    <td>是</td>
  </tr> 
  <tr>
    <td>FW</td>
    <td>外文</td>
    <td></td>
  </tr> 
  <tr>
    <td>COLONCATEGORY</td>
    <td>冒號</td>
    <td></td>
  </tr> 
  <tr>
    <td>COMMACATEGORY</td>
    <td>逗號</td>
    <td></td>
  </tr> 
  <tr>
    <td>DASHCATEGORY</td>
    <td>破折號</td>
    <td></td>
  </tr> 
  <tr>
    <td>DOTCATEGORY</td>
    <td>點號</td>
    <td></td>
  </tr> 
  <tr>
    <td>ETCCATEGORY</td>
    <td>刪節號</td>
    <td></td>
  </tr> 
  <tr>
    <td>EXCLAMATIONCATEGORY</td>
    <td>驚嘆號</td>
    <td></td>
  </tr> 
  <tr>
    <td>PARENTHESISCATEGORY</td>
    <td>括號</td>
    <td></td>
  </tr> 
  <tr>
    <td>PAUSECATEGORY</td>
    <td>頓號</td>
    <td></td>
  </tr> 
  <tr>
    <td>PERIODCATEGORY</td>
    <td>句號</td>
    <td></td>
  </tr> 
  <tr>
    <td>QUESTIONCATEGORY</td>
    <td>問號</td>
    <td></td>
  </tr> 
  <tr>
    <td>SEMICOLONCATEGORY</td>
    <td>分號</td>
    <td></td>
  </tr> 
  <tr>
    <td>SPCHANGECATEGORY</td>
    <td>雙直線</td>
    <td></td>
  </tr> 
  <tr>
    <td>WHITESPACE</td>
    <td>空白</td>
    <td></td>
  </tr> 
</table>

### Merge Rule
有、的之得地、是 這三種詞性可與其他詞組合成不同的動詞  
#### 有
1. 「還有」：視為一個連接詞，不計入五種詞性
2. 「他有看到」：「有」後方出現動詞時，不計入五種詞性
3. 將其餘「有」皆視為動詞，例如「我有一把傘」

#### 的之得地
「漂亮的」：CKIP的詞典會分為「漂亮 (形容詞)」與「的 (的之得地)」，應該合併為一個形容詞。因此「的」前方遇到形容詞時，皆結合成為形容詞。

#### 是
1. 「像是」：應合併一起使用
2. 「我是認為是這樣子的」：這邊的「是」不計入五種詞性。

## How to use the code 
Main code: [zh_TW_pos.ipynb](https://github.com/WalterOuO/partofspeech/blob/main/zh_TW_pos.ipynb)  
Package for Mode 1: [tool.py](https://github.com/walterouo/partofspeech/tool.py)

Switch the Input path and Output path in Main code and package for your use. 
