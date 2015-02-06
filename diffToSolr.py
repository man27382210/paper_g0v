#encoding=utf-8
import solr
from bson.objectid import ObjectId
from os import listdir
from os.path import isfile, join
import ast
import sys
from itertools import islice
reload(sys)
sys.setdefaultencoding("utf-8")
# from itertools import islice
# create a connection to a solr server
s = solr.SolrConnection('http://114.34.79.27:8983/solr/newsdiff')
N = 3
mypath = "/Volumes/mac/newsdiff"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
for file_use in onlyfiles:
	print file_use
	path = mypath+"/"+file_use
	with open(path, 'r') as f:
		while True:
			try:
				lines = list(islice(f, N))
				dic_use = ast.literal_eval(lines[0])
				print path
				s.add(id=dic_use["id"], title=lines[1], story=lines[2], url=dic_use["url"])	
				if not lines:
					break
			except Exception, e:
				print e
				s.commit()
				print path+"  fail"
			



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
