#-*- coding: utf-8 -*-

import string, urllib2

def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i, 5) + '.html'
        print '正在下載第'+ str(i) +'個網頁，並將其存儲爲'+sName+'...'
        f = open(sName, 'w+')
        m = urllib2.urlopen(url+str(i)).read()
        f.write(m)
        f.close()

bdurl = 'http://tieba.baidu.com/p/4312289766?pn='
#begin_page = int(raw_input(u"輸入開始頁數：\n"))
#end_page = int(raw_input(u"輸入終點頁數：\n"))
begin_page = 1
end_page = 2

baidu_tieba(bdurl, begin_page, end_page)
