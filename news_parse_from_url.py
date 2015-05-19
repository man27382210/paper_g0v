#encoding=big5
import mechanize
import cookielib
import urllib
import logging
import sys
import pymongo
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from time import sleep

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['councilor']
    # collection = db['news_url_list']
    collection = db['ntp_news_url_list']
    # urls = list(collection.find().skip(280))
    urls = list(collection.find().skip(1395))

    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=20)

    # r= br.open('http://0-udndata.com.millennium.lib.ntust.edu.tw/ndapp/Searchdec2007?udndbid=udndata&page=1&SearchString=%AA%4C%A5%40%A9%76%2B%A4%E9%B4%C1%3E%3D20100101%2B%A4%E9%B4%C1%3C%3D20141217%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8%7C%B8%67%C0%D9%A4%E9%B3%F8%7C%C1%70%A6%58%B1%DF%B3%F8%7CUpaper&sharepage=10&select=1&kind=2')
    # r =br.open('http://0-udndata.com.millennium.lib.ntust.edu.tw/ndapp/Story2007?no=1&page=1&udndbid=udndata&SearchString=qkylQKl2K6TptME%2BPTIwMTAwMTAxK6TptME8PTIwMTQxMjE3K7P4p089wXCmWLP4fLhnwNmk6bP4fMFwplix37P4fFVwYXBlcg%3D%3D&sharepage=10&select=1&kind=2&article_date=2014-11-23&news_id=7760473&showUserSearch=+%3Cstrong%3E%3Cfont+color%3D%23333333+class%3Dtitle03%3E%B1%7A%A5%48%3C%2Ffont%3E+%3Cfont+color%3D%23FF6600+class%3Dtitle04%3E%AA%4C%A5%40%A9%76%2B%A4%E9%B4%C1%3E%3D20100101%2B%A4%E9%B4%C1%3C%3D20141217%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8%7C%B8%67%C0%D9%A4%E9%B3%F8%7C%C1%70%A6%58%B1%DF%B3%F8%7CUpaper%3C%2Ffont%3E+%3Cfont+color%3D%23333333+class%3Dtitle03%3E%A6%40%B7%6A%B4%4D%A8%EC%3C%2Ffont%3E+%3Cfont+color%3D%23FF6600+class%3Dtitle04%3E116%3C%2Ffont%3E+%3Cfont+color%3D%23333333+class%3Dtitle03%3E%B5%A7%B8%EA%AE%C6%3C%2Ffont%3E%3C%2Fstrong%3E&firstFatherCateID=&collectCateNewsPage=1')
    r = br.open('http://0-udndata.com.millennium.lib.ntust.edu.tw/library/')
    r = br.open("http://0-udndata.com.millennium.lib.ntust.edu.tw/ndapp/member/MbFixLogin?124921402")

    for url in urls:
        try:
            print url["_id"]
            r = br.open("http://0-udndata.com.millennium.lib.ntust.edu.tw"+url["parse_url"])
            use = r.read()
            file_ = open('./ntp_news_html/'+str(url["_id"])+".html", 'w')
            file_.write(use)
            file_.close()
            print "save"
            print ""
            sleep(5)
        except Exception, e:
            print "False id :" + url["_id"]
            f = open("ntp_parse_page_fail.text", a)
            f.write(url["_id"])
            f.close()
    print "finish"
    exit(0)

main()