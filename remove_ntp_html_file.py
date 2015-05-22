# -*- coding: utf-8 -*-
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection = db['ntp_news_url_list']


def returnFile():
    with open("./ckip.py-master/diff_ids.txt") as f:
        content = f.readlines()
        return content
def removeFile():
	news_list = returnFile()
	for news_id in news_list:
		news_id = news_id.split("\n")[0]
		print news_id
		os.remove('./ntp_news_html/'+news_id+".html")

def removeMongo():
	news_list = returnFile()
	for news_id in news_list:
		news_id = news_id.split("\n")[0]
		collection.remove({"_id":ObjectId(news_id)})

removeMongo()
