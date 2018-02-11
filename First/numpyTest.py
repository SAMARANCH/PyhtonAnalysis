import numpy as np
import pandas as pd
import os
import sklearn as sk
import scipy as sp


MyFile = open('test.txt')
lines = MyFile.readlines()
matrix = np.zeros([5,5])
for index in range(len(lines)):
   data = lines[index].strip().split(r',')
   matrix[index,0:len(data)] = data[:]
print matrix

comment_string = '#....... Section 3.2.1 Issue #32 .......2'
modifyString = comment_string.strip('.#! ')
print modifyString
print  os.listdir(os.getcwd())
testFilename = os.getcwd()+os.sep+os.listdir(os.getcwd())[0]
print  testFilename
print os.path.exists(testFilename)

# sk.datasets.fetch_20newsgroups
# news = sk.datasets.fetch_20newsgroups(subset='all')
# print  news
list1 = range(0,5)
list2 = range(6,11)
listmerge = list1.extend(list2)
print list1

myArray = np.random.randn(3,500)
line1 = myArray[0]
logArray = np.log(np.absolute(myArray))
print myArray
print line1
print pd.cut(line1,4,labels=list('abcd'),retbins=True)
listtest = list('abcdefg')
print listtest[3]
print listtest[3:5]
print listtest[:5]
print listtest[3:]
print listtest[::2]
print listtest[::-1]
print listtest[-5:-2]
for key ,value in {3:5}.items():
   print key
   print value

x =1
y=2
min=x if x<y else y
print min

bin =10
boundary = [float(i)/bin for i in range(bin+1)]
TestDateframe = (pd.DataFrame(myArray)).T
print TestDateframe
w = TestDateframe[0].describe(percentiles = boundary).iloc[4:4+bin+1]
NewDataFrame = pd.DataFrame(TestDateframe[[0]].values,columns=['c1'],dtype=float)
d2 = pd.cut(NewDataFrame['c1'],w,labels=range(bin))
NewDataFrame['c2']=d2
print NewDataFrame