# -*-coding:gbk-*-
import pandas as pd
import numpy as np
import  openpyxl
import First.MyDataAnalysisModule

ProjectExcelAFTER =  pd.read_excel('./ExcelFile/SoundRecorderMAU.xlsx','Sheet1')
ProjectExcelAFTER.head(60).describe().to_excel('./ExcelFile/SoundRecorderMAUInfo.xlsx',sheet_name='Sheet1')