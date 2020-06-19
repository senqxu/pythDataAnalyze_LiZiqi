import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

data = {"grammer":["python","C","java","go","R","SQL","PHP","python"], "score":[1,2,np.nan,4,5,6,7,8]}
df = pd.DataFrame(data)
df.head(8)
#re=df[df['grammer'].str.contains("python")]
#df.columns#输出列名

#df['grammer'].value_counts()#输出列出现的次数
#df.drop_duplicates(['grammer'])/去重
#df['score'].mean()/求平均值
#df['grammer'].to_list()#转换为列
#df.to_excel('filename.xlsx')#存为ecxel
#df.shape#查看行列
#df[df['grammer'] == df['grammer'].max()]#列最大值所在行
#df.tail()#查看最后5行数据
#row={'grammer':'Perl','score':6.6}
#df = df.append(row,ignore_index=True)#添加一行数据['Perl',6.6]
#df.sort_values("score",inplace=True)#列值的大小进行排序
#df['grammer'].map(lambda x: len(x))#列每个字符串的长度
#df.info()
#
# df.score.plot(kind='hist')
df.describe()
df.head(9)

