#encoding=utf-8
import solr
from bson.objectid import ObjectId
from os import listdir
from os.path import isfile, join
import ast
# from itertools import islice
# create a connection to a solr server
s = solr.SolrConnection('http://localhost:8983/solr/newsdiff')
N = 3
mypath = "/Users/gcsn/Downloads/newsdiff"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
for file_use in onlyfiles:
	path = mypath+"/"+file_use
	with open(path, 'r') as infile:
		lines = [line for line in infile][:N]
		dic_use = ast.literal_eval(lines[0])
		s.add(id=dic_use["id"], title=lines[1], story=lines[2], url=dic_use["url"])
		s.commit()
		break		
# client = MongoClient('mongodb://localhost:27017/')
# db = client['councilor']
# collection = db['news_url_list']
# # add a document to the index
# news_url_list = list(collection.find())
# for news in news_url_list:
# 	try:
# 		use_story = news["story"].rstrip()
# 		if(len(use_story)>0):
# 			s.add(id=news["_id"], title=news["parse_url_name"], crname=news["cr"], cr_id=news["cr_id"], story=use_story, url=news["parse_url"])
# 		else:
# 			print use_story.encode("utf-8")
# 	except Exception, e:
# 		print e
# 		print "error"
# s.commit()
	


# do a search
# response = s.query('title:測試')
# for hit in response.results:
#     print hit['title'].encode('utf-8')
