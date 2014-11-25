# -*- coding: utf-8 -*-
import urllib2
import json
import requests
import pymongo
from pymongo import MongoClient
from time import sleep
import os

# class Councilor:
	# def __init__(self, name, party, title, platform, election_year, url_ct, url_c):
	# 	self.name = name
	# 	self.party = party
	# 	self.title = title
	# 	self.platform = platform
	# 	self.election_year = election_year
	# 	self.url_ct = url_ct
	# 	self.url_c = url_c
def saveToMongo(dictUse):
	print dictUse
	client = MongoClient('mongodb://localhost:27017/')
	db = client['councilor']
	collection = db['bills']
	id_save = collection.insert(dictUse)
	print id_save



def parseFromUrl(url):
	r = requests.get(url)
	data = r.json()
	next = ""
	if data.has_key("next"):
		next = data["next"]
		results = data["results"]
	for result in results:
		if result["county"] == u'臺北市' and result["election_year"] == '2010':
			saveToMongo(result)
		# 			print term["party"]
		# 			print term["title"]
		# 			print term["name"]
		# 			print term["platform"]
		# 			print term["url"]
		# 			print term["councilor"]
		# 			cr = Councilor(term["name"], term["party"], term["title"], term["platform"], "2010", term["url"], term["councilor"])
		# 			cr.saveToMongo()
	# if(len(next)!=0):
	# 	print next
	# 	
	# 	parseFromUrl(next)
	# else:
	# 	print "end"
	# 	return
	# return next

if __name__ == '__main__':
	# parseFromUrl('http://councils.g0v.tw/api/bills/?format=json')
	i = 2107
	while i < 2174:
		# sleep(3)
		print i
		try:
			parseFromUrl('http://councils.g0v.tw/api/bills/?page='+str(i)+'&format=json')
		except Exception, e:
			print e
			print "can't read"
			if os.path.isfile("/Users/man27382210/Desktop/g0v_paper/no_save.txt"):
				print "append"
				with open("no_save.txt", "a") as myfile:
					myfile.write(''+str(i)+'\n')
			else:
				print "new"
				with open("no_save.txt", "w") as myfile:
					myfile.write(''+str(i)+'\n')
			
		i = i+1
