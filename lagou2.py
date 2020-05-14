import requests

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'php',
}
headers = {
    'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'cookie': 'RECOMMEND_TIP=true; user_trace_token=20200513195813-90f1b9e4-dd6a-4911-a72c-51f9980d2c8b; LGUID=20200513195813-c596dd47-709c-4e90-a4c4-9003c6eeeb97; _ga=GA1.2.1032403819.1589371094; _gid=GA1.2.1349630106.1589371095; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221720de665b52e7-03bc84c34f58e5-38710758-2073600-1720de665b6707%22%2C%22%24device_id%22%3A%221720de665b52e7-03bc84c34f58e5-38710758-2073600-1720de665b6707%22%7D; JSESSIONID=ABAAABAABEIABCID076D507ACD321610A37B7B1B4A9F1F2; WEBTJ-ID=05142020%2C221205-17213872c30b09-031f22d9e696ae-38710758-2073600-17213872c31962; X_HTTP_TOKEN=36f505aebcc9a21c525564985199a40bf8eea14d03; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; PRE_SITE=https%3A%2F%2Fwww.lagou.com; LGSID=20200514221205-871081ea-0eff-481f-82ed-f126b5f258ea; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1589371094,1589381832,1589465526; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1589465526; TG-TRACK-CODE=index_search; SEARCH_ID=610782d0c2a144ebad141ae045746f08; LGRID=20200514221224-f283abb4-8ef7-43ac-bf31-4a21a9395f62',
    'dnt': '1',
    'origin': 'https://www.lagou.com'
}
respones = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',data=data, headers=headers)
print(respones.text)
