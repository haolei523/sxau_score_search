# coding: utf-8

import requests
import pandas as pd

# 添加自己的cookie
headers = {
    'Cookie':'',
    'Referer':'http://xsjwxt.sxau.edu.cn:7873/student/integratedQuery/scoreQuery/allPassingScores/index',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
# 获取数据
session = requests.session()
response = session.get('http://xsjwxt.sxau.edu.cn:7873/student/integratedQuery/scoreQuery/allPassingScores/callback',headers = headers).json()


# 分别整理数据
qiu_2014_2015 = response[0]['cjList']
df = pd.DataFrame(qiu_2014_2015)
print(df)

chun_2014_2015 = response[1]['cjList']
df = pd.DataFrame(chun_2014_2015)
print(df)

qiu_2015_2016 = response[2]['cjList']
df = pd.DataFrame(qiu_2015_2016)
print(df)

chun_2015_2016 = response[3]['cjList']
df = pd.DataFrame(chun_2015_2016)
print(df)

qiu_2016_2017 = response[4]['cjList']
df = pd.DataFrame(qiu_2016_2017)
print(df)

chun_2016_2017 = response[5]['cjList']
df = pd.DataFrame(chun_2016_2017)
print(df)

qiu_2017_2018 = response[6]['cjList']
df = pd.DataFrame(qiu_2017_2018)
print(df)

