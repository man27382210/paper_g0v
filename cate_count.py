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
collection_cc = db['cr_cate']

cate_all = collection_cate.find()
array = []
for cate in cate_all:
	array.append(str(cate["_id"]))

crs = collection_cr.find()
for cr in crs:
	cr_dic = {"_id":cr["_id"]}
	for cate_name in array:
		cr_dic[cate_name] = 0

	cr_cps = collection_cp.find({"cr_id":cr["_id"]})
	for cr_cp in cr_cps:
		pc = collection_pc.find({"cr_palt_id":str(cr_cp["_id"])})[0]
		for key, value in pc["cate_relation"].iteritems():
			if math.isnan(value):
				pc["cate_relation"][key] = 0
		sorted_x = sorted(pc["cate_relation"].items(), key=operator.itemgetter(1))
		# print pc["cr_palt_id"]
		dic_high = dict([sorted_x[7]])
		key = dic_high.keys()[0]
		val = dic_high.values()[0]
		print key
		print val
		print cr_dic
		cr_dic[key] = cr_dic[key] + 1
	print cr_dic
	# collection_cc.save(cr_dic)
	