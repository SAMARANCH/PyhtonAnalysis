import  pandas as pd
import xlrd as xr

df1 = pd.DataFrame({'Key1':['a','a','b'],
                     'Key2':['one','two','one'],
                     'Data1':[1,2,3]})
df2 = pd.DataFrame({'Key1':['a','a','b','b'],
                     'Key2':['one','one','one','two'],
                    'Data2':[4,5,6,7]})
print  pd.merge(df1,df2,on='Key1')

df1 = pd.read_excel('./DataAna.xlsx','Sheet1',usecols=[0,1])
df2 = pd.read_excel('./DataAna.xlsx','Sheet2')
df3 = pd.merge(df1,df2)
print df3



