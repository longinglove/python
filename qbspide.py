# -*- coding:utf-8 -*-

import urllib
import urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)

content = response.read().decode('utf-8')
pattern = re.compile('<div.*?author>')
print response.read()
