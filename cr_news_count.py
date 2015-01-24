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
from bs4 import BeautifulSoup
import urllib, urllib2
import re

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['councilor']
    collection = db['news_url_list']
    cr_collection = db['councilors_terms']
    crs = cr_collection.find()
    for cr in crs:
        news_list = collection.find({"cr_id":cr["_id"]})
        news_list = list(news_list)
        print cr["name"].encode('utf-8')
        print len(news_list)
        print ""
        # print news_list[0]["cr"].encode('utf-8')
        # for news in news_list:
        #     id_read = str(news["_id"])
        #     id = news["_id"]
        #     data = urllib2.urlopen("file:///Users/man27382210/Desktop/paper_g0v/news_html/"+id_read).read()
        #     soup = BeautifulSoup(data)
        #     try:
        #         story = soup.find('td',{"class":"story"})
        #         story = re.sub('<[^<]+?>', '', story.text)
        #         # print story.encode('utf-8')
        #         editor_first = story.find(u"【")
        #         editor_last = story.find(u"】")+1
        #         editor_char = story[editor_first:editor_last]
        #         story = story.replace(editor_char, "")
        #         news["story"] = story
        #         print story.encode('utf-8')
        #         news.pop("_id", None)
        #         collection.update({'_id':id}, {"$set": news}, upsert=False)
        #     except Exception, e:
        #         print e
main()