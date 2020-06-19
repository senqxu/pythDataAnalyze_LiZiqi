import numpy as np
import pandas as pd
import re
from pyecharts.charts import Pie, Line, Tab, Map, Bar, WordCloud, Page
from pyecharts import options as opts
from pyecharts.globals import SymbolType
import stylecloud

# 读数据
path = r'C:\A-SMS-work\python demo\LiZiqiDataAnalyze/李子柒视频数据.xlsx'

df = pd.read_excel(path, encoding='utf-8', error_bad_lines=False)
print(df.head())

def transform_num(x):
    str1 = str(x)
    if '万' in str1:
        return float(str1.strip('万'))*10000
    else:
        return float(str1)

# 提取数据
df['title_1'] = df.title.str.extract('【(.*?)】.*')
df['title_2'] = df.title.str.split('】').str[-1]
df['top_rank'] = df.top_rank.str.extract('最高全站日排行(\d+)名')
df['view_num'] = df.view_num.str.extract('(\d+)')
df['dm_num'] = df.dm_num.str.extract('(\d+)')
df['dianzan'] = df.dianzan.apply(lambda x: transform_num(x))
df['toubi'] = df.toubi.apply(lambda x: transform_num(x))
df['shoucang'] = df.shoucang.apply(lambda x: transform_num(x))
df['zhuanfa'] = df.zhuanfa.apply(lambda x: transform_num(x))

# 转换类型
df['view_num'] = df.view_num.astype('int')
df['dm_num'] = df.dm_num.astype('int')
df['publish_time'] = pd.to_datetime(df['publish_time'])

print(df.head(2))