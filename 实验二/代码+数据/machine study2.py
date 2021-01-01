# -*- codeing = utf-8 -*-
# @Time: 2020/11/28 13:53
# @Author: Lancelot
# @File: machine study2.py
# @Sofeware: PyCharm

import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
lance=pd.read_csv('data5.csv')


#1.请以课程1成绩为x轴，体能成绩为y轴，画出散点图

#将Constitution变成百分制
for i in range(len(lance)):
    if(lance.iloc[i,15])=='bad':
        lance.iloc[i,15]=random.randint(60,70);
    if (lance.iloc[i, 15]) == 'general':
        lance.iloc[i, 15] = random.randint(70,80);
    if (lance.iloc[i, 15]) == 'good':
        lance.iloc[i, 15] = random.randint(80,90);
    if (lance.iloc[i, 15]) == 'excellent':
        lance.iloc[i, 15] = random.randint(90,100);

plt.scatter(lance.C1, lance.Constitution)

plt.show()

#2. 以5分为间隔，画出课程1的成绩直方图。


plt.hist(x = lance.C1, # 指定绘图数据
         bins = 20, # 指定直方图中条块的个数
        color = 'steelblue', # 指定直方图的填充色
         edgecolor = 'black' # 指定直方图的边框色
         )


plt.show()



#3.对每门成绩进行z-score归一化，得到归一化的数据矩阵

#将十分制的转化成百分制
for i in range(len(lance)):
   lance.iloc[i, 10] *= 10
   lance.iloc[i, 11] *= 10
   lance.iloc[i, 12] *= 10
   lance.iloc[i, 13] *= 10

def avg(j):
    C_sum = 0
    for i in range(len(lance)):
        C_sum = C_sum + lance.iloc[i, j]
    C_avg = C_sum / len(lance)  # 得到平均值
    return C_avg


def stand(j):
    C_avg=avg(j)
    pingfang = 0
    for i in range(len(lance)):
        pingfang = (lance.iloc[i, j] - C_avg) ** 2 + pingfang
    stand_C = 0
    stand_C = (pingfang / len(lance)) ** 0.5#标准差
    return stand_C

data1 = np.mat(np.zeros((len(lance),10)))

def z_score():
    for i in range(len(lance)):
        for j in range(10):
            if j == 9:
                j = 10
            a = avg(j + 5)
            b = stand(j + 5)
            if j == 10:
                data1[i,9] = (lance.iloc[i, j + 5] - a) / b
            if j<10:
                data1[i,j] = (lance.iloc[i, j + 5]-a) / b


z_score()

#将z_score的数据保存，为实验3提供数据
np.savetxt('z_score.txt', data1, fmt="%8f", delimiter='\t') #保存为2位小数的浮点数，用逗号分隔
with open('z_score.txt') as f:
    for line in f:
        print(line, end='')

print(data1)


import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn
import numpy as np
import math


# 读取数据
dataf = ['C1','C2','C3','C4','C5','C6','C7','C8','C9','Constitution']
length=len(lance)
lance = lance[dataf] # 将dataf导入进去
print(lance)
arr=np.c_[lance]  # 按行连接矩阵
print(arr)

def new_z_score(numb):   #规范化,为了和上面的zscore区别，函数名字为new_z_score
    avg = sum(numb) / len(numb)
    stan = (sum([(x - avg) ** 2 for x in numb]) / len(numb))**0.5
    zscore =[(i-avg)/stan for i in numb]
    return zscore
def countrelation(numb1,numb2):   #计算两个数组的关系
    cor=0
    for i in range(len(numb1)):
        cor+=(numb1[i]*numb2[i])
    cor=cor/len(numb1)
    return cor

arr2=np.zeros((length,10))    # 新建一个数组，106行10列，归一化处理
print(arr2)
for i in range(length):
    arr2[i]=new_z_score(arr[i])

relation=np.zeros((length,length))  # 创建关系矩阵
for i in range(length):
    for j in range(length):
        relation[i][j]=countrelation(arr2[i],arr2[j])

print(relation)

seaborn.heatmap(relation,annot=False) #可视化
plt.show()


newarr=np.zeros((length,4))  # 新建一个arr 100*4 存放3个最近的学生ID
rela=np.zeros((length,length))
#冒泡排序
def BubbleSort(lst):
    n=length
    if n<=1:
        return lst
    for i in range (0,n):
        #记录下标
        index = [u for u in range(length)]
        for k in range(0,n):
            for j in range(0,n-k-1):
                if lst[i][j]<=lst[i][j+1]:
                    (lst[i][j], lst[i][j+1]) = (lst[i][j+1], lst[i][j])
                    (index[j], index[j+1]) = (index[j+1], index[j])
        for y in range(0, 4):
            newarr[i][y] = index[y]
    return lst


print("数列按序排列如下：")

print(BubbleSort(relation))
print(newarr)

#除去自己
new_arr=np.zeros((length,3))  # 新建一个arr 100*3 存放3个最近的学生ID
for i in range(length):
    for y in range(1, 4):
        new_arr[i][y-1] = newarr[i][y]
print(new_arr)

lancelot = pd.read_csv('data5.csv')
for i in range(length):   #根据index查找数据
    for j in range(3):
        new_arr[i][j]=lancelot['ID'][new_arr[i][j]]#将学号赋值进去

np.savetxt('data5.txt', new_arr, fmt="%d", delimiter='\t') #保存为2位小数的浮点数，用逗号分隔
with open('data5.txt') as f:
    for line in f:
        print(line, end='')

