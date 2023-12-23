from lxml import etree
import requests
from fake_useragent import UserAgent
import random
import pandas as pd
import time
import csv
import urllib3
import re
import requests

# 设置请求头参数：User-Agent, cookie, referer
headers_rep = {
    'User-Agent' : UserAgent().random,
    'cookie' : "_ga=GA1.3.578453534.1700446823; SERVERID=wb03; _ga_65K8PR1QER=GS1.3.1700446823.1.1.1700446905.0.0.0",
    # 设置从何处跳转过来
    'referer': 'https://www.house.gov/leadership',
    'Connection': 'close'
}

url_rep = 'https://www.house.gov/representatives'# 首页网址URL
#proxies={'http': 'http://127.0.0.1:1080', 'https': 'http://127.0.0.1:1080'}
requests.get(url_rep, verify=False)
requests.urllib3.disable_warnings()
page_text = requests.get(url=url_rep, headers=headers_rep).text#请求发送
tree = etree.HTML(page_text)#数据解析
result_rep = tree.xpath('//td/a/text()' + '\n')
result_repinfo = tree.xpath('//td/text()')
#print(result_rep)

headers_sen = {
    'User-Agent' : UserAgent().random,
    'cookie' : "_ga=GA1.3.578453534.1700446823; SERVERID=wb03; _ga_65K8PR1QER=GS1.3.1700446823.1.1.1700446905.0.0.0",
    # 设置从何处跳转过来
    'referer': 'https://www.senate.gov/senators/index.htm',
    'Connection': 'close'
}

url_sen = 'https://www.senate.gov/senators/index.htm'# 首页网址URL
#proxies={'http': 'http://127.0.0.1:1080', 'https': 'http://127.0.0.1:1080'}
requests.get(url_rep, verify=False)
requests.urllib3.disable_warnings()
page_text = requests.get(url=url_sen, headers=headers_sen).text#请求发送
tree = etree.HTML(page_text)#数据解析

result_senname = tree.xpath('//td/a/text()')
result_seninfo = tree.xpath('//td/text()')

x=0
sen_state = []
sen_party = []
sen_class = []
sen_or = []
sen_tel = []
while(x <= len(result_seninfo)-1):
    sen_state.append(result_seninfo[x])
    sen_party.append(result_seninfo[x+1])
    sen_class.append(result_seninfo[x+2])
    sen_or.append(result_seninfo[x+3])
    sen_tel.append(result_seninfo[x+4])
    x=x+5


for i in range(len(result_senname)):
    result_senname[i] = re.sub(',', '', result_senname[i])
    namesplit=result_senname[i].split( )
    if len(namesplit) == 2:
        namesplit[0], namesplit[1] = namesplit[1], namesplit[0]
    if len(namesplit) == 3:
        namesplit[0], namesplit[1], namesplit[2] = namesplit[1], namesplit[2], namesplit[0]
    
    result_senname[i] = ''.join(namesplit)

for i in range(len(result_rep)):
    result_rep[i] = re.sub(',', '', result_rep[i])
    namesplit=result_rep[i].split( )
    if len(namesplit) == 2:
        namesplit[0], namesplit[1] = namesplit[1], namesplit[0]
    if len(namesplit) == 3:
        namesplit[0], namesplit[1], namesplit[2] = namesplit[1], namesplit[2], namesplit[0]
    
    result_rep[i] = ''.join(namesplit)
columns = ['Name','State','Party','Class','Office','Tel']

sen_dic = {'姓名':result_senname, '州':sen_state, '党':sen_party, '办公室':sen_or, '电话':sen_tel}
# data1为list类型，参数index为索引，column为列名
resultdata = pd.DataFrame(sen_dic)
# PATH为导出文件的路径和文件名
resultdata.to_csv('sen_name.csv',index=False)

resultdata = pd.DataFrame(data = result_rep,columns = None)

resultdata.to_csv('rep_name.csv',index=False)

print(result_senname)
print(result_seninfo)