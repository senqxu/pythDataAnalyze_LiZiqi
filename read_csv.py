import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#data = {"grammer":["python","C","java","go","R","SQL","PHP","python"], "score":[1,2,3,4,5,6,7,8]}
#df = pd.DataFrame(data)
#df.head(8)

def read_data():
      path =r'C:\Users\XUSE01\Desktop\Transactions.csv'
      data = pd.read_csv(path,encoding='gbk')
      return data

def draw(data):
      data.hist(figsize=(16,14))#画直方图
      plt.savefig("plots.png",dpi=300,pad_inches = 0)
      plt.show()

#data = read_data()
#draw(data)

def draw_heatmap(data):
    ylabels = data.columns.values.tolist()

    ss = StandardScaler()     # 归一化
    data = ss.fit_transform(data)

    df = pd.DataFrame(data)

    dfData = df.corr()
    plt.subplots(figsize=(15, 15)) # 设置画面大小
    sns.heatmap(dfData, annot=True, vmax=1, square=True,yticklabels=ylabels,xticklabels=ylabels, cmap="RdBu")
    plt.savefig('../img/thermodynamicDiagram.jpg')
    plt.show()

def draw_heatmap1(data):
      df=pd.DataFram(data)
      fig=plt.figure()
      sns_plot=sns.hearmap(df)
      plt.show()
      
data = read_data()
draw_heatmap1(data)



