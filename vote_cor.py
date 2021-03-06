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

# http://councils.g0v.tw/api/councilors_terms/143/
# { "councilor": "http://councils.g0v.tw/api/councilors_terms/143/" }
# { url:"http://councils.g0v.tw/api/bills/2157/" }
client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection_cr_bills = db["councilors_bills"]
collection_bill = db['bills']
collection_bill_term = db['bills_term']
collection_cr_plat = db['cr_platform_ckip']
collection_plat_bill = db['plat_bill_cor_ckip']

def marge(plat):
    result_arr = []
    result_arr.extend(plat["bill_nonu_term"])
    result_arr.extend(plat["bill_verb_term"])
    return result_arr
def parseJson():
    json_data=open('stopword.json')
    data = json.load(json_data)
    # pprint(data)
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
    bills_list = list(collection_cr_bills.find({ "councilor": "http://councils.g0v.tw/api/councilors_terms/143/" }))
    bills_list_with_term = []
    for bill_search in bills_list:
        bill_origin = collection_bill.find({"url":bill_search["bill"]})[0]
        bill = collection_bill_term.find({"bill_id":bill_origin["_id"]})[0]
        bills_list_with_term.append(bill)
    plat_list = collection_cr_plat.find({"cr_name":u"吳碧珠"})
    for plat in plat_list:
        save_dict ={}
        plat_terms = plat["platforms_term_ckip"]
        plat_bill_cr = 0
        save_dict["plat"]=plat
        bill_arr = []
        for bill in bills_list_with_term:
            bill_dict = {}
            bill_dict["bill"] = bill
            plat_terms = list(set(plat_terms).difference(set(stopword)))
            bill_term_ckip_all = list(set(bill["bill_all_term"]).difference(set(stopword)))

            plat_terms = removeOneTerm(plat_terms)
            bill_term_ckip_all = removeOneTerm(bill_term_ckip_all)

            interArr = list(set(bill_term_ckip_all).intersection(set(plat_terms)))
            cor_value = 0
            if(len(interArr)!=0):
                cor_value = len(interArr)/len(plat_terms)
            bill_dict["cor_value"] = cor_value
            bill_arr.append(bill_dict)
            plat_bill_cr = plat_bill_cr+cor_value
        ac = plat_bill_cr/len(bills_list_with_term)
        save_dict["bills_list"] = bill_arr
        save_dict["ac"] = ac
        collection_plat_bill.save(save_dict)
    # news_list = collection.find({"cr":u"吳碧珠"})
    # news_list = list(news_list)
    
    # plat_list = list(plat_list)
    # for plat in plat_list:
    #     save_dict ={}
    #     # plat_terms = marge(plat)
    #     plat_terms = plat["platforms_term_ckip"]
    #     plat_news_cor = 0
    #     plat_news_cor_tc = 0
    #     save_dict["plat"]=plat
    #     news_arr =[]
    #     for news in news_list:
    #         news_dict = {}
    #         news_dict["news"] = news
    #         plat_terms = list(set(plat_terms).difference(set(stopword)))
    #         story_term_ckip_all = list(set(news["story_term_ckip_all"]).difference(set(stopword)))
    #         story_term_ckip_tc_all = list(set(news["story_term_ckip_tc_all"]).difference(set(stopword)))

    #         plat_terms = removeOneTerm(plat_terms)
    #         story_term_ckip_all = removeOneTerm(story_term_ckip_all)
    #         story_term_ckip_tc_all = removeOneTerm(story_term_ckip_tc_all)
            
    #         interArr = list(set(story_term_ckip_all).intersection(set(plat_terms)))
    #         interArr_tc = list(set(story_term_ckip_tc_all).intersection(set(plat_terms)))
    #         news_dict["match_term"] = interArr
    #         news_dict["match_term_tc"] = interArr_tc
    #         cor_value = 0
    #         if(len(interArr)!=0):
    #             cor_value = len(interArr)/len(plat_terms)
    #         news_dict["cor_value"] = cor_value
    #         print cor_value
    #         cor_value_tc = 0
    #         if(len(interArr_tc)!=0):
    #             cor_value_tc = len(interArr_tc)/len(plat_terms)
    #         news_dict["cor_value_tc"] = cor_value_tc
    #         print cor_value_tc
    #         print ""
    #         news_arr.append(news_dict)
    #         plat_news_cor = plat_news_cor+cor_value
    #         plat_news_cor_tc = plat_news_cor_tc+cor_value_tc
    #     ac = plat_news_cor/len(news_list)
    #     ac_tc = plat_news_cor_tc/len(news_list)
    #     save_dict["news_list"] = news_arr
    #     save_dict["ac"] = ac
    #     save_dict["ac_tc"] = ac_tc
    #     collection_plat_news.save(save_dict)
    exit(0)