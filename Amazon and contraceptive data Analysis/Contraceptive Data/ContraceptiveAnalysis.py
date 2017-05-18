import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn import datasets
from sklearn import metrics
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier

#Reading of dataset
data = pd.read_csv('Contraceptive Dataset.txt', sep=",", names = ["Wife's age", "Wife's education", "Husband's education", "Number of children ever born",
                                                                  "Wife's religion","Wife's now working?","Husband's occupation","Standard-of-living index",
                                                                  "Media exposure","Contraceptive method used"])
#Prerocessing and feature selection
data=data.dropna()# dropping rows that have null values
#Undersampling of data
sample_size = len(data[data["Contraceptive method used"] == 2]) # get the total count of low-frequency group
unHealthy_indices = data[data["Contraceptive method used"] == 1].index
unHealthy_sample = data.loc[10]
n_attributes= len(unHealthy_sample)
healthy_indices = data[data["Contraceptive method used"] == 3].index
random_indices = np.random.choice(healthy_indices, sample_size, replace=False) # use the low-frequency group count to randomly sample from high-frequency group
healthy_sample = data.loc[random_indices]
healthy_indices1 = data[data["Contraceptive method used"] == 2].index
random_indices1 = np.random.choice(healthy_indices1, sample_size, replace=False) # use the low-frequency group count to randomly sample from high-frequency group
healthy_sample1 = data.loc[random_indices1]
healthy_indices2 = data[data["Contraceptive method used"] == 1].index
random_indices2 = np.random.choice(healthy_indices2, sample_size, replace=False) # use the low-frequency group count to randomly sample from high-frequency group
healthy_sample2 = data.loc[random_indices2]
 
# Merging all the low-frequency group sample and the new (randomly selected) high-frequency sample together
merged_sample = pd.concat([healthy_sample2,healthy_sample1, healthy_sample], ignore_index=True)
merged_sample=merged_sample.reindex(np.random.permutation(merged_sample.index))

#Class label and feature seperated
y=merged_sample["Contraceptive method used"]
merged_sample=merged_sample.drop("Contraceptive method used",1)

#Features are normalised
robust_scaler = RobustScaler()
X=robust_scaler.fit_transform(merged_sample)

n_features= len(merged_sample.loc[10])
train_samples = len(merged_sample)-100  # Samples used for training the models
X_train = X[:train_samples]
X_test = X[train_samples:]
#print X_test
y_train = y[:train_samples]
#print y_train
y_test = y[train_samples:]
#print y_test

# Build a forest and compute the feature importances
forest = ExtraTreesClassifier(n_estimators=250,
                              random_state=0)

forest.fit(X, y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()

#Deleting features on the basis of results obtained from feature importance of the forest
merged_sample=merged_sample.drop("Media exposure",1)
merged_sample=merged_sample.drop("Wife's religion",1)
merged_sample=merged_sample.drop("Wife's now working?",1)

X=robust_scaler.fit_transform(merged_sample)

train_samples = len(merged_sample)-100  # Samples used for training the models
X_train = X[:train_samples]
X_test = X[train_samples:]
#print X_test
y_train = y[:train_samples]
#print y_train
y_test = y[train_samples:]

#Decision tree implementation
depth=[]
accuracy=[]
model = DecisionTreeClassifier()
for i in range(1,30):
    model = DecisionTreeClassifier(max_depth=i)
    model.fit(X_train, y_train)
    expected = y_test
    predicted = model.predict(X_test)
    # summarize the fit of the model
    if(i==5):
        print(model)
        print(metrics.classification_report(expected, predicted))
        print(metrics.confusion_matrix(expected, predicted))
        print("accuracy :",metrics.accuracy_score(expected, predicted))
    #fpr, tpr, thresholds = metrics.roc_curve(expected, predicted, pos_label=2)
    #print("area under curve",metrics.auc(fpr, tpr))
    #print(roc_auc_score(expected, predicted))
    depth.append(i)
    score=metrics.accuracy_score(expected, predicted)
    accuracy.append(score*100)
    
depth=np.asarray(depth)
accuracy=np.asarray(accuracy)


plt.plot(depth,accuracy,'--')
plt.xlabel('Depth')
plt.ylabel('Accuracy')
plt.title('Depth VS accuracy for decision trees')
plt.show()

#Logistic Regression implementation
model = LogisticRegression(multi_class='ovr')
model.fit(X_train, y_train)
print(model)
# make predictions
expected = y_test
predicted = model.predict(X_test)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print("accuracy: ",metrics.accuracy_score(expected, predicted))

#AdaBoost Classifier implementation with Logistic Regression as base model
model = AdaBoostClassifier(base_estimator=model)
model.fit(X_train, y_train)
print(model)
# make predictions
expected = y_test
predicted = model.predict(X_test)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print("accuracy :",metrics.accuracy_score(expected, predicted))
#print(model.score(X, y))

#KNeighbors Classifier implementation
accuracy1=[]
kvalues=[]
for i in range(1,len(X_train)):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, y_train)
    #print(model)
    # make predictions
    expected = y_test
    predicted = model.predict(X_test)
    # summarize the fit of the model
    if(i==80):
        print(model)
        print(metrics.classification_report(expected, predicted))
        print(metrics.confusion_matrix(expected, predicted))
        print("accuracy",metrics.accuracy_score(expected, predicted))
        print(model.score(X, y))
    score=metrics.accuracy_score(expected, predicted)
    #score=metrics.roc_curve(expected, predicted)
    accuracy1.append(score)
    kvalues.append(i)

plt.plot(kvalues,accuracy1,'--')
plt.xlabel('Different values of k')
plt.ylabel('Accuracy')
plt.title('K values VS accuracy for k nearest neighbours')
plt.show()

#SVM Classifier implementation
accuracy2=[]
cvalues=[0.1,2,10,13,18,22,45,50,56]
for i in cvalues:
    model = SVC(C=i)
    model.fit(X_train, y_train)
    
    # make predictions
    expected = y_test
    predicted = model.predict(X_test)
    # summarize the fit of the model
    if(i==22):
        print(model)
        print(metrics.classification_report(expected, predicted))
        print(metrics.confusion_matrix(expected, predicted))
        print("accuracy :",metrics.accuracy_score(expected, predicted))
    score=metrics.accuracy_score(expected, predicted)
    accuracy2.append(score)
    
plt.plot(cvalues,accuracy2,'--')
plt.xlabel('Different values of c')
plt.ylabel('Accuracy')
plt.title('C values VS accuracy for SVM')
plt.show()

#Plotting ROC curve for SVM
y = label_binarize(y, classes=[1, 2,3])
n_classes = y.shape[1]

# shuffle and split training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5,
                                                    random_state=0)

# Learn to predict each class against the other
classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True,
                                 random_state=0))
y_score = classifier.fit(X_train, y_train).decision_function(X_test)

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
plt.figure()
lw = 2
plt.plot(fpr[2], tpr[2], color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[2])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic for SVM')
plt.legend(loc="lower right")
plt.show()

#Plotting ROC curve for DecisionTreeClassifier
y = label_binarize(y, classes=[1, 2,3])
n_classes = y.shape[1]

# shuffle and split training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5,
                                                    random_state=0)

# Learn to predict each class against the other
classifier = OneVsRestClassifier(DecisionTreeClassifier(max_depth=5))
y_score = classifier.fit(X_train, y_train).predict(X_test)

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
plt.figure()
lw = 2
plt.plot(fpr[2], tpr[2], color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[2])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic for decision tree')
plt.legend(loc="lower right")
plt.show()

#Plotting ROC curve for LogisticRegression
y = label_binarize(y, classes=[1, 2,3])
n_classes = y.shape[1]

# shuffle and split training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5,
                                                    random_state=0)

# Learn to predict each class against the other
classifier = OneVsRestClassifier(LogisticRegression())
y_score = classifier.fit(X_train, y_train).predict(X_test)

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
plt.figure()
lw = 2
plt.plot(fpr[2], tpr[2], color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[2])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic for Logistic Regression')
plt.legend(loc="lower right")
plt.show()
