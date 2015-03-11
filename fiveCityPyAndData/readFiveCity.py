import os
import glob
import json
from pprint import pprint
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection = db['tncc_bill']
json_data=open('tncc_bill_path.json')
data = json.load(json_data)
for path in data:
	json_data_in_path=open(path)
	data_in_path = json.load(json_data_in_path)
	id = collection.insert(data_in_path)
	print id

# pprint(data)
# json_data.close()
# path = '/Users/man27382210/Desktop/paper_g0v/fiveCityPyAndData/tncc/motions'
# arr = []
# for dirPath, dirNames, fileNames in os.walk(path):
# 	if len(dirNames) ==0 and len(fileNames)!=0:
# 		for filename in fileNames:
# 			print dirPath+'/'+ filename
# 			st = dirPath+'/'+ filename
# 			arr.append(st)
# 	print ""
# 		# print dirPath
# 		# print dirNames
# 		# print fileNames
# with open('tncc_bill_path.json', 'w') as outfile:
# 	json.dump(arr, outfile)