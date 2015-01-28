# -*- coding: utf-8 -*-

#################################################
# example.py
# ckip.py
#
# Copyright (c) 2012-2014, Chi-En Wu
# Distributed under The BSD 3-Clause License
#################################################

from __future__ import unicode_literals, print_function, division
import re
import os
import sys
import jieba
import jieba.posseg as pseg
from pymongo import MongoClient
from bson.objectid import ObjectId
from ckip import CKIPSegmenter, CKIPParser
from time import sleep

def traverse(root):
    """Helper function to traverse all leaf nodes of the given tree root."""
    if 'child' in root:
        for child in root['child']:
            for leaf in traverse(child):
                yield leaf
    else:
        yield root

segmenter = CKIPSegmenter('gcsn', 'rb303147258')
parser = CKIPParser('gcsn', 'rb303147258')

client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection = db['news_url_list']
collection_save = db['news_url_list_ckip']

# news_list = collection.find({"cr":u"吳碧珠"})
news_list = collection.find()
news_list = list(news_list)
for news in news_list:
    if "story" in news:
        if(len(news['story'])>3):
            try:
                dic_news_save = news
                story_term_ckip_all = []
                story_term_ckip_noun = []
                story_term_ckip_verb = []
                story_term_ckip_tc_all = []
                story_term_ckip_tc_noun = []
                story_term_ckip_tc_verb = []
                story = news['story'].split('\n')

                for ind, sy in enumerate(story):
                    one_sentence = sy
                    print(one_sentence.encode('utf-8'))
                    if len(one_sentence) > 0:
                        result = segmenter.process(one_sentence)
                        if result['status_code'] != '0':
                            print('Process Failure: ' + result['status'])
                        for sentence in list(result['result']):
                            for term in sentence:
                                print(term['term'].encode('utf-8'), term['pos'])
                                if re.match("N", term['pos']) != None:
                                    if ind <=3:
                                        story_term_ckip_tc_all.append(term['term'])
                                        story_term_ckip_tc_noun.append(term['term'])
                                    story_term_ckip_all.append(term['term'])
                                    story_term_ckip_noun.append(term['term'])
                                if re.match("V", term['pos']) != None and term['pos'] != 'ADV':
                                    if ind <=3:
                                        story_term_ckip_tc_all.append(term['term'])
                                        story_term_ckip_tc_verb.append(term['term'])
                                    story_term_ckip_all.append(term['term'])
                                    story_term_ckip_verb.append(term['term'])
                        sleep(3)
                    else:
                        print("len = 0")
                dic_news_save["story_term_ckip_all"] = story_term_ckip_all
                dic_news_save["story_term_ckip_noun"] = story_term_ckip_noun
                dic_news_save["story_term_ckip_verb"] = story_term_ckip_verb
                dic_news_save["story_term_ckip_tc_all"] = story_term_ckip_tc_all
                dic_news_save["story_term_ckip_tc_noun"] = story_term_ckip_tc_noun
                dic_news_save["story_term_ckip_tc_verb"] = story_term_ckip_tc_verb
                print(dic_news_save)
                collection_save.save(dic_news_save)
            except Exception, e:
                print("error")
                print(e)
                sleep(3)