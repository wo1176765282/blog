# -*- coding:utf-8 -*-

from sklearn.linear_model import LinearRegression
import numpy as np
# data = np.loadtxt('C:\\Users\\贝贝\\Desktop\\data.txt')
#
# reg = LinearRegression()
# reg.fit(data[:,0].reshape(-1,1),data[:,1])
#
# reg.predict(data[3,0])
# print(reg.intercept_,reg.coef_)


import pandas as pd
def pre(data):
    df=pd.read_csv('G:\\house_price.csv')
    # 把英文列转化为数字，使计算机可以计算 多出来几列
    df1=pd.get_dummies(df[['dist','floor']])
    # 删除原来英文的几列
    del df1['dist_chaoyang']
    del df1['floor_low']
    # axis=1轴拼接
    df2=pd.concat([df,df1],axis=1)
    del df2['dist']
    del df2['floor']
    # 去掉因变量 price   得出x轴矩阵
    df3=df2.drop(['price'],axis=1)
    # 因变量price  为y轴矩阵
    df4=df['price']
    # 引入包 并训练此数据
    from sklearn.linear_model import LinearRegression
    leg=LinearRegression()
    # 得出模型
    legs=leg.fit(df3,df4)
    return legs.predict(data)

    #print(legs.score(df3,df4))
    #print(legs.coef_)   #斜率
    #print(legs.intercept_)    #截距

'''
pd.set_option('display.max_columns', None)
def pre(Data,d=0):
    # pd根据地区选择数据源,d：地区 ，Data:预测矩阵
    if d==0:
        df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\house_price.csv')
    elif d==1:
        df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\house_price.csv')
    else:
        df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\house_price.csv')
    # pd.scatter_matrix  显示最大行等
    df1 = pd.get_dummies(df[['dist', 'floor']])
    del df1['dist_chaoyang']
    del df1['floor_low']
    df2 = pd.concat([df, df1], axis=1)
    del df2['dist']
    del df2['floor']
    df3 = df2.drop(['price'], axis=1)   #X的值矩阵   axis=1轴拼接
    df4 = df['price']   #Y阵
    from sklearn.linear_model import LinearRegression
    leg = LinearRegression()
    legs = leg.fit(df3, df4)
    return legs.predict([Data])
# print(legs.score(df3,df4))  #   拟合度： 0.5959091332283823
# print(legs.coef_)   #斜率  [ 1092.23437222  4218.61495977   -57.77458065  6967.01535292
#  # 11771.75879975 16466.69306314 -7180.93285997 13591.77537519
#  # -8418.94991321 28968.77046877 -2005.70365381  -480.16679346]
# print(legs.intercept_)    #截距  42578.37160000614



'''