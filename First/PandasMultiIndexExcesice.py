import pandas as pd
import numpy as np

# Exercise 01- Groupby
# drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
# col = drinks.columns
# result = drinks.groupby('continent').mean()
# result.sort_values('')

# Exercise 02 - Zip Function
a = [1,2,3]
b = [4,5,6]
ZipAr1  = zip(a,b) #zip
print ZipAr1
Ar = np.random.randn(3,4)
print Ar
ZipAr2 = zip(*Ar)   # *unzip
print zip(*ZipAr2)

# Exercise 03 - Create MultiIndex
Arindex = [ ['bar','bar','baz','baz','foo','foo','qux','qux'],
               ['one','two','one','two','one','two','one','two']]
tuples = zip(*Arindex)
indextuple = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print indextuple
print 'tuple index size',len(indextuple)
s1 = pd.Series(np.random.randn(8), index=indextuple)
indexarray = pd.MultiIndex.from_arrays(Arindex, names=['first', 'second'])
s2 = pd.Series(np.random.randn(8), index=indexarray)
s3 = pd.Series(np.random.randn(8), index=Arindex)
s4 = pd.Series(np.random.randn(8), index=tuples)

# Exercise 04 - Slice
print 'bar-one value',s2['bar','one']
print 'bar value\n',s2['bar']
print 'bar and baz value ',s2[['bar','baz']]
print s2[::1]
print s2[::3]

# MultiIndex

def MyFunction(pre,n):
    return ["%s%s" % (pre, i) for i in range(n)]
# print  MyFunction('A',4)
miindex = pd.MultiIndex.from_product([MyFunction('A',4),
                                      MyFunction('B',3),
                                      MyFunction('C',4),
                                      MyFunction('D',2)],names=['A1','B1','C1','D1'])
micolumns = pd.MultiIndex.from_tuples([('a','foo'),('a','bar'),
                                       ('b','foo'),('b','bah')],
                                          names=['lvl0', 'lvl1'])
dfmi = pd.DataFrame(np.arange(len(miindex)*len(micolumns)).reshape((len(miindex),len(micolumns))),
                              index=miindex,
                              columns=micolumns)
print dfmi
#index
# print miindex

#Recommand
#Method1 IndexSlice ,Begin
# idx = pd.IndexSlice
# print dfmi.loc[idx['A1','B0':'B1',('C1','C3')],idx['a','bar':'foo']]
# #Method1 IndexSlice ,End

#Method2 Slice() ,Begin
# print 'slice() begin'
# print dfmi.loc[(slice(None),slice('B0','B1')),:]
# #Method2 Slice ,End

#Slice by axis
# print dfmi.loc(axis=0)[['A1','A2'],:,:,:]

#Sort
#default sort by axis 0, level None
# dfmi.sort_index()

# Sort by Level 1
# print 'sort level1'
# change = dfmi.sort_index(level='lvl1',axis=1)
# print dfmi
# print change

#GroupBy
groupDf = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

groupDf1= groupDf.groupby('A')
print '-----------:',groupDf1.head(5)