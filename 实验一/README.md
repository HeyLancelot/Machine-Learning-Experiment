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

findnan()：将C1-C9课程中存在nan类型转换成0

get_avg(datag,i)：计算数值的均值，并返回

#### machine study1 answer1.py

xiefangcha(j)：计算协方差，并返回

---

### 调用的函数库

pd.read_excel()：读取xlsx文件

to_csv()：保存csv文件

pd.read_csv()：读取csv文件

pd.concat()：连接两个DataFrame

drop_duplicates()：删除重复值

math.isnan():判断是否是nan类型

---
