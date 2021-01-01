# -*- codeing = utf-8 -*-
# @Time: 2020/11/22 12:49
# @Author: Lancelot
# @File: machine study1.py
# @Sofeware: PyCharm


import pandas as pd
import numpy as np
import csv
import glob
import math

#将excel文件转换为CSV
def xlsx_to_csv_pd():
    data_xls = pd.read_excel('data1.xlsx', index_col=0)
    data_xls.to_csv('data1.csv', encoding='utf-8')
xlsx_to_csv_pd()

#加载csv数据库
df_csv=pd.read_csv("data1.csv")
df_csv.head()



f1 = pd.read_csv('data1.csv')
f2 = pd.read_csv('data2.csv')
file = [f1,f2]
train = pd.concat(file)
train.to_csv('data3.csv', index=0, sep=',')


#合并成一个新文件
df=pd.read_csv('data3.csv')

Gender=df['Gender'].tolist()
# print(df1)
Gender_new=[]
for i in Gender:
    if i=='female':
        Gender_new.append('girl')
    if i=='male':
        Gender_new.append('boy')
    if i == 'boy':
          Gender_new.append('boy')
    if i == 'girl':
          Gender_new.append('girl')

df['Gender'] = Gender_new

ID=df['ID'].tolist()
ID_new=[]
for i in ID:
    if i<1000:
        ID_new.append(202000+i)
    else:
      ID_new.append(i)
df['ID'] = ID_new

Height=df['Height'].tolist()
Height_new=[]
for i in Height:
    if i<10:
        Height_new.append(i*100)
    else:
      Height_new.append(i)
df['Height'] = Height_new


df.to_csv('data4.csv', index=0, sep=',')



lance=pd.read_csv('data4.csv')

#print(lance.shape)#(197, 16)
#print(lance.info())#了解数据结构
#print(df.describe())
#print(lance.columns)


#去空格


col=lance.columns.values
lance.columns=[x.strip() for x in col]
print(lance.columns)



#当两条记录中所有的数据都相等时才返回true
#print(lance.duplicated())
#找到重复值

print(lance[lance.duplicated()])

#统计有多少个重复值

print(lance.duplicated().sum())

#删除重复值

print(df.drop_duplicates())


#直接在原数据上进行操作


lance.drop_duplicates(inplace=True)

print(lance.shape)


print(df.shape)





#重置索引

df.drop_duplicates(inplace=True)

print(lance.shape[0])
#133
lance.index=range(lance.shape[0])

print(lance.index)


print(lance.duplicated().sum())
#0

#异常值处理

print(df.describe().T)#转置


sta=(df['C1']-df['C1'].mean())/df['C1'].std()

print(df[sta.abs()>3])


#缺失值处理

#查看缺失值

print(lance.isnull().sum())


#新建一个list_C1，存取对于C1重复值的ID，前面的Name那些也需要弄，Name里面有一个乱码
list_C1=[]
list_C1_add=[]#补充的数据
list_C1_empty=[]#对应的ID顺序
a =lance[lance.C1.isnull()]
for i in range(lance.C1.isnull().sum()):
    list_C1.append(a.iloc[i,0])
C1_k=0
for j in range(len(list_C1)):
    for i in range(len(lance)):
        if list_C1[C1_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i, 5])==False:
            list_C1_add.append(lance.iloc[i,5])
            C1_k += 1
        if C1_k > len(list_C1)-1:
            break
    if C1_k > len(list_C1) - 1:
        break
C1_o=0
for j in range(len(list_C1)):
    for i in range(len(lance)):
        if list_C1[C1_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 5]) == True:
            list_C1_empty.append(i)
            C1_o += 1
        if C1_o > len(list_C1) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if C1_o > len(list_C1) - 1:
        break
for i in range(len(list_C1)):
    if len(list_C1_empty) == 0 or len(list_C1_add)==0:
        break
    lance.iloc[list_C1_empty[i], 5] = list_C1_add[i]
print(list_C1_empty)
print(list_C1_add)
print(lance[lance.C1.isnull()])

lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])
#C2
list_C2=[]
list_C2_add=[]#补充的数据
list_C2_empty=[]#对应的ID顺序
a =lance[lance.C2.isnull()]
for i in range(lance.C2.isnull().sum()):
    list_C2.append(a.iloc[i,0])
C2_k=0
for j in range(len(list_C2)):
    for i in range(len(lance)):
        if list_C2[C2_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i, 6])==False:
            list_C2_add.append(lance.iloc[i,6])
            C2_k += 1
        if C2_k > len(list_C2)-1:
            break
    if C2_k > len(list_C2) - 1:
        break
C2_o=0
for j in range(len(list_C2)):
    for i in range(len(lance)):
        if list_C2[C2_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 6]) == True:
            list_C2_empty.append(i)
            C2_o += 1
        if C2_o > len(list_C2) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if C2_o > len(list_C2) - 1:
        break
for i in range(len(list_C2)):
    if len(list_C2_empty) == 0 or len(list_C2_add)==0:
        break
    lance.iloc[list_C2_empty[i], 6] = list_C2_add[i]
print(list_C2_empty)
print(list_C2_add)
print(lance[lance.C2.isnull()])
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])
#C3

list_C3=[]
list_C3_add=[]#补充的数据
list_C3_empty=[]#对应的ID顺序
a =lance[lance.C3.isnull()]
for i in range(lance.C3.isnull().sum()):
    list_C3.append(a.iloc[i,0])
C3_k=0
for j in range(len(list_C3)):
    for i in range(len(lance)):
        if list_C3[C3_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i, 7])==False:
            list_C3_add.append(lance.iloc[i,7])
            C3_k += 1
        if C3_k > len(list_C3)-1:
            break
    if C3_k > len(list_C3) - 1:
        break
C3_o=0
for j in range(len(list_C3)):
    for i in range(len(lance)):
        if list_C3[C3_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 7]) == True:
            list_C3_empty.append(i)
            C3_o += 1
        if C3_o > len(list_C3) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if C3_o > len(list_C3) - 1:
        break
for i in range(len(list_C3)):
    if len(list_C3_empty) == 0 or len(list_C3_add)==0:
        break
    lance.iloc[list_C3_empty[i], 7] = list_C3_add[i]
print(list_C3_empty)
print(list_C3_add)
print(lance[lance.C3.isnull()])
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])
#C4

list_C4=[]
list_C4_add=[]#补充的数据
list_C4_empty=[]#对应的ID顺序
a =lance[lance.C4.isnull()]
for i in range(lance.C4.isnull().sum()):
    list_C4.append(a.iloc[i,0])
C4_k=0
for j in range(len(list_C4)):
    for i in range(len(lance)):
        if list_C4[C4_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i,8])==False:
            list_C4_add.append(lance.iloc[i,8])
            print(lance.iloc[i,8])
            C4_k += 1
        if C4_k > len(list_C4)-1:
            break
    if C4_k > len(list_C4) - 1:
        break
C4_o=0
for j in range(len(list_C4)):
    for i in range(len(lance)):
        if list_C4[C4_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 8]) == True:
            list_C4_empty.append(i)
            C4_o += 1
            print(i)
        if C4_o > len(list_C4) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if C4_o > len(list_C4) - 1:
        break
for i in range(len(list_C4)):
    if len(list_C4_empty) == 0 or len(list_C4_add)==0:
        break
    lance.iloc[list_C4_empty[i],8] = list_C4_add[i]


print(list_C4_empty)
print(list_C4_add)
print(lance[lance.C4.isnull()])
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])

#C5

list_C5=[]
list_C5_add=[]#补充的数据
list_C5_empty=[]#对应的ID顺序
a =lance[lance.C5.isnull()]
for i in range(lance.C5.isnull().sum()):
    list_C5.append(a.iloc[i,0])
C5_k=0
C5_j=0
for j in range(len(list_C5)):
    for i in range(len(lance)):
        if list_C5[C5_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i,9])==False:
            list_C5_add.append(lance.iloc[i,9])
            print(lance.iloc[i,9])
            C5_j+=1
            break
        if C5_k > len(list_C5)-1:
            break
        if i ==len(lance)-1 and C5_j==j:
            list_C5_add.append(0)
    C5_k += 1
    if C5_k > len(list_C5) - 1:
        break
C5_o=0
for j in range(len(list_C5)):
    for i in range(len(lance)):
        if list_C5[C5_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 9]) == True:
            list_C5_empty.append(i)
            C5_o += 1
            print(i)
        if C5_o > len(list_C5) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if C5_o > len(list_C5) - 1:
        break
for i in range(len(list_C5)):
    if len(list_C5_empty) == 0 or len(list_C5_add)==0:
        break
    lance.iloc[list_C5_empty[i],9] = list_C5_add[i]


print(list_C5_empty)
print(list_C5_add)
print(lance[lance.C5.isnull()])
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])

#C6,C5改的没有补充到之前的地方

list_C6=[]
list_C6_add=[]#补充的数据
list_C6_empty=[]#对应的ID顺序
a =lance[lance.C6.isnull()]
for i in range(lance.C6.isnull().sum()):
    list_C6.append(a.iloc[i,0])
C6_k=0
C6_j=0
for j in range(len(list_C6)):
    for i in range(len(lance)):
        if list_C6[C6_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i,10])==False:
            list_C6_add.append(lance.iloc[i,10])
            print(lance.iloc[i,10])
            C6_j+=1
            break
        if C6_k > len(list_C6)-1:
            break
        if i ==len(lance)-1 and C6_j==j:
            list_C6_add.append(0)
    C6_k += 1
    if C6_k > len(list_C6) - 1:
        break
C6_o=0
for j in range(len(list_C6)):
    for i in range(len(lance)):
        if list_C6[C6_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 10]) == True:
            list_C6_empty.append(i)
            C6_o += 1
            print(i)
        if C6_o > len(list_C6) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if C6_o > len(list_C6) - 1:
        break
for i in range(len(list_C6)):
    if len(list_C6_empty) == 0 or len(list_C6_add)==0:
        break
    lance.iloc[list_C6_empty[i],10] = list_C6_add[i]
print(list_C6_empty)
print(list_C6_add)
print(lance[lance.C6.isnull()])
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])


#C7

list_C7=[]
list_C7_add=[]#补充的数据
list_C7_empty=[]#对应的ID顺序
a =lance[lance.C7.isnull()]
for i in range(lance.C7.isnull().sum()):
    list_C7.append(a.iloc[i,0])
C7_k=0
C7_j=0
for j in range(len(list_C7)):
    for i in range(len(lance)):
        if list_C7[C7_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i,11])==False:
            list_C7_add.append(lance.iloc[i,11])
            print(lance.iloc[i,11])
            C7_j+=1
            break
        if C7_k > len(list_C7)-1:
            break
        if i ==len(lance)-1 and C7_j==j:
            list_C7_add.append(0)
    C7_k += 1
    if C7_k > len(list_C7) - 1:
        break
C7_o=0
for j in range(len(list_C7)):
    for i in range(len(lance)):
        if list_C7[C7_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 11]) == True:
            list_C7_empty.append(i)
            C7_o += 1
            print(i)
        if C7_o > len(list_C7) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if C7_o > len(list_C7) - 1:
        break
for i in range(len(list_C7)):
    if len(list_C7_empty) == 0 or len(list_C7_add)==0:
        break
    lance.iloc[list_C7_empty[i],11] = list_C7_add[i]
print(list_C7_empty)
print(list_C7_add)
print(lance[lance.C7.isnull()])
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])


#C8


list_C8=[]
list_C8_add=[]#补充的数据
list_C8_empty=[]#对应的ID顺序
a =lance[lance.C8.isnull()]
for i in range(lance.C8.isnull().sum()):
    list_C8.append(a.iloc[i,0])
C8_k=0
C8_j=0
for j in range(len(list_C8)):
    for i in range(len(lance)):
        if list_C8[C8_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i,12])==False:
            list_C8_add.append(lance.iloc[i,12])
            print(lance.iloc[i,12])
            C8_j+=1
            break
        if C8_k > len(list_C8)-1:
            break
        if i ==len(lance)-1 and C8_j==j:
            list_C8_add.append(0)
    C8_k += 1
    if C8_k > len(list_C8) - 1:
        break
C8_o=0
for j in range(len(list_C8)):
    for i in range(len(lance)):
        if list_C8[C8_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 12]) == True:
            list_C8_empty.append(i)
            C8_o += 1
            print(i)
        if C8_o > len(list_C8) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if C8_o > len(list_C8) - 1:
        break
for i in range(len(list_C8)):
    if len(list_C8_empty) == 0 or len(list_C8_add)==0:
        break
    lance.iloc[list_C8_empty[i],12] = list_C8_add[i]
print(list_C8_empty)
print(list_C8_add)
print(lance[lance.C8.isnull()])
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])


#C9

list_C9=[]
list_C9_add=[]#补充的数据
list_C9_empty=[]#对应的ID顺序
a =lance[lance.C9.isnull()]
for i in range(lance.C9.isnull().sum()):
    list_C9.append(a.iloc[i,0])
C9_k=0
C9_j=0
for j in range(len(list_C9)):
    for i in range(len(lance)):
        if list_C9[C9_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i,13])==False:
            list_C9_add.append(lance.iloc[i,13])
            print(lance.iloc[i,13])
            C9_j+=1
            break
        if C9_k > len(list_C9)-1:
            break
        if i ==len(lance)-1 and C9_j==j:
            list_C9_add.append(0)
    C9_k += 1
    if C9_k > len(list_C9) - 1:
        break
C9_o=0
for j in range(len(list_C9)):
    for i in range(len(lance)):
        if list_C9[C9_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 13]) == True:
            list_C9_empty.append(i)
            C9_o += 1
            print(i)
        if C9_o > len(list_C9) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if C9_o > len(list_C9) - 1:
        break
for i in range(len(list_C9)):
    if len(list_C9_empty) == 0 or len(list_C9_add)==0:
        break
    lance.iloc[list_C9_empty[i],13] = list_C9_add[i]
print(list_C9_empty)
print(list_C9_add)
print(lance[lance.C9.isnull()])
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])



#Height

list_Height=[]
list_Height_add=[]#补充的数据
list_Height_empty=[]#对应的ID顺序
a =lance[lance.Height.isnull()]
for i in range(lance.Height.isnull().sum()):
    list_Height.append(a.iloc[i,0])
Height_k=0
Height_j=0
for j in range(len(list_Height)):
    for i in range(len(lance)):
        if list_Height[Height_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i,4])==False:
            list_Height_add.append(lance.iloc[i,4])
            print(lance.iloc[i,4])
            Height_j+=1
            break
        if Height_k > len(list_Height)-1:
            break
        if i ==len(lance)-1 and Height_j==j:
            list_Height_add.append(0)
    Height_k += 1
    if Height_k > len(list_Height) - 1:
        break
Height_o=0
for j in range(len(list_Height)):
    for i in range(len(lance)):
        if list_Height[Height_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 4]) == True:
            list_Height_empty.append(i)
            Height_o += 1
            print(i)
        if Height_o > len(list_Height) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if Height_o > len(list_Height) - 1:
        break
for i in range(len(list_Height)):
    if len(list_Height_empty) == 0 or len(list_Height_add)==0:
        break
    lance.iloc[list_Height_empty[i],4] = list_Height_add[i]
print(list_Height_empty)
print(list_Height_add)
print(lance[lance.Height.isnull()])
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])

#id
'''
for u in range(len(lance)-1):
    if lance.iloc[u,0]==lance.iloc[u+1,0]:
        v=u
        lance.drop([u])
'''
for i in range(len(lance)):
    if i==len(lance)-1:
        break
    if lance.iloc[i,1]==lance.iloc[i+1,1] and lance.iloc[i,0]!=lance.iloc[i+1,0]:
        lance.iloc[i, 0]=lance.iloc[i+1,0]
    if lance.iloc[i, 0] == lance.iloc[i + 1, 0] and lance.iloc[i, 1] != lance.iloc[i + 1, 1] and lance.iloc[i,5]==lance.iloc[i+1,5]:
        lance.iloc[i , 1] = lance.iloc[i+1, 1]
    if lance.iloc[i,0]==lance.iloc[i+1,0] and lance.iloc[i,3]!=lance.iloc[i+1,3]:
        lance.iloc[i+1, 3]=lance.iloc[i,3]
    if lance.iloc[i,0]==lance.iloc[i+1,0] and lance.iloc[i,15]!=lance.iloc[i+1,15]:
        lance.iloc[i,15]=lance.iloc[i+1,15]

lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])

#Name 找到相同ID的数量，选择其中一个Name 保存 去重


list_Name=[]
list_Name_add=[]#补充的数据
list_Name_empty=[]#对应的ID顺序
a =lance[lance.Name.isnull()]
list_remember=[]#记录所有的ID
for i in range(len(lance)):
    list_remember.append(lance.iloc[i,0])
b=lance
a_mid=0
b_mid=len(lance)
for i in range(len(lance)):
    for j in range(len(lance)):
        if(b.iloc[j,0]==lance.iloc[i,0]):
            lance.iloc[i,1]=b.iloc[j,1]
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])


#Constitution

#先将Constitution转换成数字1bad 2general 3good 4excellent

for i in range(len(lance)):
    if(lance.iloc[i,15])=='bad':
        lance.iloc[i,15]=1;
    if (lance.iloc[i, 15]) == 'general':
        lance.iloc[i, 15] = 2;
    if (lance.iloc[i, 15]) == 'good':
        lance.iloc[i, 15] = 3;
    if (lance.iloc[i, 15]) == 'excellent':
        lance.iloc[i, 15] = 4;

list_Constitution=[]
list_Constitution_add=[]#补充的数据
list_Constitution_empty=[]#对应的ID顺序
a =lance[lance.Constitution.isnull()]
for i in range(lance.Constitution.isnull().sum()):
    list_Constitution.append(a.iloc[i,0])
Constitution_k=0
Constitution_j=0
for j in range(len(list_Constitution)):
    for i in range(len(lance)):
        if list_Constitution[Constitution_k]==lance.iloc[i,0] and math.isnan(lance.iloc[i,15])==False:
            list_Constitution_add.append(lance.iloc[i,15])
            Constitution_j+=1
            break
        if Constitution_k > len(list_Constitution)-1:
            break
        if i ==len(lance)-1 and Constitution_j==j:
            list_Constitution_add.append(0)
            Constitution_j += 1
    Constitution_k += 1
    if Constitution_k > len(list_Constitution) - 1:
        break
Constitution_o=0
for j in range(len(list_Constitution)):
    for i in range(len(lance)):
        if list_Constitution[Constitution_o] == lance.iloc[i, 0] and math.isnan(lance.iloc[i, 15]) == True:
            list_Constitution_empty.append(i)
            Constitution_o += 1
        if Constitution_o > len(list_Constitution) - 1:
            break
        # print(i,lance.iloc[i, 0],list_C1[C1_o],lance.iloc[i, 5])
    if Constitution_o > len(list_Constitution) - 1:
        break
print(list_Constitution)
print(list_Constitution_add)
print(list_Constitution_empty)
for i in range(len(list_Constitution)):
    if len(list_Constitution_empty) == 0 or len(list_Constitution_add)==0:
        break
    lance.iloc[list_Constitution_empty[i],15] = list_Constitution_add[i]

print(list_Constitution_empty)
print(list_Constitution_add)
print(lance[lance.Constitution.isnull()])
lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])

Constitution_avg=int(lance['Constitution'].mean())

#将0的 即空的变成平均值
for i in range(len(lance)):
    if lance.iloc[i,15]==0:
        lance.iloc[i,15]=Constitution_avg


#将Constitution转换成原来的字符串
for i in range(len(lance)):
    if(lance.iloc[i,15])==1:
        lance.iloc[i,15]='bad';
    if (lance.iloc[i, 15]) == 2:
        lance.iloc[i, 15] = 'general'
    if (lance.iloc[i, 15]) == 3:
        lance.iloc[i, 15] = 'good'
    if (lance.iloc[i, 15]) == 4:
        lance.iloc[i, 15] = 'excellent'


#Constitution完成

#将

#将nan类型转换成0 C1-C9
def findnan():
    for i in range(len(lance)):
        for j in range(9):
            if math.isnan(lance.iloc[i, j + 5]) == True:
                lance.iloc[i, j + 5] = 0

findnan()

def get_avg(datag,i):
    sums=0
    for j in range(len(datag)):
        sums=sums+datag.iloc[j,i]
    avgs=sums/len(datag)
    return avgs


#将0的 即空的变成平均值
for i in range(len(lance)):
    for j in range(9):
        if lance.iloc[i,j+5]==0:
            avgg=get_avg(lance,j+5)
            lance.iloc[i, j + 5]=avgg


#list_C1[C1_k]存取ID，溢出133，对应ID
#C1到C9整个循环，最后再去除重复


#再寻找是否有空，空值用均值补充

lance=lance.sort_values(by='ID',ascending=True)
result=sorted(lance ,key = lambda x: x[0])


for i in range(len(lance)):
    if i==len(lance)-1:
        break
    if lance.iloc[i,1]==lance.iloc[i+1,1] and lance.iloc[i,0]!=lance.iloc[i+1,0]:
        lance.iloc[i, 0]=lance.iloc[i+1,0]
    if lance.iloc[i, 0] == lance.iloc[i + 1, 0] and lance.iloc[i, 1] != lance.iloc[i + 1, 1] and lance.iloc[i,5]==lance.iloc[i+1,5]:
        lance.iloc[i , 1] = lance.iloc[i+1, 1]
    if lance.iloc[i,0]==lance.iloc[i+1,0] and lance.iloc[i,3]!=lance.iloc[i+1,3]:
        lance.iloc[i+1, 3]=lance.iloc[i,3]
    if lance.iloc[i,0]==lance.iloc[i+1,0] and lance.iloc[i,15]!=lance.iloc[i+1,15]:
        lance.iloc[i,15]=lance.iloc[i+1,15]


lance.drop_duplicates(inplace=True)
lance.index=range(lance.shape[0])
lance.to_csv('data5.csv', index=0, sep=',')



#完成数据行合并 只保留一个表头


#回答问题
