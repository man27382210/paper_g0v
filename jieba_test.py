#encoding=utf-8
import jieba

seg_list = jieba.cut("我去你的", cut_all=True)
print "Full Mode:", "/ ".join(seg_list)  # 全模式