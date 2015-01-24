#encoding=utf-8
import mechanize
import cookielib
import urllib
import logging
import sys
import pymongo
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from time import sleep
from pymongo import MongoClient
from bs4 import BeautifulSoup
import urllib, urllib2
import re

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['councilor']
    collection = db['news_url_list']
    # cr_collection = db['councilors_terms']
    # crs = cr_collection.find()
    # for cr in crs:    
    news_list = collection.find()
    news_list = list(news_list)
    # print news_list[0]["cr"].encode('utf-8')
    for news in news_list:
        id_read = str(news["_id"])
        id = news["_id"]
        try:
            # data = urllib2.urlopen("file:///Users/man27382210/Desktop/paper_g0v/news_html/"+id_read).read()
            # soup = BeautifulSoup(data)
            # story = soup.find('td',{"class":"story"})
            # story = re.sub('<[^<]+?>', '', story.text)
            # print story.encode('utf-8')
            story = news["story"]
            editor_first = story.find(u"【")
            editor_last = story.find(u"】")+1
            editor_char = story[editor_first:editor_last]
            print editor_last
            if(len(editor_char)>0):
                story = story.replace(editor_char, "")
                news["story"] = story
                print story.encode('utf-8')
                news.pop("_id", None)
                collection.update({'_id':id}, {"$set": news}, upsert=False)
        except Exception, e:
            print e
    # for cr in crs:    
    #     news_list = collection.find({"cr_id":cr["_id"]})
    #     news_list = list(news_list)
    #     # print news_list[0]["cr"].encode('utf-8')
    #     for news in news_list:
    #         id_read = str(news["_id"])
    #         id = news["_id"]
    #         try:
    #             data = urllib2.urlopen("file:///Users/man27382210/Desktop/paper_g0v/news_html/"+id_read).read()
    #             soup = BeautifulSoup(data)
    #             story = soup.find('td',{"class":"story"})
    #             story = re.sub('<[^<]+?>', '', story.text)
    #             # print story.encode('utf-8')
    #             editor_first = story.find(u"【")
    #             editor_last = story.find(u"】")+1
    #             editor_char = story[editor_first:editor_last]
    #             story = story.replace(editor_char, "")
    #             news["story"] = story
    #             print story.encode('utf-8')
    #             news.pop("_id", None)
    #             collection.update({'_id':id}, {"$set": news}, upsert=False)
    #         except Exception, e:
    #             print e
    # final_dic = {}
    # for cr in crs:
    #     final_dic[str(cr["_id"])] = {"name":cr["name"], "party":cr["party"], "platform":cr["platform"]}
    # with open('cr.json', 'w') as outfile:
    #   json.dump(final_dic, outfile)

    # collection = db['cr_sim']
    # node = []
    # node_index ={}
    # link = []
    # crs = list(collection.find())
    # count = 0
    # for cr in crs:
    #     node_index[cr["cr_id"]] = count
    #     count = count+1
    #     node.append({"name":cr["cr_id"], "group":1})

    # for cr in crs:
    #     main_id = node_index[cr["cr_id"]]
    #     for sim in cr["cr_sim"]:
    #         sub_id = node_index[sim["sim_id"]]
    #         value = sim["value"]
    #         link.append({"source":main_id, "value":value, "target":sub_id})
    # result = {"nodes":node, "links":link}
    # with open('cr_sim.json', 'w') as outfile:
    #   json.dump(result, outfile)

    # urls = collection.find().skip(179)

    # br = mechanize.Browser()
    # cj = cookielib.LWPCookieJar()
    # br.set_cookiejar(cj)
    # br.set_handle_equiv(True)
    # br.set_handle_redirect(True)
    # br.set_handle_referer(True)
    # br.set_handle_robots(False)
    # br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=20)

    # r= br.open('http://0-udndata.com.millennium.lib.ntust.edu.tw/ndapp/Searchdec2007?udndbid=udndata&page=1&SearchString=%AA%4C%A5%40%A9%76%2B%A4%E9%B4%C1%3E%3D20100101%2B%A4%E9%B4%C1%3C%3D20141217%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8%7C%B8%67%C0%D9%A4%E9%B3%F8%7C%C1%70%A6%58%B1%DF%B3%F8%7CUpaper&sharepage=10&select=1&kind=2')
    # r =br.open('http://0-udndata.com.millennium.lib.ntust.edu.tw/ndapp/Story2007?no=1&page=1&udndbid=udndata&SearchString=qkylQKl2K6TptME%2BPTIwMTAwMTAxK6TptME8PTIwMTQxMjE3K7P4p089wXCmWLP4fLhnwNmk6bP4fMFwplix37P4fFVwYXBlcg%3D%3D&sharepage=10&select=1&kind=2&article_date=2014-11-23&news_id=7760473&showUserSearch=+%3Cstrong%3E%3Cfont+color%3D%23333333+class%3Dtitle03%3E%B1%7A%A5%48%3C%2Ffont%3E+%3Cfont+color%3D%23FF6600+class%3Dtitle04%3E%AA%4C%A5%40%A9%76%2B%A4%E9%B4%C1%3E%3D20100101%2B%A4%E9%B4%C1%3C%3D20141217%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8%7C%B8%67%C0%D9%A4%E9%B3%F8%7C%C1%70%A6%58%B1%DF%B3%F8%7CUpaper%3C%2Ffont%3E+%3Cfont+color%3D%23333333+class%3Dtitle03%3E%A6%40%B7%6A%B4%4D%A8%EC%3C%2Ffont%3E+%3Cfont+color%3D%23FF6600+class%3Dtitle04%3E116%3C%2Ffont%3E+%3Cfont+color%3D%23333333+class%3Dtitle03%3E%B5%A7%B8%EA%AE%C6%3C%2Ffont%3E%3C%2Fstrong%3E&firstFatherCateID=&collectCateNewsPage=1')
    # r = br.open('http://0-udndata.com.millennium.lib.ntust.edu.tw/library/')
    # r = br.open("http://0-udndata.com.millennium.lib.ntust.edu.tw/ndapp/member/MbFixLogin?124921402")

    # count = 0
    # for url in urls:
    #     try:
    #         print count
    #         print url["_id"]
    #         r = br.open("http://0-udndata.com.millennium.lib.ntust.edu.tw"+url["parse_url"])
    #         use = r.read()
    #         file_ = open('./news_html/'+str(url["_id"]), 'w')
    #         file_.write(use)
    #         file_.close()
    #         print "save"
    #         print ""
    #         sleep(5)
    #     except Exception, e:
    #         print "False at index :" + count
    #     finally:
    #         count = count+1
    # print "finish"
    # exit(0)

main()