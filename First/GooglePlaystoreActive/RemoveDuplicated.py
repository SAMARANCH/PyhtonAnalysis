import pandas as pd
import numpy as np
import  openpyxl

def up(x):
    return  x.upper()

def  dataframesort(df):
      df1 = df.sort_values(by=['Total User Installs'],ascending=False)
      return df1
# ProjectExcel = pd.read_excel('./ExcelFile/DataAnalysis.xlsx','Sheet1')
# ProjectExcel.drop_duplicates(subset=['GP_Device_Name','Eproject_Name'],inplace=True)
# ProjectExcel.to_excel('./ExcelFile/DataAnalysisAfter.xlsx',sheet_name='Total')

# ProjectExcel = pd.read_excel('./ExcelFile/simple.xlsx','Sheet1')
# ProjectExcel['Alpha']= ProjectExcel['Alpha'].apply(lambda x:x.upper())
# print ProjectExcel

# ProjectExcel = pd.read_excel('./ExcelFile/TestData.xlsx','Sheet1')
# ProjectExcelFilter = ProjectExcel[['Date','Device','Total User Installs']]
# # print ProjectExcelFilter.head()
# # print ProjectExcelFilter.groupby('Date')[['Device','Total User Installs']].apply(lambda x:x.sort_values(by='Total User Installs',ascending=False).head(5))
# print ProjectExcelFilter.groupby('Date')[['Device','Total User Installs']].head()
# print ProjectExcelFilter

dictm = {'a':1 , 'b':2 ,'c':3}
listm = [2,3,1]
for key , value in dictm.items() :
   print key ,value

for index , value in enumerate(listm):
     print index , value

try:
    print 'my name {0}'.format('shen')
    print 'my name{a:3d},{b:3d},{c:3d}'.format(**dictm)
    print 'my name {a}'.format(a=111)
except:
    print 'aaaaa'
    raise
finally:
    print 'bbbbb'

print 'ddd {}'.format([1,2,3])