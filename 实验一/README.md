# 实验一    《多源数据集成、清洗和统计》

---

**题目**

广州大学某班有同学100人，现要从两个数据源汇总学生数据。第一个数据源在数据库中，第二个数据源在txt文件中，两个数据源课程存在缺失、冗余和不一致性，请用C/C++/Java程序实现对两个数据源的一致性合并以及每个学生样本的数值量化。

● 数据库表：ID (int),  姓名(string), 家乡(string:限定为Beijing / Guangzhou / Shenzhen / Shanghai), 性别（string:boy/girl）、身高（float:单位是cm)）、课程1成绩（float）、课程2成绩（float）、...、课程10成绩(float)、体能测试成绩（string：bad/general/good/excellent）；其中课程1-课程5为百分制，课程6-课程10为十分制。

● txt文件：ID(string：6位学号)，性别（string:male/female）、身高（string:单位是m)）、课程1成绩（string）、课程2成绩（string）、...、课程10成绩(string)、体能测试成绩（string：差/一般/良好/优秀）；其中课程1-课程5为百分制，课程6-课程10为十分制。

---

**参考**

两个数据源合并后读入内存，并统计：
1. 学生中家乡在Beijing的所有课程的平均成绩。
2. 学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。(备注：该处做了修正，课程10数据为空，更改为课程9)
3. 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
4. 学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

---

### 实验环境

编译器:PyCharm2020.2.3

作业环境:Python 3.8

---

### 实验导入的模块

import pandas as pd

import numpy as np

import csv

import glob

import math

---

### 文件说明

data1.xlsx：实验提供的数据源1

data1.csv：转换成csv格式

data2.csv：实验的数据源2

data3.csv：将两个数据源合同在一起

data4.csv：将两个数据源的数据规范化

data5.csv: 清洗数据完成的文件

machine study1.py：进行数据集成、清洗的源py

machine study1 answer1.py：回答实验题目的py文件

实验结果.jpg：存放实验一题目的回答截图

---

### 数据的规范化

两个数据源之间完成合并之后，将Gender(性别)规范为男(boy)、女(girl);将ID规范化为：“202000+i”的格式；将Height(身高)规范化为厘米单位(cm)

实验回答题目问题时，将体育成绩的四个等级bad、general、good、excellent转化为百分制对应的25、50、75、100，同理C6、C7、C8、C9由十分制转化成百分制

---

### 数据处理

将数据上面存在重复的删除，对缺失的部分通过另一个数据源中的数据补充，如果两个数据源中都无法补充，计算当前列的均值，将均值补充到缺失的值

---

### 函数说明

#### machine study1.py

xlsx_to_csv_pd()：将数据源1（xlsx格式）转化成（csv）格式

```
def xlsx_to_csv_pd():
    data_xls = pd.read_excel('data1.xlsx', index_col=0)    
    data_xls.to_csv('data1.csv', encoding='utf-8')
```

findnan()：将C1-C9课程中存在nan类型转换成0

```
def findnan():
    for i in range(len(lance)):
        for j in range(9):
            if math.isnan(lance.iloc[i, j + 5]) == True:
                lance.iloc[i, j + 5] = 0
```

get_avg(datag,i)：计算数值的均值，并返回

```
def get_avg(datag,i):
    sums=0
    for j in range(len(datag)):
        sums=sums+datag.iloc[j,i]
    avgs=sums/len(datag)
    return avgs
```

#### machine study1 answer1.py

xiefangcha(j)：计算相关系数，并返回

```
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
```

---

### 调用的函数库

pd.read_excel()：读取xlsx文件

to_csv()：保存csv文件

pd.read_csv()：读取csv文件

pd.concat()：连接两个DataFrame

drop_duplicates()：删除重复值

math.isnan():判断是否是nan类型

---

### 难题与解决

1.由于刚开始入门课程，实验中提及到的数据集成、清洗等操作对我来说都是从未掌握的新知识，于是前期花了很多时间去了解掌握数据集成清洗这些知识。

2.python语言也是我刚开始学习的编译语言，起初都是使用C++进行编译的，在了解课程知识后，明白python语言对机器学习和数据挖掘的重要性，于是开始学习这门语言，因此在实验的开始过程中，难免对有一些细节上的错误，前期在一边掌握的过程中一边学习。因此代码上有很多注释过的print()的代码，都是为了了解当前操作的数据是怎么样的、什么类型等。并且由于是在刚开始学习这门语言，函数的调用设计比较少，起始的时候几乎都是用直接运行的代码段进行运行，其实在代码中清洗里完全可以封装成函数进行操作，但那时没有注意到这一点，因此在清洗的过程中，我需要用很多段代码段进行清洗，代码上存在冗余。

3.数据上面的nan表示并不是空值，起初我认为是在C++语言中的null一样，使用if的时候用!=判断导致出错频繁，并未了解nan类型表示是什么。因此在实验过程中操作时候并未发现是什么错误，最后每一次输出的时候都print一次后，发现其有type发现可能并不是None，因此调用了math模块使用math.isnan()中采解决了nan这个问题。

4.类型导致的错误，因为实验中容易混淆里面DataFrame和list、array类型，经常出错，后来学习到iloc之后才加快了实验的进程。

---

### 总结

实验一中前期的数据清洗我认为才是实验中比较难的部分，因为在实验的过程是起始入门的阶段，还有一些小细节没有掌握到的，因此前期编译的过程中报错蛮多的。数据在清洗的过程中，首先需要去重，然后去别的数据源中找到数据中缺失的数据进行补充，同时还需要规范化数据的标准，比如单位。以及怎么处理缺失值等知识，这些都是需要自己的不断尝试在明白的，在不断报错的过程中学习了解到相关知识，因为实验你中存在很多重要的课程知识，对我知识层面的补充具有很大的帮助。特别是中间存在的nan类型，让我明白不能只看大致的代码，遇到错误就不断尝试错误代码段里面的数据，全部输出然后进行查看里面的数据。让我明白遇到错误就需要有耐心进行不断尝试，尝试过才能明白自己的错误在哪里，这次实验的知识也能为之后的实验提供很重要的作用。

---
