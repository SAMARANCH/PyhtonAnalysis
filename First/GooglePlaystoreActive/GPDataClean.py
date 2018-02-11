# -*-coding:gbk-*-
import pandas as pd
import numpy as np
import  openpyxl
import First.MyDataAnalysisModule

AndriodVerion = ['L','M']
ProjectExcel = pd.read_excel('./ExcelFile/WeatherMAU.xlsx','Sheet1')
ProjectExcel.drop_duplicates(subset='Device',inplace=True,keep='last')
ProjectExcel.dropna(subset=['Device'],inplace=True)
# ProjectExcelFilter = ProjectExcel.loc[(ProjectExcel['Android OS'].isin(AndriodVerion)) & (ProjectExcel['BlackList']=='')]
# ProjectExcel.to_excel('./ExcelFile/WeatherMAUAfter.xlsx',sheet_name='Sheet1')
ProjectExcelAFTER =  pd.read_excel('./ExcelFile/WeatherMAUAfter.xlsx','Sheet1')
ProjectExcelAFTER.head(60).describe().to_excel('./ExcelFile/WeatherMAUInfo.xlsx',sheet_name='Sheet1')