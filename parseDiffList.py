# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection = db['ntp_news_url_list']
collection_ckip = db['ntp_news_url_list_ckip']

news_list = list(collection.find({}, fields={"_id":1}))
ckip_list = list(collection_ckip.find({}, fields={"_id":1}))
a = list()
for id_use in news_list:
	a.append(id_use["_id"])
b = list()
for id_use in ckip_list:
	b.append(id_use["_id"])
diff_lisr = list(set(a).difference(set(b)))


for id in diff_lisr:
	f = open("./diff_ids.txt", "a")
	f.write(str(id)+"\n")
f.close()	
