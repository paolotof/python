# import and merge data
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

# create dummy variables
predvar= data_clean[['longitude','latitude',
    'extraction_type_group', 'quality_group', 'quantity',
    'waterpoint_type', 'construction_year']]
cols2transform = [name for name in predvar.columns if
    predvar[name].dtype == 'object']
predValsDummies = pd.concat([pd.get_dummies(predvar[col]) for col in cols2transform], axis=1)
predValsDummies = pd.concat([predValsDummies, predvar.drop(cols2transform, axis = 1)], axis = 1)
predvar = predValsDummies
predvar.describe()

# standardize clustering variables to have mean=0 and sd=1
clustervar = predvar.copy()
from sklearn import preprocessing
for column in clustervar.columns:
    clustervar[column] = preprocessing.scale(clustervar[column].astype('float64'))

# onvert the class labels into numbers
from sklearn.preprocessing import LabelEncoder
y = data_clean['status_group'].values
enc = LabelEncoder()
label_encoder = enc.fit(y)
y = label_encoder.transform(y) + 1
label_dict = {1: 'functional', 2: 'non functional', 3: 'functional needs repair'}

# split training and test data
from sklearn.cross_validation import train_test_split
clus_train, clus_test, targetTrain, targetTest = train_test_split(clustervar, y, 
                                                              test_size=.3, 
                                                              random_state=03022017)

# k-means cluster analysis for 1-25 clusters                                                           
from sklearn.cluster import KMeans
import numpy as np

clusters = range(1,25)
clustersM = [KMeans(n_clusters = k).fit(clus_train) for k in clusters]
centroids = [k.cluster_centers_ for k in clustersM]
from scipy.spatial.distance import cdist
D_k = [cdist(clus_train, cent, 'euclidean') for cent in centroids]
dist = [np.min(D,axis=1) for D in D_k]
avgWithinSS = [sum(d)/clus_train.shape[0] for d in dist]

"""
Plot average distance from observations from the cluster centroid
to use the Elbow Method to identify number of clusters to choose
"""
import matplotlib.pylab as plt
plt.plot(clusters, avgWithinSS)
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Average within-cluster sum of squares')
plt.title('Selecting k with the Elbow Method')
plt.show()

model3=KMeans(n_clusters=3)
model3.fit(clus_train)
clusassign=model3.predict(clus_train)

clusterLabels = model3.labels_ + 1

import sklearn.metrics
sklearn.metrics.confusion_matrix(targetTrain, clusterLabels)
sklearn.metrics.accuracy_score(targetTrain, clusterLabels)

# PCA:
from sklearn.decomposition import PCA
pca_2 = PCA(n_components=2)
pca = pca_2.fit(clus_train).transform(clus_train)
pca_2.explained_variance_ratio_
# plot PCA
targetNames = np.unique(train_labels.status_group)
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
colors = ['navy', 'turquoise', 'darkorange']
lw = 2
for color, i, target_name in zip(colors, [0, 1, 2], targetNames):
    ax1.scatter(pca[model3.labels_ == i, 0], 
								pca[model3.labels_ == i, 1], 
								color=color, alpha=.7, lw=lw,
                label=target_name)

ax1.set_xlabel('PCA 1')
ax1.set_ylabel('PCA 2')
ax1.set_title('PCA for 3 Clusters')
ax1.legend(loc='best', shadow=False, scatterpoints=1)
# LDA:
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
sklearn_lda = LDA(n_components=2)
for color, i, target_name in zip(colors, [0, 1, 2], targetNames):
    ax2.scatter(lda[model3.labels_ == i, 0], 
								lda[model3.labels_ == i, 1], 
								alpha = .7, 
								color = color,
                label = target_name
                )

ax2.set_xlabel('LDA1')
ax2.set_ylabel('LDA2')
ax2.set_title('LDA for 3 Clusters')
ax2.legend(loc='best', shadow=False, scatterpoints=1)
plt.show()
