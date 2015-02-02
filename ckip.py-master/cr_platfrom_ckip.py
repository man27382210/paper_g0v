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

segmenter = CKIPSegmenter('gcsn', 'rb303147258')
parser = CKIPParser('gcsn', 'rb303147258')

client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection = db['cr_platform']
collection_save = db['cr_platform_ckip']
crs = collection.find()
crs = list(crs)
for cr in crs:
    try:
        cr_news = cr
        platforms_term_ckip = []
        platforms_nonu_ckip = []
        platforms_verb_ckip = []
        result = segmenter.process(cr_news["plat_origin"])
        if result['status_code'] != '0':
            print('Process Failure: ' + result['status'])
        for sentence in list(result['result']):
            for term in sentence:
                print(term['term'].encode('utf-8'), term['pos'])
                if re.match("N", term['pos']) != None:
                    platforms_term_ckip.append(term['term'])
                    platforms_nonu_ckip.append(term['term'])
                if re.match("V", term['pos']) != None and term['pos'] != 'ADV':
                    platforms_term_ckip.append(term['term'])
                    platforms_verb_ckip.append(term['term'])
        sleep(2)

        cr_news["platforms_term_ckip"] = platforms_term_ckip
        cr_news["platforms_nonu_ckip"] = platforms_nonu_ckip
        cr_news["platforms_verb_ckip"] = platforms_verb_ckip
        print(cr_news)
        collection_save.save(cr_news)
    except Exception, e:
        print("error")
        print(e)
        sleep(3)