import  pandas as pd
import numpy as np
import MyDataAnalysisModule

# ProjectExcel = MyDataAnalysisModule.openExcel('./ExcelFile/Total_12_20.xlsx','Total')
# group1= ProjectExcel.groupby(['GP_Device_Name','Eproject_Name'])['FotaMAU'].sum().reset_index()
# # group1= ProjectExcel.groupby(['GP_Device_Name','Eproject_Name'])['FotaMAU'].sum()
# group1.to_excel('./ExcelFile/Total_12_20After.xlsx',sheet_name='Total')

Df1 = pd.DataFrame(np.arange(24).reshape(6,4),index=['one','two','three','three','three','three'],columns=['c1','c2','c3','c4'])

#Rolling
# print Df1['c1']
# print Df1['c1'].rolling(window=3,center=True).mean()

#Transform
# print Df1.groupby(level=0)['c1'].transform(lambda x : x-x.mean()/x.std())

# print Df1.groupby(level=0)['c1'].sum()
print Df1
# print Df1.groupby(level=0).mean()
print Df1.groupby(level=0).transform(lambda x : x-x.mean())

#Apply
print Df1.groupby(level=0).apply(lambda x : x['c1']-x['c1'].mean())
print Df1.groupby(level=0).apply(lambda x : x.describe())
print Df1.groupby(level=0).apply(lambda x : x['c1'].value_counts())

