#encoding=utf-8
import ngram
index = ngram.NGram(N=3)
terms = list(index.ngrams(index.pad(u"網路世代來臨，民意代表也無法只侷限在以往實體選民服務的方式，紛紛上網設立網站、部落格，向選民報告近況。近來台北市議員最流行的就是噗浪，不少議員幾乎天天發噗，其中又以綠營議員最為積極。由於噗浪以「時間軸線」方式呈現噗友留言，互動性高且即時，更容易拉近與噗友的距離，同時噗浪留言簡潔有力，讓人能很快一目了然，不少政治人物、民代甚至把噗浪當成新聞發布平台。民進黨市議員莊瑞雄就是噗浪愛好者，幾乎每天早晚都噗，甚至用手機拍照「現場噗」，讓噗友有「身歷其境」的感覺。他說，噗浪上有來自四面八方的噗友，針對不同議題，想法獨特，還有很多令人噴飯的回應，讓他有很多靈感。噗友的加油、打氣，也是他揭弊的動力。莊瑞雄說，玩噗浪會上癮，會希望把卡馬值 (Karma)升到100，等掉下來後再繼續噗。包括劉耀仁、黃向羣、吳思瑤、顏聖冠、李慶鋒等綠營議員都有噗浪，也經常在上面發表言論及心得。其中又以莊瑞雄卡馬值最高，已達95.85。相較下，藍營市議員有玩噗浪的是少之又少，只有國民黨李彥秀及新黨王鴻薇。李彥秀助理謝心瑜說，噗浪只需一小段話，不像部落格文章又長又多，更容易貼近民眾。她說，議員把她抱著女兒侯貽寶的照片當封面，馬上就有噗友發噗回應直說「好可愛」、「母女都漂亮」。至於王鴻薇因太久沒發噗，卡馬值已經掉到0。市議員陳玉梅助理表示，議員太忙了，實在沒時間發噗，所以用部落格方式與選民互動，況且如果是假手他人代噗，被發現也不好。有議員認為，噗浪已淪為形式，政治人物噗女兒怎樣、幾點幾分吃了什麼、早安、晚安、下雨了等，根本沒有意義，這些關民眾什麼事，所以堅持不玩噗浪。")))
print terms