import os
locationFiles = (
    "%s/Dropbox/data/DrivenData/pumpItUp/"%(os.environ['HOME'])
)
filename = "trainValues.csv"
import pandas as pd
train_values = pd.read_csv("%s%s"%(locationFiles, filename),
    header = 0)

filename = "trainLabels.csv"
train_labels = pd.read_csv("%s%s"%(locationFiles, filename),
    header = 0)

trainVals = pd.merge(train_values, train_labels, how = 'left',
    left_on = 'id', right_on = 'id')

# variables as choosen by the DataCamp tutorial
predVals = trainVals[['longitude','latitude',
    'extraction_type_group', 'quality_group', 'quantity',
    'waterpoint_type', 'construction_year']]
targets = trainVals.status_group

# remove categorical variables, they give error when fitting the 
# tree since dummy variables should be used instead.
cols2transform = [name for name in predVals.columns if
    predVals[name].dtype == 'object']

predValsDummies = predVals.drop(cols2transform, axis = 1)
print(predValsDummies.shape)

from sklearn.cross_validation import train_test_split
pred_train, pred_test, tar_train, tar_test = train_test_split(
    predValsDummies, targets, test_size=.4)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import sklearn.metrics

classifier = DecisionTreeClassifier()
classifier = classifier.fit(pred_train, tar_train)
predictions = classifier.predict(pred_test)

print sklearn.metrics.accuracy_score(tar_test, predictions)
#0.6449915824915825

print sklearn.metrics.confusion_matrix(tar_test, predictions)
#array([[9262,  717, 2890],
       #[ 847,  487,  408],
       #[3154,  419, 5576]])

print "functional probability %f"%(9262.0 / (9262.0 +  717 +  2890))

print "functional probability %f"%(487.0 /(847.0 + 487 + 408))

print "functional probability %f"%(5576.0 / (3154 +  419 + 5576.0))

#Displaying the decision tree
# NOTE: do not run! None of these is actually a good option! 
# It takes very long to make a plot

from sklearn import tree
with open("pumpItUp.dot", 'w') as f:
	f = tree.export_graphviz(classifier, out_file=f)

os.unlink('pumpItUp.dot')

import pydotplus 
dot_data = tree.export_graphviz(classifier, out_file=None)
# or, for more aesthetic options
dot_data = tree.export_graphviz(classifier, out_file=None, 
                         feature_names=pred_train.feature_names,  
                         class_names=trainVals.status_group,  
                         filled=True, rounded=True,  
                         special_characters=True)  

graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_pdf("pumpItUp.pdf") 
