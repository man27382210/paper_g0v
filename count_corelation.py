#encoding=utf-8
from __future__ import division
import re
import os
import sys
import jieba
import jieba.posseg as pseg
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection = db['news_url_list_save']
collection_cr_plat = db['cr_platform']
collection_plat_news = db['plat_news_cor_new']

def marge(plat):
    result_arr = []
    result_arr.extend(plat["platforms_nonu"])
    result_arr.extend(plat["platforms_verb"])
    return result_arr


if __name__ == "__main__":
    news_list = collection.find({"cr":u"吳碧珠"})
    news_list = list(news_list)
    plat_list = collection_cr_plat.find({"cr_name":u"吳碧珠"})
    plat_list = list(plat_list)
    for plat in plat_list:
        save_dict ={}
        plat_terms = marge(plat)
        plat_news_cor = 0
        save_dict["plat"]=plat
        news_arr =[]
        for news in news_list:
            news_dict = {}
            news_dict["news"] = news
            interArr = list(set(news["story_term"]).intersection(set(plat_terms)))
            news_dict["match_term"] = interArr
            print interArr
            cor_value = 0
            if(len(interArr)!=0):
                print plat_terms
                print len(plat_terms)
                print interArr
                print len(interArr)
                cor_value = len(interArr)/len(plat_terms)
            news_dict["cor_value"] = cor_value
            print cor_value
            print ""
            news_arr.append(news_dict)
            plat_news_cor = plat_news_cor+cor_value
        ac = plat_news_cor/len(news_list)
        save_dict["news_list"] = news_arr
        save_dict["ac"] = ac
        collection_plat_news.save(save_dict)
    exit(0)