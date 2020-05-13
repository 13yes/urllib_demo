from urllib import request

url = 'https://www.lgstatic.com/lg-www-fed/pkg/search-result/page/index/main.html_aio_2_8cd72e1.js'
header = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='}
req = request.Request(url, headers=header)
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
