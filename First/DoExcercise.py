# -*- coding: utf-8 -*-
import pandas as pd
import sys

# chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep='\t')
# # prices = [float(value[1 : -1]) for value in chipo.item_price]
# # # reassign the column with the cleaned prices
# # chipo.item_price = prices
# # # make the comparison
# # chipo10 = chipo[chipo['item_price'] > 10.00]
# # print len(chipo10)
# # prices = [float(value[:]) for value in chipo.item_price]
# # print len(prices)
# # print type(chipo.item_price[1])
# # chipo.sort_values(by='item_price',ascending=False).to_excel('./ExcelFile/Weather_W52After.xlsx',sheet_name='Sheet1')
# # MyList = [x for x in chipo['item_name']]
# # MyArray = []
# # for x in  range(len(MyList)):
# #      MyArray.append(MyList[x][0])
# # print chipo[chipo['item_name']=]
#
# # drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
# # print drinks.head()
# # print drinks.iloc[: , 1:4].apply(lambda x : x.sum()).head()
# print 17.0/3.0
# print 17.0//3.0
# print 17%3
#
#
# print "my test \tmy"
# print r"my test \t"
# print [1]*3
# print '''\
# my name:
# email:
# code:
# '''
# print ('fffff'+'ddddd')
# my = 'abcdaf   '
# print my[-2:]
# print my.find('a')
# print my.find('a',1,4)
# print my.strip()
#
# # def f(a,mya=[]):
# #      mya.append(a)
# #      return mya
# # def f(a,mya=None):
# #     if mya == None:
# #         mya=[]
# #     mya.append(a)
# #     return mya
# # print f(1)
# # print  f(2)
#
# # print ('str',end='dddd')
#
# # def parrot(voltage, state='a stiff', action='voom'):
# #
# # d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# # parrot(**d)
# # -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
# #
# # args = [3, 6]
# # list(range(*args))
# # def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
# #     def cheeseshop(kind, *arguments, **keywords):
#
#
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# myli=['one','two','three','four']
# myli.pop(0)
# print  myli
# myli2 = list('myname')
# myli2.pop(0)
# print myli2
#
# mydict = {'a':1,'b':2,'c':3}
# mydict['a']=3
# print mydict
#
# {x: x**2 for x in (2, 4, 6)}
# dict(sape=4139, guido=4127, jack=4098)
#
# a = set('abracadabra')
# b = set('alacazam')
# a                                  # unique letters in a
# a - b                              # letters in a but not in b
# a | b                              # letters in a or b or both
# a & b                              # letters in both a and b
# a ^ b                              # letters in a or b but not both
#
# for k, v in knights.items():
#     for i, v in enumerate(['tic', 'tac', 'toe']):

print sys.path
print dir()
x = 10 * 3.25
y = 200 * 200
# s = 'The value of x is ' + x + ', and y is ' + y+ '...'
print repr(x).rjust(8),repr(y).rjust(2)
print'We are the {} who say "{}!"'.format('knights', 'Ni')

print('{0} and {1}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))