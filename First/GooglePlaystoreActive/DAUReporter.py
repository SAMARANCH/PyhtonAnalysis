import pandas as pd
import numpy as np
import  openpyxl
import matplotlib.pyplot as plt

# # ProjectExcel = pd.read_csv('./ExcelFile/DailyDAU-Files-output-201801161505.csv',sep='\t')
# ProjectExcel = pd.read_excel('./ExcelFile/DAUReportor.xlsx','Sheet1')
# # # print ProjectExcel.columns
# xLabel = ProjectExcel['Version']
# yValue = ProjectExcel[ProjectExcel.columns[2]]
# Fig , Ax = plt.subplots()
# Ax.set_xticklabels(xLabel,rotation = 90 ,fontsize = 'small')
# Ax.plot(yValue)
# plt.show()

ax2 = plt.subplot(132)
ax2.scatter([1, 2],[3, 4])
ax2.set_xlim([0, 5])
ax2.set_ylim([0, 5])
plt.show()
