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
data_clean = pd.merge(train_values, train_labels, how = 'left',
    left_on = 'id', right_on = 'id')

predvar= data_clean[['longitude','latitude',
    'extraction_type_group', 'quality_group', 'quantity',
    'waterpoint_type', 'construction_year']]
cols2transform = [name for name in predvar.columns if
    predvar[name].dtype == 'object']
predValsDummies = pd.concat([pd.get_dummies(predvar[col]) for col in cols2transform], axis=1)
predValsDummies = pd.concat([predValsDummies, predvar.drop(cols2transform, axis = 1)], axis = 1)
predvar = predValsDummies

import numpy as np
target = pd.Series(np.zeros(data_clean.shape[0]))
target[data_clean.status_group == 'functional'] = 1

predictors=predvar.copy()
from sklearn import preprocessing
for column in predictors.columns:
    predictors[column] = preprocessing.scale(predictors[column].astype('float64'))

from sklearn.cross_validation import train_test_split
pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, target, 
                                                              test_size=.3, random_state=123)
from sklearn.linear_model import LassoLarsCV
model=LassoLarsCV(cv=10, precompute=False).fit(pred_train,tar_train)

dict(zip(predictors.columns, model.coef_))
print ("%s variables of %s where removed"%(sum(model.coef_ == 0), len(model.coef_)))

sortedCoef = sorted(range(len(model.coef_)), key=lambda k: model.coef_[k])
print (predictors.columns[sortedCoef])

import matplotlib.pylab as plt
m_log_alphas = -np.log10(model.alphas_)
ax = plt.gca()
plt.plot(m_log_alphas, model.coef_path_.T)
plt.axvline(-np.log10(model.alpha_), linestyle='--', color='k',
            label='alpha CV')
plt.ylabel('Regression Coefficients')
plt.xlabel('-log(alpha)')
plt.title('Regression Coefficients Progression for Lasso Paths')
plt.show()

m_log_alphascv = -np.log10(model.cv_alphas_)
plt.figure()
plt.plot(m_log_alphascv, model.cv_mse_path_, ':')
plt.plot(m_log_alphascv, model.cv_mse_path_.mean(axis=-1), 'k',
         label='Average across the folds', linewidth=2)
plt.axvline(-np.log10(model.alpha_), linestyle='--', color='k',
            label='alpha CV')
plt.legend()
plt.xlabel('-log(alpha)')
plt.ylabel('Mean squared error')
plt.title('Mean squared error on each fold')
plt.show()         

from sklearn.metrics import mean_squared_error
train_error = mean_squared_error(tar_train, 
                                 model.predict(pred_train))
test_error = mean_squared_error(tar_test, 
                                model.predict(pred_test))
print ('training data MSE %s'%(train_error))
print ('test data MSE %s'%(test_error))

rsquared_train = model.score(pred_train,
                             tar_train)
rsquared_test=model.score(pred_test,
                          tar_test)
print ('training data R-square %s'%(rsquared_train))z
print ('test data R-square %s'%(rsquared_test))
