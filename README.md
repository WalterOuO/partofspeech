# Part of Speech
This project is a system to analysize traditional Chinese Part of Speech (POS) based on [CKIP Transformers](https://github.com/ckiplab/ckip-transformers) released by [CKIP Lab](https://github.com/ckiplab).  
The 62 kinds of part of speech tag listed by CKIP Lab is condensed to 5 kinds to focus on the five most common parts of speech.  
The remaining 5 pos is Noun, Pronoun, Verb, Adjective, Adverb.  
這是一個基於CKIP Lab推出之CKIP Transformers所建立的繁體中文詞性分析系統，我們將CKIP Lab列出的詞性種類從62種整併至5種以聚焦在五種最常見的詞性，分別是名詞、代名詞、動詞、形容詞、副詞。

### Demo video
https://github.com/user-attachments/assets/dccf8657-a266-43e9-a3b8-34ae24a316f6

### Input and Output
#### Input
Input should be a excel file recording every sentence spoken by the person. Each sentence includes three columns: Start time, End time and Content. The transcripts are manually made by Praat.
![Input 示範檔](https://github.com/user-attachments/assets/b9c9df26-d3c0-47a6-bb54-7948fe42b6ea)


#### Output
In Mode 1, system will make a excel file to record every count and proportion of each part of speech.  
![Output mode1示範檔](https://github.com/user-attachments/assets/e454f1b1-6a28-405b-8253-e9947e58f630)

In Mode 2, system will directly show the part of speech result for every sentence.  
In the end, system will analyze total count and total proportion of each part of speech for this person.
![Output mode2-1示範圖](https://github.com/user-attachments/assets/f3bc133a-4d2b-4499-8fd6-046a2881d03a)
![Output mode2-2示範圖](https://github.com/user-attachments/assets/c22e4fab-0ba5-4c51-8dad-e530230ff1f5)

### Part of Speech tag Conversion
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
</table>


