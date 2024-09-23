# Part of Speech
This project is a system to analysize traditional Chinese Part of Speech (POS) based on [CKIP Transformers](https://github.com/ckiplab/ckip-transformers) released by [CKIP Lab](https://github.com/ckiplab).  
The 62 kinds of part of speech tag listed by CKIP Lab is condensed to 5 kinds to focus on the five most common parts of speech.  
The remaining 5 pos is Noun, Pronoun, Verb, Adjective, Adverb.  
這是一個基於CKIP Lab推出之CKIP Transformers所建立的繁體中文詞性分析系統，我們將CKIP Lab列出的詞性種類從62種整併至5種以聚焦在五種最常見的詞性，分別是名詞、代名詞、動詞、形容詞、副詞。

### Demo video
<video src='https://youtu.be/bEShvcKCTjo'></video>

### Part of Speech tag Conversion
Adjust from: https://ckip-transformers.readthedocs.io/en/stable/main/tag.html  
This is a table to map 62 kinds of pos to 5 kinds of pos, which can be tunned by personal used.  
[Conversion Table](url)
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

### Model Fine-tuning


