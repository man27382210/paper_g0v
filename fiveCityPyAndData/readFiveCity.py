import os
import glob
import json
from pprint import pprint
json_data=open('tncc_bill_path.json')
data = json.load(json_data)
for path in data:
	json_data_in_path=open(path)
	data_in_path = json.load(json_data_in_path)
	for key in data_in_path:
		# print key.encode('utf-8') + " : " +data_in_path[key].encode('utf-8')
		# print type(data_in_path[key])
		if type(data_in_path[key]) is list:
			for key_in_list in data_in_path[key]:
				# print type(key_in_list)
				print key_in_list.encode('utf-8')
	break

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