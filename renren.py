from urllib import request
from urllib import parse
from http.cookiejar import CookieJar
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
def get_opener():
    cookiejar = CookieJar()
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    return opener
def login_renren(opener):
    data = {
    'email': '15613852806',
    'password': '15175608090'
    }
    login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)
def visit_profile(opener):
    url = 'http://www.renren.com/426203590/profile'
    req = request.Request(url, headers=headers)
    resp = opener.open(req)
    with open('wanli.html', 'w', encoding='utf-8')as fp:
        fp.write(resp.read().decode('utf-8'))
if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)
