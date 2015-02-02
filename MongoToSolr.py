#encoding=utf-8
import solr
from pymongo import MongoClient
from bson.objectid import ObjectId

# create a connection to a solr server
s = solr.SolrConnection('http://localhost:8983/solr/newslist')
client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection = db['news_url_list']
# add a document to the index
news_url_list = list(collection.find())
for news in news_url_list:
	try:
		use_story = news["story"].rstrip()
		if(len(use_story)>0):
			s.add(id=news["_id"], title=news["parse_url_name"], crname=news["cr"], cr_id=news["cr_id"], story=use_story, url=news["parse_url"])
		else:
			print use_story.encode("utf-8")
	except Exception, e:
		print e
		print "error"
s.commit()
	


# do a search
# response = s.query('title:測試')
# for hit in response.results:
#     print hit['title'].encode('utf-8')
