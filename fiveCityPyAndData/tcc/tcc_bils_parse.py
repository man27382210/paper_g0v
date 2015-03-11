import os
import glob
import json
from pprint import pprint
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection = db['tcc_bills']
json_data=open('tcc_cr_url.json')
cr_data = json.load(json_data)

cr_keys = cr_data.keys()

json_data=open('bills.json')
bills_data = json.load(json_data)
for bill in bills_data:
	print bill["proposed_by"]
	tmp = [val for val in bill["proposed_by"] if val in cr_keys]
	if len(tmp) >0:
		id = collection.insert(bill)
		print id