# -*- codeing = utf-8 -*-
# @Time: 2020/12/27 17:01
# @Author: Lancelot
# @File: machine study3.py
# @Sofeware: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
#z-score 进行聚类的时候 需要降维


lance=pd.read_table('z_score.txt',header=None)
print(type(lance))
print(lance)

#编写PCA实现函数

#首先，去均值化:

dataset=lance
#计算均值


meanvals=dataset.mean(0)
print(type(meanvals))
print(meanvals)


#去均值化，均值变成0

meanremoved=dataset-meanvals
print(type(meanremoved))
print(meanremoved)


#计算协方差
covmat=np.mat(np.cov(meanremoved.astype(float),rowvar=False))
print(covmat)

#计算方差矩阵的特征值和右特征向量
eigvals,eigvects=np.linalg.eig(covmat)
print(eigvals)
#print(eigvals.shape)

#对特征值排序，.argsort()函数默认从小到大排序
eigvalind=np.argsort(eigvals)
#提取出最大的N个特征
N=2
eigvalind=eigvalind[:-(N+1):-1]#反向
print(eigvalind)

#切片
redeigvects=eigvects[:,eigvalind]
print(redeigvects)

#转换新空间
lowdatamat=np.mat(meanremoved)*redeigvects#降维后的矩阵
print(lowdatamat)



#封装函数
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



plt.scatter(lowdatamat[:,0].A.flatten(),lowdatamat[:,1].A.flatten(),marker='*',c='g')
plt.show()


# 欧氏距离计算
def distances(arrA, arrB):

    d = arrA - arrB
    s = (np.sum(np.power(d, 2), axis=1))
    dist = np.sqrt(s.tolist())
    return dist


# 为给定数据集构建一个包含K个随机质心的集合
def randCent(dataSet, k):
    n=dataSet.shape[1]#有n列
    data_min=dataSet.iloc[:,:n-1].min()#找出最小值
    data_max=dataSet.iloc[:,:n-1].max()#找出最大值
    randCent = np.random.uniform(data_min, data_max, (k, n-1))#data_min之前data_max，生成k行n-1列的数
    return randCent


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

#抓到每个簇最大的距离作为半径
def findr(clusterAssment,k):
    list_r=[]
    for j in range(k):
        dis = 0
        for i in range(len(clusterAssment)):
            if j==(clusterAssment.iloc[i,4]) and dis<(clusterAssment.iloc[i,3]):
                dis=(clusterAssment.iloc[i,3])
        list_r.append(dis)
    return list_r

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


#将刚才降维后的矩阵转换成dataframe
newdata=pd.DataFrame(lowdatamat)
#聚类
#将dataset转成array
llann=np.array(newdata)
print('newdata')
print(newdata)

ze=pd.DataFrame(np.zeros(newdata.shape[0]).reshape(-1,1))
new_data=pd.concat([newdata,ze],axis=1,ignore_index=True)

for i in range(2,6):
    test_cent, test_cluster = kMeans(new_data, i)
    showCluster(i, test_cent, test_cluster,1)


lancelot=pd.read_csv('data6.csv')
lan=pd.DataFrame(np.zeros(lancelot.shape[0]).reshape(-1,1))
new_lan=pd.concat([lancelot,lan],axis=1,ignore_index=True)
for i in range(2,4):
    test1_cent, test1_cluster = kMeans(new_lan, i)
    showCluster(i, test1_cent, test1_cluster, 0)




