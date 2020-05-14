from urllib import request
url = 'http://www.renren.com/426203590/profile'
headers={
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'Cookie':'anonymid=ka6q8jbr-4z9hd3; depovince=HEB; _r01_=1; ick_login=017bf39c-0fdc-4dac-917c-d81356aff1be; jebecookies=a412f542-1438-400d-ab60-357677cc1f43|||||; taihe_bi_sdk_uid=60a29b23149fa3edf9eb7a4da71a5832; taihe_bi_sdk_session=c06c36c38ddcaab381427c65276be3ad; _de=E4D57F125BFA8F7722D1361953B7C8FA; p=3fee974c674e9be2132ec350c11bb8c83; first_login_flag=1; ln_uact=15613852806; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20131007/0925/h_main_pF13_056000000eb1111a.jpg; t=5c3e49b3f06003674438dc42183ad7733; societyguester=5c3e49b3f06003674438dc42183ad7733; id=332498033; xnsid=eceb26b8; ver=7.0; loginfrom=null; wp_fold=0'
}
req = request.Request(url, headers=headers)
resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
with open('renren.html', 'w', encoding='utf-8')as fp:
    fp.write(resp.read().decode('utf-8'))
