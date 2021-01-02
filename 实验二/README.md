# 实验二 《数据统计和可视化》

---

**题目**

基于实验一中清洗后的数据练习统计和视化操作，100个同学（样本），每个同学有11门课程的成绩（11维的向量）；那么构成了一个100x11的数据矩阵。以你擅长的语言C/C++/Java/Python/Matlab，编程计算：
1. 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
2. 以5分为间隔，画出课程1的成绩直方图。
3. 对每门成绩进行z-score归一化，得到归一化的数据矩阵。
4. 计算出100x100的相关矩阵，并可视化出混淆矩阵。（为避免歧义，这里“协相关矩阵”进一步细化更正为100x100的相关矩阵，100为学生样本数目，视实际情况而定）
5. 根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。

---

### 实验环境

编译器:PyCharm2020.2.3

作业环境:Python 3.8

---

### 实验导入的模块

import matplotlib.pyplot as plt

import random

import pandas as pd

import numpy as np

import seaborn

import math

---

### 文件说明

data5.csv：存放实验一中的数据整理完成后的数据

data5.txt：存放结果，距离每个样本最近的三个样本，题目5的结果ID的矩阵

machine study2.py：实验二的所有代码信息（前3个实验注释后编译的第4、5个实验）

z_score.txt：实验二中题目3的结果，存放z-score的数据矩阵

2-1散点图.jpg：实验二中题目1的结果，可视化散点图

2-2直方图.jpg：实验中题目2的结果，可视化直方图

2-3zscore矩阵.txt：实验二中题目3的矩阵结果，和z_score.txt一样

2-4混淆矩阵.jpg：实验二中题目4的可视化混淆矩阵的结果

2-5最近样本.txt：实验二中题目5的结果，结果ID的矩阵和data5.txt一样

---

#### 数据的规范化

将体育成绩的四个等级bad、general、good、excellent转化为百分制对应的60-70、70-80、80-90、90-100的随机数，同理C6、C7、C8、C9由十分制转化成百分制

代码段:
```
  for i in range(len(lance)):
    if(lance.iloc[i,15])=='bad':
        lance.iloc[i,15]=random.randint(60,70);
    if (lance.iloc[i, 15]) == 'general':
        lance.iloc[i, 15] = random.randint(70,80);
    if (lance.iloc[i, 15]) == 'good':
        lance.iloc[i, 15] = random.randint(80,90);
    if (lance.iloc[i, 15]) == 'excellent':
        lance.iloc[i, 15] = random.randint(90,100);
    lance.iloc[i, 10] *= 10
    lance.iloc[i, 11] *= 10
    lance.iloc[i, 12] *= 10
    lance.iloc[i, 13] *= 10
```
---

### 函数说明

#### machine study2.py

avg(j)：计算均值
```
def avg(j):
    C_sum = 0
    for i in range(len(lance)):
        C_sum = C_sum + lance.iloc[i, j]
    C_avg = C_sum / len(lance)  # 得到平均值
    return C_avg
```

stand(j)：计算标准差
```
def stand(j):
    C_avg=avg(j)
    pingfang = 0
    for i in range(len(lance)):
        pingfang = (lance.iloc[i, j] - C_avg) ** 2 + pingfang
    stand_C = 0
    stand_C = (pingfang / len(lance)) ** 0.5#标准差
    return stand_C
```

z_score()：z-score归一化
```
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
```

new_z_score(numb)：同样归一化计算
```
def new_z_score(numb):   #规范化,为了和上面的zscore区别，函数名字为new_z_score
    avg = sum(numb) / len(numb)
    stan = (sum([(x - avg) ** 2 for x in numb]) / len(numb))**0.5
    zscore =[(i-avg)/stan for i in numb]
    return zscore
```

countrelation(numb1,numb2)：计算两个数组的关系
```
def countrelation(numb1,numb2):   #计算两个数组的关系
    cor=0
    for i in range(len(numb1)):
        cor+=(numb1[i]*numb2[i])
    cor=cor/len(numb1)
    return cor
 ```

BubbleSort(lst)：冒泡排序
```
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
   ```
