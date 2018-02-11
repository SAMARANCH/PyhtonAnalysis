# -*-coding:gbk-*-
import pandas as pd
import numpy as np
import  openpyxl
import MyDataAnalysisModule

AndriodVerion = ['L','M']
ProjectExcel = MyDataAnalysisModule.openExcel('./ExcelFile/Weather_W52.xlsx','Sheet1')
ProjectExcel.drop_duplicates(subset='Device',inplace=True)
ProjectExcel.dropna(subset=['Device'],inplace=True)
# ProjectExcelFilter = ProjectExcel.loc[(ProjectExcel['Android OS'].isin(AndriodVerion)) & (ProjectExcel['BlackList']=='')]
ProjectExcel.to_excel('./ExcelFile/Weather_W52After.xlsx',sheet_name='Sheet1')