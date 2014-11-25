# -*- coding: utf-8 -*-
import urllib2
import json
import requests
import pymongo
from pymongo import MongoClient

class Councilor:
	def __init__(self, name, party, title, platform, election_year, url_ct, url_c):
		self.name = name
		self.party = party
		self.title = title
		self.platform = platform
		self.election_year = election_year
		self.url_ct = url_ct
		self.url_c = url_c
	def saveToMongo(self):
		client = MongoClient('mongodb://localhost:27017/')
		db = client['councilor']
		collection = db.cr
		councilor={
			"name":self.name,
			"party":self.party,
			"title":self.title,
			"platform":self.platform,
			"election_year":self.election_year,
			"url_councilor_term": self.url_ct,
			"url_councilor": self.url_c
		}
		print councilor
		id_save = collection.insert(councilor)
		print id_save



def parseFromUrl(url):
	r = requests.get(url)
	data = r.json()
	next = ""
	if data.has_key("next"):
		next = data["next"]
	councilors_arr = data["results"]
	for councilor in councilors_arr:
		each_terms = councilor["each_terms"]
		for term in each_terms:
			if int(term["election_year"]) == 2010:
				if term["county"] == u'臺北市':
					print term["party"]
					print term["title"]
					print term["name"]
					print term["platform"]
					print term["url"]
					print term["councilor"]
					cr = Councilor(term["name"], term["party"], term["title"], term["platform"], "2010", term["url"], term["councilor"])
					cr.saveToMongo()
	if(len(next)!=0):
		parseFromUrl(next)
	else:
		print "end"
		return

if __name__ == '__main__':
	parseFromUrl('http://councils.g0v.tw/api/councilors/?format=json')