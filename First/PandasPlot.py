import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as sty


TestDataFrame = pd.DataFrame(np.random.randn(10,10),index=pd.date_range('1/1/2000', periods=10),columns=list('ABCDEFGHIJ'))
TestDataFrame.plot(kind='bar',figsize=(10,10),sharex = False)
plt.subplots_adjust( hspace=0.5)
plt.show()

df_box = pd.DataFrame(np.random.randn(50, 2))
df_box['g'] = np.random.choice(['A', 'B'], size=50)
df_box.loc[df_box['g'] == 'B', 1] += 3

# df2 = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
# # df2['b'] = df2['b'] + np.arange(1000)
# df2['z'] = np.random.uniform(0, 3, 1000)
# # df2.plot.hexbin(x='a', y='b', C='z', reduce_C_function=np.max)
# df2.plot.hexbin(x='a', y='b',gridsize=25)
# plt.show()

# df3= pd.DataFrame(np.random.rand(3,4),index=['a','b','c'],columns=list('abcd'))
# data = df3['a']
# data.plot.pie()
# plt.show()



