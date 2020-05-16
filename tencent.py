from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tencent.html', parser=parser)
# 1 获取所有cr标签
# spans = html.xpath('//span')
# for span in spans:
#     print(etree.tostring(span, encoding='utf-8').decode('utf-8'))
# 2 获取第二个span标签
# span = html.xpath('//span[2]')[0]
# print(etree.tostring(span, encoding='utf-8').decode('utf-8'))
# 3 获取所有h4为recruit-title
# trs = html.xpath('//h4[@class="recruit-title"]')
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))
# 4 获取a标签下的href属性
# aList = html.xpath('//a/@href')
# for a in aList:share-detail
#     print(a)
# 5 获取所有职位信息文本
alist = html.xpath('//div[position()>6]')
for a in alist:
    hrefs = a.xpath('.//div/@id')[1]
    print(hrefs)
