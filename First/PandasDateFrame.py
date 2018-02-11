import pandas as pd
import numpy as np

Df = pd.DataFrame(np.random.randn(3,4),index=['one','two','three'],columns=['c1','c2','c3','c4'])
BoolDf = Df>0
print Df
print Df.loc['one',['c1','c2']]
print Df.loc[['one']]
print Df.iat[1,1]
print Df.at['two','c2']
## get Entire Row
#method1,return DataFrame
print Df[0:1]
#method2 ,return DataFrame
print Df[:'one']
#method3 , return DataFrame ,Series
print Df.loc['one']
print Df.loc[['one','two']]
print Df.loc['one':'two']
print Df
print 'boolean test:',Df.loc[Df['c1']>0]
print '------------------------------'
#method4 , return DataFrame
print Df.head(1)
#mehtod5
print Df.iloc[[2]]
print '----------------------------------------------------'
##get Entire Column
# Method1,returen Series
print Df['c1']
print Df[['c1','c3']]
#method2
print Df.loc[:,'c1':'c3']
print Df.loc[:,['c1','c3']]
#method3
print Df.iloc[:,[1,2]]
print Df.iloc[:,1:2]
print Df.iloc[0]
print '----------------------------------------------------'
## insert number
Df.insert(2,'insert',[25,0,0])
print Df
print '----------------------------------------------------'
# for index ,dataseries in Df.iterrows():
#     print index
#     print dataseriest
Df2 = pd.DataFrame(np.random.randn(6,5))
print Df2
# print Df2.lookup(Df2.index,Df2.columns)
print  Df2
print np.abs(Df2)>1
print len(Df2)

#Value
DfNparray = Df.as_matrix()
print Df.values
print Df.shape

#Iterator
for Col , narray in Df.iteritems():
  print  narray

#lookup
Df5 = pd.DataFrame(np.random.randn(3,3),index=['one','two','three'],columns=['c1','c2','c3'])
print Df5
print Df5.lookup(['one','two'],['c1','c2'])
Df5Info = Df5.describe()
print Df5Info.index
print Df5Info.columns
print Df5Info.loc[['25%','75%'],:]


list1 = [1,5,7,9,13]
list2 = [2,5,8,13,17]

meanlist1 = sum(list1)/len(list1)
meanlist2 = sum(list2)/len(list2)
meansum1 = map(lambda x : x-meanlist1,list1)
meansum1Square = map(lambda x : (x-meanlist1)**2,list1)
meansum2 = map(lambda x : x-meanlist2,list2)
meansum2Square = map(lambda x : (x-meanlist2)**2,list2)
meanMerge = sum(map(lambda x,y : x*y , meansum1,meansum2))
SquareMerge = (sum(meansum1Square)*sum(meansum2Square))**0.5
print  meanMerge/SquareMerge
