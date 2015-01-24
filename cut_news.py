#encoding=utf-8
import re
import os
import sys
import jieba
import jieba.posseg as pseg
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection = db['news_url_list']
collection_save = db['news_url_list_save']
def cuttest(test_sent):
    result_arr = []
    noun_terms_arr = []
    verb_terms_arr = []
    words_use = pseg.cut(test_sent)
    for word_use in words_use:
        if re.match("n", word_use.flag) != None:
            noun_terms_arr.append(word_use.word)
        if re.match("v", word_use.flag) != None:
            verb_terms_arr.append(word_use.word)
    # for word in noun_terms_arr:
    #     print word.encode('utf-8')
    # for word in verb_terms_arr:
    #     print word.encode('utf-8')
    result_arr.extend(noun_terms_arr)
    result_arr.extend(verb_terms_arr)
    print "done"
    return result_arr


if __name__ == "__main__":
    news_list = collection.find({"cr":u"吳碧珠"})
    news_list = list(news_list)
    for news in news_list:
        news["story_term"] = cuttest(news["story"])
        collection_save.save(news)
    exit(0)