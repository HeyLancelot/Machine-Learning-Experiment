# 实验三  《k-means聚类算法》

---

### 实验说明

在课下询问老师可以使用python完成编译，python可视化等操作比较方便，选择python编译

---

**题目**

实现k-means聚类算法，
1. 对实验二中的z-score归一化的成绩数据进行测试，观察聚类为2类，3类，4类，5类的结果，观察得出什么结论？
2. 由老师给出测试数据，进行测试，并画出可视化出散点图，类中心，类半径，并分析聚为几类合适。

x|y
---|:--:
3.45|7.08
1.76|7.24
4.29|9.55
3.35|6.65
3.17|6.41
3.68|5.99
2.11|4.08
2.58|7.10
3.45|7.88
6.17|5.40
4.20|6.46
5.87|3.87
5.47|2.21
5.97|3.62
6.24|3.06
6.89|2.41
5.38|2.32
5.13|2.73
7.26|4.19
6.32|3.62

找到聚类中心后，判断(2,6)是属于哪一类？

---

### 实验环境

编译器:PyCharm2020.2.3

作业环境:Python 3.8

---

### 实验导入的模块

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

import random

---

### 文件说明

data6.csv：老师提供的数据源，即上面的列表

machine study3.py：整个实验的源代码文件

z_score.txt：实验二中z-score得到的结果

降维后可视化.jpg：数据降维之后的散点图

3-1聚2类.jpg：实验三题目1的聚2类的可视化结果

3-1聚3类.jpg：实验三题目1的聚3类的可视化结果

3-1聚4类.jpg：实验三题目1的聚4类的可视化结果

3-1聚5类.jpg：实验三题目1的聚5类的可视化结果

3-2聚2类.jpg：实验三题目2的聚2类的可视化结果

3-2聚3类.jpg实验三题目2的聚3类的可视化结果

3-2(2,6)的所属类别.txt：回答题目的问题，（2，6）的所属聚类

---

### 数据的规范化

由于使用的是实验二中的z-score结果，因此采用同样的数据规范化

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

pca(dataset,N=999999)：将数据降维，但我由于之前在函数外已完成降维，所以没有调用这个函数，将函数封装方便以后使用
```
def pca(dataset,N=999999):
    meanvals=dataset.mean(0)
    meanremoved=dataset-meanvals
    covmat=np.mat(np.cov(meanremoved,rowvar=0))
    eigvals,eigvects=np.linalg.eig(covmat)
    eigvalind=np.argsort(eigvals)
    eigvalind=eigvalind[:-(N+1):-1]
    redeigvects=eigvects[:,eigvalind]
    lowdatamat=np.mat(meanremoved)*redeigvects
    reconmat=(lowdatamat*redeigvects.T)+np.mat(meanvals)
    return lowdatamat
```

distances(arrA, arrB)：欧氏距离计算
```
def distances(arrA, arrB):
    d = arrA - arrB
    s = (np.sum(np.power(d, 2), axis=1))
    dist = np.sqrt(s.tolist())
    return dist
```

randCent(dataSet, k)：为给定数据集构建一个包含K个随机质心的集合
```
def randCent(dataSet, k):
    n=dataSet.shape[1]#有n列
    data_min=dataSet.iloc[:,:n-1].min()#找出最小值
    data_max=dataSet.iloc[:,:n-1].max()#找出最大值
    randCent = np.random.uniform(data_min, data_max, (k, n-1))#data_min之前data_max，生成k行n-1列的数
    return randCent
```

kMeans(dataSet,k)：进行K-Means聚类，迭代
```
def kMeans(dataSet,k):
    m,n=dataSet.shape#得到dataSet里面有多少行，多少列
    centroid=randCent(dataSet,k)#随机生成k个质心
    print("质心")
    print(centroid)
    clusterAssment=np.zeros((m,3))#初始化矩阵
    clusterAssment[:,0]=np.inf#第0列表示距离，初始都设置为无穷大
    clusterAssment[:,1:3]=-1#第1列表示本次迭代簇的标号 第2列为上次迭代簇的标号
    #result_set=np.concatenate([one_list, three_list.T], axis=1)
    result_set=pd.concat([dataSet,pd.DataFrame(clusterAssment)],axis=1,ignore_index=True)#对列连接
    clusterChanged=True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            dist=distances(dataSet.iloc[i,:n-1].values,centroid)
            result_set.iloc[i,n]=dist.min()#最小值
            result_set.iloc[i,n+1]=np.where(dist==dist.min())[0]#返回最小的索引
        clusterChanged=not(result_set.iloc[:,-1]==result_set.iloc[:,-2]).all()#看一下第一列和第二列是否相同 一直迭代
        if clusterChanged:
            cent_df=result_set.groupby(n+1).mean()#对点求均值
            centroid=cent_df.iloc[:,:n-1].values#当前质心更新
            result_set.iloc[:,-1]=result_set.iloc[:,-2]#将最后一列更新为倒数第二列
    return centroid,result_set
```

findr(clusterAssment,k)：抓到每个簇最大的距离作为半径
```
def findr(clusterAssment,k):
    list_r=[]
    for j in range(k):
        dis = 0
        for i in range(len(clusterAssment)):
            if j==(clusterAssment.iloc[i,4]) and dis<(clusterAssment.iloc[i,3]):
                dis=(clusterAssment.iloc[i,3])
        list_r.append(dis)
    return list_r
```

showCluster(k, test_cent, test_cluster,lllan)：绘制所有的样本，可视化结果
```
def showCluster(k, test_cent, test_cluster,lllan):
    # 绘制所有的样本
    plt.scatter(test_cluster.iloc[:, 0], test_cluster.iloc[:, 1], c=test_cluster.iloc[:, -1])

    # 绘制质心
    plt.scatter(test_cent[:, 0], test_cent[:, 1], color='red', marker='X', s=100)

    if(lllan==0):
        r_find = findr(test_cluster, k)  # 得到半径
        for i in range(k):
            theta = np.arange(0, 2 * np.pi, 0.01)
            x = test_cent[i, 0] + r_find[i] * np.cos(theta)
            y = test_cent[i, 1] + r_find[i] * np.sin(theta)
            plt.plot(x, y, r_find[i])
            plt.axis('equal')
            plt.axis('scaled')
    plt.show()
```

---

### 调用的函数库

pd.read_table()：读取txt文件，即读取之前实验二中的z-score.txt

np.mat()：新建矩阵

np.linalg.eig()：计算方差矩阵的特征值和右特征向量

np.argsort():从小到大排序，对特征值排序

plt.scatter()：绘制散点图

plt.show()：显示图

np.random.uniform(data_min, data_max, (k, n-1))：data_min之间data_max，生成k行n-1列的数

pd.concat()：连接两个DataFrame

---

### 难题与解决

1.实验三开始时，需要对z-score的数据进行降维，因为在实验起始画散点图的时候才发现10门成绩画不了散点图，上网搜索无果。后来询问同学得知数据降维这个知识，于是了解PCA降维的相关知识，将txt文件的10门成绩数据成功降维到2维，可视化散点图。

2.K-Means算法之前需要计算好点到簇心的欧氏距离，并且起始需要随机去簇心。通过np.random.uniform()这个函数库初始化随机簇心。迭代的过程中由于忘记修改clusterChanged的布尔值，导致一直迭代，无法得到结果。

3.可视化图的时候，本来可以直接显示结果，但是题目2需要画出聚类的半径，于是设置了可视化结果的函数，用里面的参数判断是否需要画圆，圆的画法使用参数方程画出圆的轨迹，而簇心到点就在K-Means返回的函数值的第4列（或者3，0、1、2、3列），顺序第4。设置一个函数findr()得到每个类的最大欧氏距离作为半径，把圆画出来。

---

### 总结

实验三作为理论课程的最后一个实验，针对K-Means算法进行的实验。对算法的了解主要通过在实验中，如果只看K-Means算法的算法定义很难去了解这个算法具体怎么操作的。通过自己实验的过程中结合对算法的知识，一步一步的实现，不仅巩固了对K-Means算法的了解，并且对其印象加深了不少。整个步骤的了解，帮助我以后在机器学习的相关方面的知识进行了补充。同时，对可视化的相关知识也增加了不少，毕竟圆的画法还是蛮讲究的，需要参数方程或者标准方程来实现，通过这个实验让我了解了不少相关知识，非常感谢！

