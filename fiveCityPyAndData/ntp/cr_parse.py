import os
import glob
import json
from pprint import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection = db['ntp_bills']
json_data=open('ntp_cr_id.json')
cr_id_data = json.load(json_data)
cr_keys = cr_id_data.keys()



# cr_id = {}
# for cr in crs_data:
# 	id = collection.insert(cr)
# 	print id
# 	cr_id[cr["name"]] = str(id)
# with open('ntp_cr_id.json', 'w') as outfile:
# 	json.dump(cr_id, outfile)
# json_data=open('tcc_cr_url.json')
# cr_data = json.load(json_data)

# cr_keys = cr_data.keys()

json_data=open('bills.json')
bills_data = json.load(json_data)
for bill in bills_data:
# 	print bill["proposed_by"]
	proposed_arr = [val for val in bill["proposed_by"] if val in cr_keys]
	petitioned_arr = [val for val in bill["petitioned_by"] if val in cr_keys]
	if len(proposed_arr)>0 or len(petitioned_arr)>0:
		proposed_arr_save = []
		petitioned_arr_save = []
		if len(proposed_arr)>0:
			for cr_name in proposed_arr:
				# print cr_id_data[cr_name]
				proposed_arr_save.append(ObjectId(cr_id_data[cr_name]))
		if len(petitioned_arr)>0:
			for cr_name in petitioned_arr:
				# print cr_id_data[cr_name]
				petitioned_arr_save.append(ObjectId(cr_id_data[cr_name]))
		bill["proposed_id"] = proposed_arr_save
		bill["petitioned_id"] = petitioned_arr_save
		# print bill
		id = collection.insert(bill)
		print id