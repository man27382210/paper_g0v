import pymongo
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
import operator
import math


client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection_cate = db['bills_catgory_terms']
collection_cr = db['councilors_terms']
collection_pc = db['plat_cate']
collection_cp = db['cr_platform']

crs = collection_cr.find()
for cr in crs:
	cr_dic = {"_id":cr["_id"]}
	
	cr_cps = collection_cp.find({"cr_id":cr["_id"]})
	for cr_cp in cr_cps:
		pc = collection_pc.find({"cr_palt_id":str(cr_cp["_id"])})[0]
		for key, value in pc["cate_relation"].iteritems():
			if math.isnan(value):
				pc["cate_relation"][key] = 0
		sorted_x = sorted(pc["cate_relation"].items(), key=operator.itemgetter(1))
		print pc["cr_palt_id"]
		dic_high = dict([sorted_x[7]])
		key = dic_high.keys()[0]
		val = dic_high.keys()[0]
		
		print ""
	
	