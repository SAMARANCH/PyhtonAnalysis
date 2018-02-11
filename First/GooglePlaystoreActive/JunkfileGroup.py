# -*-coding:gbk-*-
import pandas as pd
import numpy as np
import  openpyxl

ProjectExcel = pd.read_excel('./ExcelFile/Junkfilechapin.xlsx','Sheet1')
group1= ProjectExcel.groupby(['dt','ad_area','ad_action'])['_col3'].sum()
group1.to_excel('./ExcelFile/Junkfilechapinafter.xlsx',sheet_name='Sheet1')
