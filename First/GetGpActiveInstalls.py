# -*-coding:gbk-*-
import pandas as pd
import numpy as np
import  openpyxl
import MyDataAnalysisModule

ProjectExcel = MyDataAnalysisModule.openExcel('./SoundRecorderGpDevices.xlsx','Sheet1')
ProjectExcel.drop_duplicates(subset='Device',inplace=True)
ProjectFilter = ProjectExcel.loc[:,('Device','Active Device Installs')]
ProjectFilter.dropna(how='any',inplace=True)
# MyIndex = pd.Index(np.arange(len(ProjectFilter)),name='Num')
# ProjectFilterNew = pd.DataFrame(ProjectFilter,index=MyIndex)
ProjectFilter.to_excel('./SoundRecorderGpDevicesAfter.xlsx',sheet_name='Sheet1')