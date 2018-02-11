# -*-coding:gbk-*-
import pandas as pd
import numpy as np
import  openpyxl

# ProjectExcel = pd.read_excel('./ExcelFile/DataAnalysis.xlsx','Sheet1')
# ProjectExcel.drop_duplicates(subset=['GP_Device_Name','Eproject_Name'],inplace=True)
# ProjectExcel.to_excel('./ExcelFile/DataAnalysisAfter.xlsx',sheet_name='Total')
ProjectExcel = pd.read_excel('./ExcelFile/SoundRecorder01.xlsx','Sheet1')
ProjectExcel.drop_duplicates(subset='Device',inplace=True,keep='last')
ProjectExcelFilter = ProjectExcel.loc[ProjectExcel['Active Device Installs']!=0]
ProjectExcelFilter.to_excel('./ExcelFile/SoundRecorder01After.xlsx',sheet_name='Sheet1')