import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

Data = np.random.randint(0,100,20)
MyDataFrame = pd.DataFrame(Data,columns=['Value'])

def DevideGroup(Data = None,groupnum=3):
    if Data is None:
        return None
    label = ['Group{0}'.format(x+1) for x in range(groupnum)]
    return pd.cut(Data['Value'],groupnum,labels=label)

MyDataFrame['Group'] = DevideGroup(MyDataFrame)

DataInfo = MyDataFrame.groupby(by='Group').describe()
# # Fig , Axes  = mp.subplots(1,1,figsize=(10, 8))
# # DataInfo.plot(x=DataInfo.index,y='count',kind = 'barh',ax = Axes[0])
# # mp.show()
# DataInfo.categories = ['G1','G2','G3']
# print DataInfo.describe()
print DataInfo.index
print DataInfo['Value']['count']
print  DataInfo.loc[:,('Value','count')]

s_mi = pd.Series(np.arange(6) ,index=pd.MultiIndex.from_product([[0, 1], ['a', 'b', 'c']]))
print s_mi.index.isin([(0,'a'),(1,'b')])

testDataframe = pd.DataFrame(np.random.randn(3,4))
print testDataframe
filterDataframe = testDataframe.where(testDataframe<0,0)
print filterDataframe


index = pd.MultiIndex.from_tuples([('bird', 'falcon'),
                                    ('bird', 'parrot'),
                                    ('mammal', 'lion'),
                                    ('mammal', 'monkey')],
                                      names=['class', 'name'])
columns = pd.MultiIndex.from_tuples([('speed', 'max'),
                                     ('species', 'type')])
df = pd.DataFrame([(389.0, 'fly'),
                  ( 24.0, 'fly'),
                  ( 80.5, 'run'),
                   (np.nan, 'jump')],
                       index=index,
                       columns=columns)

df.reset_index(level='class',inplace=True)
print df.columns,df.index

                     A         B         C
first second
bar   one     0.895717  0.410835 -1.413681
      two     0.805244  0.813850  1.607920
baz   one    -1.206412  0.132003  1.024180
      two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
qux   one    -1.170299  1.130127  0.974466
      two    -0.226169 -1.436737 -2.006747

