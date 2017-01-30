## --- Load the dataset
import os
locationFiles = (
    "%s/Dropbox/data/DrivenData/pumpItUp/"%(os.environ['HOME'])
)
import pandas as pd
filename = "trainValues.csv"
train_values = pd.read_csv("%s%s"%(locationFiles, filename),
    header = 0)
filename = "trainLabels.csv"
train_labels = pd.read_csv("%s%s"%(locationFiles, filename),
    header = 0)
AH_data = pd.merge(train_values, train_labels, how = 'left',
    left_on = 'id', right_on = 'id')
data_clean = AH_data.dropna()

data_clean.dtypes
data_clean.describe()

## --- Split into training and testing sets

predictors = data_clean[['longitude','latitude',
    'extraction_type_group', 'quality_group', 'quantity',
    'waterpoint_type', 'construction_year']]

targets = data_clean.status_group
# add dummy variables to avoid
# ValueError: could not convert string to float: communal standpipe
# when running the model
# 1 - identify categorical variables
cols2transform = [name for name in predictors.columns if
    predictors[name].dtype == 'object']
# 2 - make dummies
predValsDummies = pd.concat([pd.get_dummies(predictors[col]) for col in cols2transform], axis=1)
# 3 - attach continuous variables
predValsDummies = pd.concat([predValsDummies, predictors.drop(cols2transform, axis = 1)], axis = 1)
# overwrite old value with new one to 1) save memory, 2) keep recycling coursera code 
predictors = predValsDummies
from sklearn.cross_validation import train_test_split
pred_train, pred_test, tar_train, tar_test  = train_test_split(predictors, 
			 targets, test_size=.4)

pred_train.shape
pred_test.shape
tar_train.shape
tar_test.shape

## --- Build model on training data
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=25)
classifier=classifier.fit(pred_train,tar_train)
predictions=classifier.predict(pred_test)

import sklearn.metrics
sklearn.metrics.confusion_matrix(tar_test,predictions)
sklearn.metrics.accuracy_score(tar_test, predictions)

# fit an Extra Trees model to the data
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(pred_train,tar_train)
# display the relative importance of each attribute
print(model.feature_importances_)

importances = model.feature_importances_
import numpy as np
std = np.std([tree.feature_importances_ for tree in model.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]
print("Feature ranking:")
for f in range(pred_train.shape[1]):
    print("%d. feature %d %s (%f)" % (f + 1, indices[f], 
			 pred_train.columns[indices[f]], 
			 importances[indices[f]]))

# where does 'dry' comes from
list(data_clean['quantity'].unique())
#list(data_clean['extraction_type_group'].unique())
list(data_clean['waterpoint_type'].unique())
# Plot the features' importances of the forest
import matplotlib.pylab as plt
plt.figure()
plt.title("Six most important features")
nFeatures = 6
feats = range(nFeatures)
plt.bar(feats, importances[indices[feats]],
       color="r", yerr=std[indices[feats]], align="center")
# rotate the label names to display the whole variable name on x axis
plt.xticks(feats, pred_train.columns[indices[feats]], rotation=90) 
plt.xlim([-1, nFeatures])
plt.tight_layout() # to avoid trimming the labels on the x axis
plt.show()
    
"""
Running a different number of trees and see the effect
 of that on the accuracy of the prediction
"""
nTrees = 100
trees = np.arange(nTrees)
accuracy=np.zeros(nTrees)
for idx in range(len(trees)):
   classifier=RandomForestClassifier(n_estimators=idx + 1)
   classifier=classifier.fit(pred_train,tar_train)
   predictions=classifier.predict(pred_test)
   accuracy[idx]=sklearn.metrics.accuracy_score(tar_test, predictions)
   
import matplotlib.pylab as plt
plt.cla()
plt.plot(trees, accuracy)
plt.show()
print('%s trees give max accuracy'%(trees[accuracy == max(accuracy)][0]))

