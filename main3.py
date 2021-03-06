# -*- coding: utf-8 -*-
"""main3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zw998_c7LE6Qs9KBrUMnr-c4--5pAtUc
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import seaborn as sns
names = ['purchase_sequence', 'style_id','article_type','gender','Revenue','Return_Reason','orders','Total Revenue','Return Value','RTO Value','RGM','Items','Return Items','RTO Items','return_q2_cogs','Return_Duration','Inv_Age','mserve','Q2_perc','CA_Q2_perc','scm_cost','GP','is_return' ]
names1 = ['purchase_sequence', 'style_id','article_type','gender','Revenue','Return_Reason','orders','Total Revenue','Return Value','RTO Value','RGM','Items','Return Items','RTO Items','return_q2_cogs','Return_Duration','Inv_Age','mserve','Q2_perc','CA_Q2_perc','scm_cost','GP' ]

RandomForestClassifier(bootstrap=True,class_weight=None,criterion='gini',max_depth=None,max_features='auto',max_leaf_nodes=None,min_impurity_decrease=0.0, min_impurity_split=None,min_samples_leaf=1, min_samples_split=2,min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=1,oob_score=False, random_state=None,verbose=0,warm_start=False)
url = "https://raw.githubusercontent.com/zeus1912/dataset/main/fdata.csv"
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
X = array[:,0:22]
y = array[:,22]

fig, axs = plt.subplots(1, 2, sharey=True)
dataframe.plot(kind='scatter', x='Return_Reason', y='is_return', ax=axs[0], figsize=(16, 2))
dataframe.plot(kind='scatter', x='orders', y='is_return', ax=axs[1],figsize=(16, 2))
##df.plot(kind='scatter', x='tpres', y='hesc', ax=axs[2])
#d#f.plot(kind='scatter', x='ppres', y='hesc', ax=axs[3])
plt.show()

