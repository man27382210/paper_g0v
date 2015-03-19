#encoding=utf-8
from __future__ import division
from pymongo import MongoClient
from bson.objectid import ObjectId

# 計算議員的評分 為證件達成率/政見總數
# 最後計算全新北市排名、分區排名
# 並且比較得票率 看是不是一樣

client = MongoClient('mongodb://localhost:27017/')
db = client['councilor']
collection_crs = db["ntp_crs"]
ntp_plat_bill_cor_weight_one_fourth = db['ntp_plat_bill_cor_weight_one_fourth']
ntp_plat_bill_cor_weight_one_third = db['ntp_plat_bill_cor_weight_one_third']

if __name__ == "__main__":
    cr_list = list(collection_crs.find())
    for cr in cr_list:
        plat_bill_cor_fourth = list(ntp_plat_bill_cor_weight_one_fourth.find({"cr_id":cr["_id"]}))
        cr_origin_ac = 0
        cr_weight_ac_fourth = 0
        cr_weight_ac_mince_fourth = 0
        cr_weight_ac_cor_fourth = 0
        cr_weight_ac_cor_mince_fourth = 0
        for plat_bill in plat_bill_cor_fourth:
            cr_origin_ac = cr_origin_ac + plat_bill["origin_ac"]
            cr_weight_ac_fourth =  cr_weight_ac_fourth + plat_bill["weight_ac"]
            cr_weight_ac_mince_fourth = cr_weight_ac_mince_fourth + plat_bill["weight_ac_mince"]
            cr_weight_ac_cor_fourth = cr_weight_ac_cor_fourth + plat_bill["weight_ac_with_cor"]
            cr_weight_ac_cor_mince_fourth = cr_weight_ac_cor_mince_fourth + plat_bill["weight_ac_with_cor_mince"]
        cr_origin_ac = cr_origin_ac/ len(plat_bill_cor_fourth)
        cr_weight_ac_fourth = cr_weight_ac_fourth/ len(plat_bill_cor_fourth)
        cr_weight_ac_mince_fourth = cr_weight_ac_mince_fourth/ len(plat_bill_cor_fourth)
        cr_weight_ac_cor_fourth = cr_weight_ac_cor_fourth/ len(plat_bill_cor_fourth)
        cr_weight_ac_cor_mince_fourth = cr_weight_ac_cor_mince_fourth/ len(plat_bill_cor_fourth)

        plat_bill_cor_third = list(ntp_plat_bill_cor_weight_one_third.find({"cr_id":cr["_id"]}))
        cr_weight_ac_third = 0
        cr_weight_ac_mince_third = 0
        cr_weight_ac_cor_third = 0
        cr_weight_ac_cor_mince_third = 0
        for plat_bill in plat_bill_cor_third:
            cr_weight_ac_third = cr_weight_ac_third + plat_bill["weight_ac"] 
            cr_weight_ac_mince_third = cr_weight_ac_mince_third + plat_bill["weight_ac_mince"]
            cr_weight_ac_cor_third = cr_weight_ac_cor_third + plat_bill["weight_ac_with_cor"]
            cr_weight_ac_cor_mince_third = cr_weight_ac_cor_mince_third + plat_bill["weight_ac_with_cor_mince"]
        cr_weight_ac_third = cr_weight_ac_third / len(plat_bill_cor_third)
        cr_weight_ac_mince_third = cr_weight_ac_mince_third / len(plat_bill_cor_third)
        cr_weight_ac_cor_third = cr_weight_ac_cor_third / len(plat_bill_cor_third)
        cr_weight_ac_cor_mince_third = cr_weight_ac_cor_mince_third / len(plat_bill_cor_third)

        cr["cr_origin_ac"] = cr_origin_ac
        cr["cr_weight_ac_fourth"] = cr_weight_ac_fourth
        cr["cr_weight_ac_mince_fourth"] = cr_weight_ac_mince_fourth
        cr["cr_weight_ac_cor_fourth"] = cr_weight_ac_cor_fourth
        cr["cr_weight_ac_cor_mince_fourth"] = cr_weight_ac_cor_mince_fourth
        cr["cr_weight_ac_third"] = cr_weight_ac_third
        cr["cr_weight_ac_mince_third"] = cr_weight_ac_mince_third
        cr["cr_weight_ac_cor_third"] = cr_weight_ac_cor_third
        cr["cr_weight_ac_cor_mince_third"] = cr_weight_ac_cor_mince_third
        print cr
        collection_crs.save(cr)
