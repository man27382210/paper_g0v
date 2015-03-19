# coding=UTF-8
import csv
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection_crs = db["ntp_crs"]
with open('ntp_cr_allcity.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	reader = list(reader)
	# print len(reader)
	for i, row in enumerate(reader):
		cr = list(collection_crs.find({"name":row["姓名"]}))
		if len(cr)>0:
			cr = cr[0]
			cr["place"] = row["地區"]
			cr["place_code"] = row["地區代號"]
			cr["cvotes"] = row["得票數"]
			cr["pvotes"] = row["得票率"]
			if row["當選註記"] == u"*":
				cr["beelected"] = True
			else:
				cr["beelected"] = False
			print collection_crs.save(cr)

		# break
		# for i, key in enumerate(row):
		# 	if row[key] == u"*":
		# 		print key+ " : 當選"
		# 	print key +" : "+ row[key]

				
		print ""