import pandas as pd
import numpy as np
import  openpyxl

ProjectExcel = pd.read_excel('./ExcelFile/JunkfileChapin.xlsx','Sheet2')
ProjectExcel.dropna(how='any',inplace=True)
ProjectExcel.to_excel('./ExcelFile/JunkfileChapinAfter.xlsx',sheet_name='Sheet2')