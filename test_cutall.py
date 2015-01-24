#encoding=utf-8
import sys
sys.path.append("../")
import jieba

def cuttest(test_sent):
    result = jieba.cut(test_sent,cut_all=True)
    for word in result:
        print word.encode('utf-8'), "/", 
    print ""


if __name__ == "__main__":
    cuttest("干脆就把那部蒙人的闲法给废了拉倒！RT @laoshipukong : 27日，全国人大常委会第三次审议侵权责任法草案，删除了有关医疗损害责任“举证倒置”的规定。在医患纠纷中本已处于弱势地位的消费者由此将陷入万劫不复的境地。 ")