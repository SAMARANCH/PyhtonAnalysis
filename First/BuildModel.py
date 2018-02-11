import pandas as pd
import numpy as np
import sklearn.cluster as sk

TestData = pd.DataFrame(np.random.randn(100,3),columns=list('abc'))
#choose K-Mean()
def computer(Data):
  Model = sk.KMeans(n_clusters = 3,n_jobs=4,max_iter=500)
  Model.fit(TestData)
  return Model
if __name__=="__main__":
    fixModel = computer(TestData)
    r = list(TestData.columns)
    r.append('type')
    print  r
    print pd.DataFrame(fixModel.cluster_centers_,index=pd.Series(fixModel.labels_).value_counts().index)
