#encoding=utf-8
from __future__ import division
import re
import os
import sys
import jieba
import jieba.posseg as pseg
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from pprint import pprint


client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
# collection = db['news_url_list_save']
collection = db['news_url_list_ckip']
collection_cr_plat = db['cr_platform_ckip']
collection_plat_news = db['plat_news_cor_ckip']

def marge(plat):
    result_arr = []
    result_arr.extend(plat["platforms_nonu"])
    result_arr.extend(plat["platforms_verb"])
    return result_arr
def parseJson():
    json_data=open('stopword.json')
    data = json.load(json_data)
    pprint(data)
    json_data.close()
    return data
def removeOneTerm(array):
    array_return = []
    for term in array:
        if len(term) > 1:
            array_return.append(term)
    return array_return

if __name__ == "__main__":
    stopword = parseJson()
    news_list = collection.find({"cr":u"吳碧珠"})
    news_list = list(news_list)
    plat_list = collection_cr_plat.find({"cr_name":u"吳碧珠"})
    plat_list = list(plat_list)
    for plat in plat_list:
        save_dict ={}
        # plat_terms = marge(plat)
        plat_terms = plat["platforms_term_ckip"]
        plat_news_cor = 0
        plat_news_cor_tc = 0
        save_dict["plat"]=plat
        news_arr =[]
        for news in news_list:
            news_dict = {}
            news_dict["news"] = news
            plat_terms = list(set(plat_terms).difference(set(stopword)))
            story_term_ckip_all = list(set(news["story_term_ckip_all"]).difference(set(stopword)))
            story_term_ckip_tc_all = list(set(news["story_term_ckip_tc_all"]).difference(set(stopword)))

            plat_terms = removeOneTerm(plat_terms)
            story_term_ckip_all = removeOneTerm(story_term_ckip_all)
            story_term_ckip_tc_all = removeOneTerm(story_term_ckip_tc_all)
            
            interArr = list(set(story_term_ckip_all).intersection(set(plat_terms)))
            interArr_tc = list(set(story_term_ckip_tc_all).intersection(set(plat_terms)))
            news_dict["match_term"] = interArr
            news_dict["match_term_tc"] = interArr_tc
            cor_value = 0
            if(len(interArr)!=0):
                cor_value = len(interArr)/len(plat_terms)
            news_dict["cor_value"] = cor_value
            print cor_value
            cor_value_tc = 0
            if(len(interArr_tc)!=0):
                cor_value_tc = len(interArr_tc)/len(plat_terms)
            news_dict["cor_value_tc"] = cor_value_tc
            print cor_value_tc
            print ""
            news_arr.append(news_dict)
            plat_news_cor = plat_news_cor+cor_value
            plat_news_cor_tc = plat_news_cor_tc+cor_value_tc
        ac = plat_news_cor/len(news_list)
        ac_tc = plat_news_cor_tc/len(news_list)
        save_dict["news_list"] = news_arr
        save_dict["ac"] = ac
        save_dict["ac_tc"] = ac_tc
        collection_plat_news.save(save_dict)
    exit(0)