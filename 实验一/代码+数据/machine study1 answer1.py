# -*- codeing = utf-8 -*-
# @Time: 2020/11/27 19:13
# @Author: Lancelot
# @File: machine study1 answer1.py
# @Sofeware: PyCharm

import pandas as pd
import numpy as np
import csv
import glob
import math

lance=pd.read_csv('data5.csv')


#不能用库函数,将体能测试也变成百分制
#1. 学生中家乡在Beijing的所有课程的平均成绩

list_BJavg=[]

for i in range(len(lance)):
    if(lance.iloc[i,15])=='bad':
        lance.iloc[i,15]=25;
    if (lance.iloc[i, 15]) == 'general':
        lance.iloc[i, 15] = 50;
    if (lance.iloc[i, 15]) == 'good':
        lance.iloc[i, 15] = 75;
    if (lance.iloc[i, 15]) == 'excellent':
        lance.iloc[i, 15] = 100;

for i in range(len(lance)):
    if lance.iloc[i,2]=='Beijing':
        sum=lance.iloc[i,5]+lance.iloc[i,6]+lance.iloc[i,7]+lance.iloc[i,8]+lance.iloc[i,9]+lance.iloc[i,10]*10+lance.iloc[i,11]*10+lance.iloc[i,12]*10+lance.iloc[i,13]*10+lance.iloc[i,15]
        list_BJavg.append(sum/10)
BJsum=0
for i in range(len(list_BJavg)):
    BJsum=BJsum+list_BJavg[i]
BJavg=BJsum/len(list_BJavg)

print('学生中家乡在Beijing的所有课程的平均成绩:',BJavg,'(包括体测成绩)')


#2.学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。

count_gz=0#统计的数量

for i in range(len(lance)):
    if lance.iloc[i,2]=='Guangzhou'and lance.iloc[i,5]>80and lance.iloc[i,13]>9and lance.iloc[i,3]=='boy':
        count_gz+=1

print("学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量为:",count_gz)

#3. 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？

list_gz_con=[]
list_sh_con=[]

for i in range(len(lance)):
    if lance.iloc[i,2]=='Shanghai' and lance.iloc[i,3]=='girl':
        list_sh_con.append(lance.iloc[i,15])

for i in range(len(lance)):
    if lance.iloc[i,2]=='Guangzhou' and lance.iloc[i,3]=='girl':
        list_gz_con.append(lance.iloc[i,15])

sum_gz_con=0
sum_sh_con=0

for i in range(len(list_gz_con)):
    sum_gz_con=sum_gz_con+list_gz_con[i]

for i in range(len(list_sh_con)):
    sum_sh_con=sum_sh_con+list_sh_con[i]


print("广州女生的平均体能测试成绩:",sum_gz_con/len(list_gz_con))
print("上海女生的平均体能测试成绩:",sum_sh_con/len(list_sh_con))
if sum_gz_con/len(list_gz_con)>sum_sh_con/len(list_sh_con):
    print("故广州女生的平均体能比上海女生好")
if sum_gz_con/len(list_gz_con)<sum_sh_con/len(list_sh_con):
    print("故上海女生的平均体能比广州女生好")
if sum_gz_con/len(list_gz_con)==sum_sh_con/len(list_sh_con):
    print("故上海女生和广州女生的平均体能相近")

#4.学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

#不能使用库函数

#将后面的十分制转成百分制

for i in range(len(lance)):
   lance.iloc[i,10]*=10
   lance.iloc[i, 11] *= 10
   lance.iloc[i, 12] *= 10
   lance.iloc[i, 13] *= 10

#Constitution的平均值
Con_sum=0
for i in range(len(lance)):
    Con_sum=Con_sum+lance.iloc[i,15]
Con_avg=Con_sum/len(lance)


pingfang=0
for i in range(len(lance)):
    pingfang=abs(lance.iloc[i,15]-Con_avg)**2+pingfang

stand_Con=0
stand_Con=(pingfang/len(lance))**0.5

#C1的平均值
C1_sum=0
for i in range(len(lance)):
    C1_sum=C1_sum+lance.iloc[i,5]
C1_avg=C1_sum/len(lance)

#使用库函数验证标准差
list_ha=[]
for i in range(len(lance)):
    list_ha.append(lance.iloc[i,12])

pingfang=0
for i in range(len(lance)):
    pingfang=abs(lance.iloc[i,5]-C1_avg)**2+pingfang

stand_C1=0
stand_C1=(pingfang/len(lance))**0.5

##cov验证

#C1和Constitution的协方差
xiefangcha=0

for i in range(len(lance)):
    xiefangcha=lance.iloc[i,5]*lance.iloc[i,15]+xiefangcha

finalxie=xiefangcha/len(lance)-Con_avg*C1_avg


C1_Con=finalxie/(stand_C1*stand_Con)


#写一个函数可以调用的
def xiefangcha(j):
    C_sum = 0
    for i in range(len(lance)):
        C_sum = C_sum + lance.iloc[i, j]
    C_avg = C_sum / len(lance)


    pingfang = 0
    for i in range(len(lance)):
        pingfang = (lance.iloc[i, j] - C_avg) ** 2 + pingfang

    stand_C = 0
    stand_C = (pingfang / len(lance)) ** 0.5
    xiefangcha = 0


    for i in range(len(lance)):
        xiefangcha = lance.iloc[i, j] * lance.iloc[i, 15] + xiefangcha
    xiefangcha=xiefangcha/len(lance)
    a=xiefangcha
    b=Con_avg * C_avg
    #finalxie = float(xiefangcha - (Con_avg * C_avg))
    finalxie=(a-b)*len(lance)
    C_Con = finalxie / (stand_C * stand_Con)
    k=abs(C_Con)
    k=float(k)
    return k

for i in range(9):
    x=xiefangcha(i+5)
    print('C',i+1,"课程成绩与体能测试成绩彼此之间的相关系数:",x)


