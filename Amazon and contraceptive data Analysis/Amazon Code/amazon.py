import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
from sklearn import datasets
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn import preprocessing
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize


data = pd.read_csv("amazon_dataset.csv")
data=data.dropna()

sample_size = len(data[data["ACTION"] == 0]) # get the total count of low-frequency group
print("sample_size : ",sample_size) 

data_t = data[data["ACTION"] == 0].index
random_indices1 = np.random.choice(data_t, sample_size, replace=False) # use the low-frequency group count to randomly sample from high-frequency group
data_t1 = data.loc[random_indices1]

data_te = data[data["ACTION"] == 1].index
random_indices2 = np.random.choice(data_te, sample_size, replace=False) # use the low-frequency group count to randomly sample from high-frequency group
data_t2 = data.loc[random_indices2]
 
# Merging all the low-frequency group sample and the new (randomly selected) high-frequency sample together
merged_sample = pd.concat([data_t2,data_t1], ignore_index=True)
print len(merged_sample)
merged_sample = shuffle(merged_sample)
target = merged_sample['ACTION']
merged = merged_sample.drop('ACTION',1)
merged=merged.drop('RESOURCE',1)
#merged=merged.drop('MGR_ID',1)
#merged=merged.drop('ROLE_FAMILY_DESC',1)
merged = preprocessing.normalize(merged)

dataSplit = int(len(merged) * .8)
print dataSplit
train = merged[:dataSplit]
test = merged[dataSplit:]
target_train = target[:dataSplit]
target_test = target[dataSplit:]


# Build a forest and compute the feature importances
forest = ExtraTreesClassifier(n_estimators=250,
                              random_state=0)

forest.fit(train, target_train)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(8):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

#SVM model

model = SVC()
model.fit(train,target_train)
print(model)
# make predictions
expected = target_test
predicted = model.predict(test)

#print ('SVM',accuracy)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print("accuracy SVM",metrics.accuracy_score(expected, predicted)*100)

fpr,tpr,threshold=roc_curve(expected,predicted)
roc_auc=auc(fpr,tpr)
fig,ax=plt.subplots()
ax.plot(fpr,tpr,'b',label='AUC = %0.2f'% roc_auc)
ax.legend(loc='lower right')
ax.plot([0,1],[0,1],'r--')
ax.set_xlabel('True Positive Rate')
ax.set_ylabel('False Positive Rate')
plt.show()

# Logistic Regression model

model = LogisticRegression()
model.fit(train,target_train)
print(model)
# make predictions
expected = target_test
predicted = model.predict(test)
#accuracy=(metrics.accuracy_score(test,target_test))*100
#print ('Logistic Regression',accuracy)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print("accuracy logistic",metrics.accuracy_score(expected, predicted)*100)

fpr,tpr,threshold=roc_curve(expected,predicted)
roc_auc=auc(fpr,tpr)
fig,ax=plt.subplots()
ax.plot(fpr,tpr,'b',label='AUC = %0.2f'% roc_auc)
ax.legend(loc='lower right')
ax.plot([0,1],[0,1],'r--')
ax.set_xlabel('True Positive Rate')
ax.set_ylabel('False Positive Rate')
plt.show()

#Decision tree classifier

depth=[]
accuracy=[]
model = DecisionTreeClassifier()
for i in range(1,30):
    model = DecisionTreeClassifier(max_depth=i)
    model.fit(train,target_train)
    #print(model)
    expected = target_test
    predicted = model.predict(test)
    score=metrics.accuracy_score(expected, predicted)
    accuracy.append(score*100)
    depth.append(i)
    
# summarize the fit of the model
max_accuracy=max(accuracy)
max_index = accuracy.index(max_accuracy)
print('Max index',max_index)
depth=np.asarray(depth)
accuracy=np.asarray(accuracy)

model = DecisionTreeClassifier(max_depth=max_index)
model.fit(train,target_train)

expected = target_test
predicted = model.predict(test)
score=metrics.accuracy_score(expected, predicted)
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print("Decision Tree",metrics.accuracy_score(expected, predicted)*100)

plt.plot(depth,accuracy,'--')
plt.xlabel('depth')
plt.ylabel('accuracy')
plt.show()

fpr,tpr,threshold=roc_curve(expected,predicted)
roc_auc=auc(fpr,tpr)
fig,ax=plt.subplots()
ax.plot(fpr,tpr,'b',label='AUC = %0.2f'% roc_auc)
ax.legend(loc='lower right')
ax.plot([0,1],[0,1],'r--')
ax.set_xlabel('True Positive Rate')
ax.set_ylabel('False Positive Rate')
plt.show()

#Random Forest Classifier

model = RandomForestClassifier()
model.fit(train,target_train)
print(model)
# make predictions
expected = target_test
predicted = model.predict(test)
# summarize the fit of the model
#accuracy=(metrics.accuracy_score(test,target_test))*100
#print ('RandomForest',accuracy)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print("accuracy randomforest",metrics.accuracy_score(expected, predicted)*100)

fpr,tpr,threshold=roc_curve(expected,predicted)
roc_auc=auc(fpr,tpr)
fig,ax=plt.subplots()
ax.plot(fpr,tpr,'b',label='AUC = %0.2f'% roc_auc)
ax.legend(loc='lower right')
ax.plot([0,1],[0,1],'r--')
ax.set_xlabel('True Positive Rate')
ax.set_ylabel('False Positive Rate')
plt.show()

#Ensemble Bagging

model = BaggingClassifier()
model.fit(train,target_train)
print(model)
# make predictions
expected = target_test
predicted = model.predict(test)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print("Bagging",metrics.accuracy_score(expected, predicted)*100)

fpr,tpr,threshold=roc_curve(expected,predicted)
roc_auc=auc(fpr,tpr)
fig,ax=plt.subplots()
ax.plot(fpr,tpr,'b',label='AUC = %0.2f'% roc_auc)
ax.legend(loc='lower right')
ax.plot([0,1],[0,1],'r--')
ax.set_xlabel('True Positive Rate')
ax.set_ylabel('False Positive Rate')
plt.show()

#k-Nearest Neighbour

accuracy1=[]
kvalues=[]
for i in range(1,len(train)):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(train, target_train)
    #print(model)
    # make predictions
    expected = target_test
    predicted = model.predict(test)
    # summarize the fit of the model
    #print(metrics.classification_report(expected, predicted))
    #print(metrics.confusion_matrix(expected, predicted))
    #print("accuracy",metrics.accuracy_score(expected, predicted))
    #print(model.score(X, y))
    score1=metrics.accuracy_score(expected, predicted)
    accuracy1.append(score1)
    kvalues.append(i)

plt.plot(kvalues,accuracy1,'--')
plt.xlabel('different values of k')
plt.ylabel('accuracy')
plt.show()



