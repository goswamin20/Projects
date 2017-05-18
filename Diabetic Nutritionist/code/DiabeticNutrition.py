#refered from scikit documentation http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html and http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
import pandas as pd
import pandas.io.sql as sql
from pandas import *
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import numpy as np
from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.metrics as sm
from matplotlib import pyplot
from sklearn.cluster import KMeans
from scipy import cluster
import MySQLdb

#Input age, gender,bloodgroup, blood sugar level, food and amount of to be consumed by the user
age=input("Enter your age:")
upper=age+5
lower=age-5
gender= raw_input("Enter your gender(F/M):")
bloodgroup= raw_input("Enter your blood group(A,B,AB,O):")
sugarlevel= float(input("Enter your blood sugar level:"))
food=raw_input("Enter your food:")
serving=float(raw_input("Enter amount of food(gms):"))

# load the dataset into pandas dataframe
dataNutrition = pd.read_csv('Nutrition Dataset.csv',usecols=["FoodName","GyclemicIndex","Energywithdietaryfibre(kJ)",
                                                             "Energywithoutdietaryfibre(kJ)","Totalfat(g)",
                                                             "Availablecarbohydrateswithsugaralcohols(g)",
                                                             "Availablecarbohydrateswithoutsugaralcohol(g)",
                                                             "Starch(g)",
                                                             "Alcohol(g)","Totalsaturatedfat(g)",
                                                             "Totalmonounsaturatedfat(g)",
                                                             "Totalpolyunsaturatedfat(g)","Totaltransfattyacids(mg)"])

#Check whether food entered by user present in the dataset
list={food}
f=dataNutrition[dataNutrition['FoodName'].isin(list)]
descision="not decided"
data=[{}]
dataf1=[]
j=0
flag=11

#if food is present in the dataset, calculations for glycemic index are done directly
if(f.size>0):
    flag=1
    netcarbs=float(f["Totalfat(g)"]+f["Availablecarbohydrateswithsugaralcohols(g)"]+f["Availablecarbohydrateswithoutsugaralcohol(g)"]
                   -f["Alcohol(g)"]-f["Starch(g)"]+f["Totalsaturatedfat(g)"]+f["Totalmonounsaturatedfat(g)"]+f["Totalpolyunsaturatedfat(g)"]
                   +f["Totaltransfattyacids(mg)"])
    GI=f["GyclemicIndex"].values
    GlycemicLoad=(float)(netcarbs*GI*serving)/10000.0
    print ("Glycemic Load:",GlycemicLoad)
    if(GlycemicLoad<10.0):
        print("Food is appropriate for consumption")
    elif(GlycemicLoad<=19.0 and sugarlevel<=100.0):
        print("Food is appropriate for consumption")
    elif(GlycemicLoad>=20.0 and GI<=55.0):
        print("If food is consumed in lesser quatity, it would be fit for consumption")
        descision = raw_input("Do you want a healthier food substitute(Y/N):")
    else:
        print("Food is inappropriate for consumption")
        descision=raw_input("Do you want a healthier food substitute(Y/N):")
#if food is not present in the dataset, user is asked to enter the nutrient values for calculation of glycemic index
else:
    flag=0
    data=[{"FoodName":food,"Energywithdietaryfibre(kJ)":float(raw_input("Enter Energywithdietaryfibre(kJ):")),
    "Energywithoutdietaryfibre(kJ)":float(raw_input("Enter Energywithoutdietaryfibre(kJ):")),
    "Moisture(g)":float(raw_input("Enter Moisture(g):")),
    "Protein(g)":float(raw_input("Enter Protein(g):")),
    "Totalfat(g)":float(raw_input("Enter Totalfat(g):")),
    "Availablecarbohydrateswithsugaralcohols(g)":float(raw_input("Enter Available carbohydrates with sugar alcohols(g):")),
    "Availablecarbohydrateswithoutsugaralcohol(g)":float(raw_input("Enter Availablecarbohydrateswithoutsugaralcohol(g):")),
    "Starch(g)":float(raw_input("Enter Starch(g):")),
    "Totalsugars(g)":float(raw_input("Enter Totalsugars(g):")),
    "Addedsugars(g)":float(raw_input("Enter Addedsugars(g):")),
    "Freesugars(g)":float(raw_input("Enter Freesugars(g):")),
    "Dietaryfibre(g)":float(raw_input("Enter Dietaryfibre(g):")),
    "Alcohol(g)":float(raw_input("Enter Alcohol(g):")),
    "Ash(g)":float(raw_input("Enter Ash(g):")),
    "PreformedvitaminA(retinol)(g):":float(raw_input("Enter Preformed vitamin A(retinol)(g):")),
    "Beta - carotene(g)":float(raw_input("Enter Beta - carotene(g):")),
    "ProvitaminA(b - carotene equivalents)(g)":float(raw_input("Enter Provitamin A(b - carotene equivalents) (g):")),
    "VitaminAretinolequivalents(g)":float(raw_input("Enter Vitamin A retinol equivalents(g):")),
    "Thiamin(B1)(mg)":float(raw_input("Enter Thiamin(B1)(mg):")),
    "Riboflavin(B2)(mg)":float(raw_input("Enter Riboflavin(B2)(mg):")),
    "Niacin(B3)(mg)":float(raw_input("Enter Niacin(B3)(mg):")),
    "Niacinderivedequivalents(mg)":float(raw_input("Enter Niacin derived equivalents(mg):")),
    "Folate, natural(g)":float(raw_input("Enter Folate, natural(g):")),
    "Folic acid(g):":float(raw_input("Enter Folic acid(g):")),
    "Total Folates(g)":float(raw_input("Enter Total Folates(g):")),
    "Dietaryfolateequivalents(g)":float(raw_input("Enter Dietary folate equivalents(g):")),
    "VitaminB6(mg)":float(raw_input("Enter Vitamin B6(mg):")),
    "VitaminB12(g)":float(raw_input("Enter Vitamin B12(g):")),
    "VitaminC(mg)":float(raw_input("Enter Vitamin C(mg):")),
    "Alpha-tocopherol(mg)":float(raw_input("Enter Alpha - tocopherol(mg):")),
    "VitaminE(mg)":float(raw_input("Enter Vitamin E(mg):")),
    "Calcium(Ca)(mg)":float(raw_input("Enter Calcium(Ca)(mg):")),
    "Iodine(I)(g)":float(raw_input("Enter Iodine(I)(g):")),
    "Iron(Fe)(mg)":float(raw_input("Enter Iron(Fe)(mg):")),
    "Magnesium(Mg)(mg)":float(raw_input("Enter Magnesium(Mg)(mg):")),
    "Phosphorus(P)(mg)":float(raw_input("Enter Phosphorus(P)(mg):")),
    "Potassium(K)(mg)":float(raw_input("Enter Potassium(K)(mg):")),
    "Selenium(Se)(g)":float(raw_input("Enter Selenium(Se)(g):")),
    "Sodium(Na)(mg)":float(raw_input("Enter Sodium(Na)(mg):")),
    "Zinc(Zn)(mg)":float(raw_input("Enter Zinc(Zn)(mg):")),
    "Caffeine(mg)":float(raw_input("Enter Caffeine(mg):")),
    "Cholesterol(mg)":float(raw_input("Enter Cholesterol(mg):")),
    "Tryptophan(mg)":float(raw_input("Enter Tryptophan(mg):")),
    "Totalsaturatedfat(g)":float(raw_input("Enter Totalsaturatedfat(g):")),
    "Totalmonounsaturatedfat(g)":float(raw_input("Enter Totalmonounsaturatedfat(g):")),
    "Totalpolyunsaturatedfat(g)":float(raw_input("Enter Totalpolyunsaturatedfat(g):")),
    "Linoleic acid(g)":float(raw_input("Enter Linoleic acid(g):")),
    "Alpha - linolenic acid(g)":float(raw_input("Enter Alpha - linolenic acid(g):")),
    "C20:5 w3 Eicosapentaenoic(mg)":float(raw_input("Enter C20:5 w3 Eicosapentaenoic(mg):")),
    "C22:5 w3 Docosapentaenoic(mg)":float(raw_input("Enter C22:5 w3 Docosapentaenoic(mg):")),
    "C22:6 w3 Docosahexaenoic(mg)":float(raw_input("Enter C22:6 w3 Docosahexaenoic(mg):")),
    "Total long chain omega3 fatty acids(mg)":float(raw_input("Enter Total long chain omega3 fatty acids(mg):")),
    "Totaltransfattyacids(mg)":float(raw_input("Enter Totaltransfattyacids(mg):"))}]
    dataf = pd.DataFrame(data)
    dataf1= dataf

    #Partioning features and label
    dataNutrition = dataNutrition[dataNutrition["GyclemicIndex"].notnull()]
    diabetes_X = dataNutrition.drop('GyclemicIndex', 1)
    diabetes_X=diabetes_X.drop('FoodName', 1)
    diabetes_Y = dataNutrition["GyclemicIndex"]

    #Preprocessing: Features are normalised
    robust_scaler = RobustScaler()
    diabetes_X=robust_scaler.fit_transform(diabetes_X)
    diabetes_X_train = diabetes_X

    # Build a forest and compute the feature importances (done once for feature selection)
    forest = ExtraTreesClassifier(n_estimators=250,random_state=0)
    forest.fit(diabetes_X, diabetes_Y)
    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_],
                 axis=0)
    indices = np.argsort(importances)[::-1]

    # Print the feature ranking
    #print("Feature ranking:")
    #for f in range(diabetes_X.shape[1]):
        #print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

    #Predicting GLycemic Index using Linear Regression
    diabetes_y_train = diabetes_Y
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)
    diabetes_X_test=dataf[["Energywithdietaryfibre(kJ)","Energywithoutdietaryfibre(kJ)","Totalfat(g)",
                         "Availablecarbohydrateswithsugaralcohols(g)","Availablecarbohydrateswithoutsugaralcohol(g)","Starch(g)",
                         "Alcohol(g)","Totalsaturatedfat(g)","Totalmonounsaturatedfat(g)","Totalpolyunsaturatedfat(g)",
                         "Totaltransfattyacids(mg)"]].values
    print diabetes_X_test
    GI=int(regr.predict(diabetes_X_test))
    print ("Glycemic Index: ",GI)
    netcarbs = float(dataf["Totalfat(g)"] + dataf["Availablecarbohydrateswithsugaralcohols(g)"] + dataf[
            "Availablecarbohydrateswithoutsugaralcohol(g)"]
                         - dataf["Alcohol(g)"] - dataf["Starch(g)"] + dataf["Totalsaturatedfat(g)"] + dataf[
                             "Totalmonounsaturatedfat(g)"] + dataf["Totalpolyunsaturatedfat(g)"]
                         + dataf["Totaltransfattyacids(mg)"])
    GlycemicLoad = (float)(netcarbs * GI * serving) / 10000.0
    print ("Glycemic Load: ",GlycemicLoad)

    if (GlycemicLoad < 10.0): #condition for low GL
        print("Food is appropriate for consumption")
    elif (GlycemicLoad <= 19.0 and sugarlevel <= 100.0): #condition for medium GL and normal blood sugar level
        print("Food is appropriate for consumption")
    elif (GlycemicLoad >= 20.0 and GI <= 55.0): #condition for high GL but low GI
        print("If food is consumed in lesser quatity, it would be fit for consumption")
        descision = raw_input("Do you still want a healthier food substitute(Y/N):")
    else: #Condition for high GI and GL
        print("Food is inappropriate for consumption")
        descision = raw_input("Do you want a healthier food substitute(Y/N):")

    #The model was evaluated using variance square and mean squared error
    # The mean squared error
    #print("Mean squared error: %.2f"
          #% np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
    # variance score
    #print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))
answer="n"
if(descision=="Y" or descision=="y"):#when the user wants a healthier substitute
    print "y"
    cnx=""
    try:
        cnx = MySQLdb.connect(user="root", passwd="root", host="127.0.0.1", port=3306)
        print("connected")
    except:
        print("not connected")

    #If the user entered food already has a case saved with better substitute
    sqlstring = 'select * from diabeticnutritionist.nutrition where food="%s"' % food
    df = pd.read_sql(sqlstring, cnx)
    if (df.size > 0):
        df1 = pd.read_sql_query(
            'select * from diabeticnutritionist.nutrition where bloodgroup=%(bloodgroup)s and food=%(food)s and gender=%(gender)s and age BETWEEN %(lower)s AND %(upper)s',
            cnx, params={"food": food, "gender": gender, "lower": lower, "upper": upper, "bloodgroup": bloodgroup})
        if(df1.size>0):
            substitute=df1["sub"].values
            print ("Healthier substitute will be: "+substitute)
            answer = raw_input("Is this a good substitute and ensures no allergies? (Y/N):")

    #when the user is unsatisfied with substitute or no substitute exists in our knowledge base for user entered food
    if(answer=="n" or answer=="N" or df.size<=0):
        dataNutrition1 = pd.read_csv('Nutrition Dataset.csv',usecols=["FoodName", "GyclemicIndex", "Energywithdietaryfibre(kJ)","Energywithoutdietaryfibre(kJ)", "Protein(g)",
                                                                      "Availablecarbohydrateswithsugaralcohols(g)","Availablecarbohydrateswithoutsugaralcohol(g)",
                                                                       "Dietaryfibre(g)", "VitaminAretinolequivalents(g)", "Thiamin(B1)(mg)",
                                                                       "Riboflavin(B2)(mg)", "Niacin(B3)(mg)", "Dietaryfolateequivalents(g)",
                                                                       "VitaminB6(mg)", "VitaminB12(g)", "VitaminC(mg)",
                                                                       "Alpha-tocopherol(mg)", "VitaminE(mg)", "Calcium(Ca)(mg)",
                                                                       "Iodine(I)(g)", "Iron(Fe)(mg)", "Magnesium(Mg)(mg)","Phosphorus(P)(mg)",
                                                                       "Potassium(K)(mg)", "Selenium(Se)(g)", "Sodium(Na)(mg)",
                                                                       "Zinc(Zn)(mg)"])
        value=[]
        if(flag==1):#when user entered food exists in dataset
            value=dataNutrition1[dataNutrition1["FoodName"]==food]
            value=value.drop('GyclemicIndex', 1)
        if(flag==0):#when user entered food does not exists in dataset
            value= dataf1[["FoodName", "Energywithdietaryfibre(kJ)","Energywithoutdietaryfibre(kJ)", "Protein(g)",
                                                                      "Availablecarbohydrateswithsugaralcohols(g)","Availablecarbohydrateswithoutsugaralcohol(g)",
                                                                       "Dietaryfibre(g)", "VitaminAretinolequivalents(g)", "Thiamin(B1)(mg)",
                                                                       "Riboflavin(B2)(mg)", "Niacin(B3)(mg)", "Dietaryfolateequivalents(g)",
                                                                       "VitaminB6(mg)", "VitaminB12(g)", "VitaminC(mg)",
                                                                       "Alpha-tocopherol(mg)", "VitaminE(mg)", "Calcium(Ca)(mg)",
                                                                       "Iodine(I)(g)", "Iron(Fe)(mg)", "Magnesium(Mg)(mg)","Phosphorus(P)(mg)",
                                                                       "Potassium(K)(mg)", "Selenium(Se)(g)", "Sodium(Na)(mg)",
                                                                       "Zinc(Zn)(mg)"]]

        #Running Kmeans to find a healthier substitute
        dataNutrition1 = dataNutrition1[dataNutrition1["GyclemicIndex"].notnull()]
        dataNutrition1 =dataNutrition1[dataNutrition1["GyclemicIndex"]<55]
        diabetes_X = dataNutrition1.drop('GyclemicIndex', 1)
        diabetes_X=diabetes_X.append(value)
        diabetes_X = diabetes_X.drop('FoodName', 1)
        X = np.array(diabetes_X)

        cluster_array = [cluster.vq.kmeans(diabetes_X, i) for i in range(1, 10)]

        # plt.plot([var for (cent, var) in cluster_array])
        # plt.show()

        kmeans = KMeans(n_clusters=3)
        kmeans.fit(X)
        centroid = kmeans.cluster_centers_
        labels = kmeans.labels_

        # print (centroid)
        #print(labels)

        for i in range(3):
            ds = X[np.where(labels == i)]
            # pyplot.plot(ds[:, 0], ds[:, 1], 'o')
            # lines = pyplot.plot(centroid[i, 0], centroid[i, 1], 'kx')
            # plt.setp(lines, ms=20.0)
            # plt.setp(lines, mew=5.0)
            # plt.show()
        diabetes_X["labels"]=labels
        listsub= diabetes_X[diabetes_X['labels'] == labels[labels.size-1]].index.get_values()
        min=100
        l=listsub[1]

        #finding the best substitute from the ones suggested by kmeans algorithm
        for i in range(0,listsub.size-1):
            if(dataNutrition1.ix[listsub[i],1]<min and dataNutrition1.ix[listsub[i],0]!=food):
                min=dataNutrition1.ix[listsub[i],1]
                #print min
                j=i
                l=listsub[i]
        listsub = np.array(listsub)
        listsub = np.delete(listsub, j)
        substitute= dataNutrition1.ix[l,0]
        print ("Healthier substitute will be: "+substitute)
        answer = raw_input("Is this a good substitute and ensures no allergies? (Y/N):")

        #till the user finds an appropriate substitute the search goes on and once the user finds the substitute it is saved in knowledge base for knowledge
        if(answer=="y" or answer=="Y"):
            cur = cnx.cursor()
            values=(age,gender,bloodgroup,str(sugarlevel),food,substitute)
            cur.execute('insert into diabeticnutritionist.nutrition (age,gender,bloodgroup,sugarlevel,food,sub) values (%s,%s,%s,%s,%s,%s)',values)
            cnx.commit()
        else:
            k=1
            a=0
            while(answer!="Y" and answer!="y"):
                l=listsub[k]
                substitute = dataNutrition1.ix[l,0]
                print ("Healthier substitute will be: " + substitute)
                answer = raw_input("Is this a good substitute and ensures no allergies? (Y/N):")
                if(k<listsub.size-2):
                    k=k+1
                else:
                    a=1
                    print "no more substitutes available"
                    answer="y"
            if a==0:
                cur = cnx.cursor()
                values = (age, gender, bloodgroup, str(sugarlevel), food, substitute)
                cur.execute(
                    'insert into diabeticnutritionist.nutrition (age,gender,bloodgroup,sugarlevel,food,sub) values (%s,%s,%s,%s,%s,%s)',
                    values)
                cnx.commit()


