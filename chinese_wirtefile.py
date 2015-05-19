#this file can really write chinese name.


#encoding=utf-8
import pymongo
import json
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
from pymongo import MongoClient
import codecs


client = MongoClient('mongodb://localhost:27017/')
db = client['startuptaiwan']
collection = db['posts']

results = collection.find({"content.reflections":{"$exists":True}})
for r in results:
	f = codecs.open('test.txt','a','utf-8')
	f.write(r["content"]["reflections"].encode('utf-8')+'\n') # python will convert \n to os.linesep
	f.close()
	