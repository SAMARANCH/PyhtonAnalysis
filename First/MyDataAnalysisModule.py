import pandas as pd
import numpy as np
import openpyxl

#OpenExcel
def openExcel(Filename,Sheetname):
    ProjectExcel = pd.read_excel(Filename, sheet_name=Sheetname)
    return  ProjectExcel