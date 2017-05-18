# Databricks notebook source exported at Sat, 3 Dec 2016 12:08:16 UTC
# MAGIC %md ###Prediction of Accident prone locations using Apache Spark on Databricks Community Edition
# MAGIC ###Problem Statement
# MAGIC Every day a number of people die out of road accidents all over the world. The severity of road accidents is more in densely populated countries. A country's asset is their population and the health and safety of it is the top priority of every country. This project would help in decreasing road accidents and ensure better road safety. We haved used the UK road accidents dataset to analyse and classify which locations are more prone to severe accidents. We have taken into consideration numerous attributes which affects road accidents to predict the same. Additionally we will be plotting these accidents prone locations on Google map depending on the severity of accidents that took place at those locations.
# MAGIC In order to implement this project we have used python and Apache Spark.
# MAGIC 
# MAGIC 
# MAGIC ###Dataset
# MAGIC 1. <a href="https://github.com/kavyaprasad/accident_Data/blob/master/DfTRoadSafety_Accidents_2015.csv"><b>AccidentData.csv</b></a> - This file contails data about Accident. The various attributes present in the dataset are
# MAGIC   1. Accident Index: Index of each accident (STRING)
# MAGIC   2. Location Easting OSGR: Gives Us the exact location of the place (INTEGER)
# MAGIC   3. Location Northing OSGR: Gives Us the exact location of the place (INTEGER)
# MAGIC   4. Longitude : Longitude of the place (INTEGER)
# MAGIC   5. Latitude: Latitude of the place (INTEGER)
# MAGIC   6. Police Force: Number of police available at that time (INTEGER)
# MAGIC   7. Accident Severity:  Severity of the accident (INTEGER)
# MAGIC   8. Number of Vehicles:  Number of involved in the accident (INTEGER)
# MAGIC   9. Number of Casualties:  Number of people died or injured (INTEGER)
# MAGIC   10. Date: The date of travel (INTEGER)
# MAGIC   11. Day of Week: Day of the week (INTEGER)
# MAGIC   12. Time: Time of the accident (STRING)
# MAGIC   13. Local Authority(District): local district number (INTEGER)
# MAGIC   14. Local Authority(Highway): local Highway number (STRING)
# MAGIC   15. 1st Road Class: Hierarchy which the road falls in  (INTEGER)
# MAGIC   16. 1st Road Number: Road number (STRING)
# MAGIC   17. Speed limit: Speed limit in the road (INTEGER)
# MAGIC   18. Junction Detail: Each number in this column various junction types (INTEGER)
# MAGIC   19. Junction Control: Kind of control (INTEGER)
# MAGIC   20. 2nd Road Class: Hierarchy which the road falls in (INTEGER)
# MAGIC   21. 2nd Road Number: Road number (STRING)
# MAGIC   22. Pedestrian Crossing Human Control: Human Control for Pedestrian Crossing (INTEGER)
# MAGIC   23. Pedestrian Crossing Physical Facilities: Physical Facilities for Pedestrian Crossing (INTEGER)
# MAGIC   24. Light Conditions: Daytime or Nightime (INTEGER)
# MAGIC   25. Weather Conditions: Weather Conditions when the accident happened (INTEGER)
# MAGIC   26. Road Surface Conditions: Road Surface Conditions where the accident occured (INTEGER)
# MAGIC   27. Special Conditions at Site: Other Conditions prevailing at the accident spot (INTEGER)
# MAGIC   28. Carriageway Hazards:  Carriageway Hazards in the past (STRING)
# MAGIC   29. Urban or Rural Area: Is it an Urban or rural area (INTEGER)
# MAGIC   30. Did Police Officer Attend Scene of Accident: Did Police Officer Attend Scene of Accident (INTEGER)
# MAGIC   31. LSOA of Accident Location: Accident location (STRING)

# COMMAND ----------

# MAGIC %md ### Dataset Link
# MAGIC 
# MAGIC Download the dataset using the shell command wget and the URL, save them into the tmp directory. The URL for the dataset is
# MAGIC AccidentData: https://raw.githubusercontent.com/kavyaprasad/accident_Data/master/DfTRoadSafety_Accidents_2015.csv

# COMMAND ----------

# MAGIC %sh
# MAGIC wget -P /tmp "https://raw.githubusercontent.com/kavyaprasad/accident_Data/master/DfTRoadSafety_Accidents_2015.csv"

# COMMAND ----------

# MAGIC %md ### Uploading the dataset into Databricks file system
# MAGIC 
# MAGIC Databricks file system is a distributed file system lying on top of Amazon S3. We will upload the data from the local file system into our DBFS. Below is a python script which copies the data from the local file system into the datasets folder of DBFS of your cluster.
# MAGIC 
# MAGIC The local files are referenced using `file:/` and DBFS files are referenced using `dbfs:/`

# COMMAND ----------

localAccidentDataFilePath = "file:/tmp/DfTRoadSafety_Accidents_2015.csv"
dbutils.fs.mkdirs("dbfs:/datasets")
dbutils.fs.cp(localAccidentDataFilePath, "dbfs:/datasets/")
#Displaying the files present in the DBFS datasets folder of your cluser
display(dbutils.fs.ls("dbfs:/datasets"))

# COMMAND ----------

#Number of accidents based on the severity
AccidentRDD=sc.textFile("dbfs:/datasets/DfTRoadSafety_Accidents_2015.csv")
header= AccidentRDD.first()
AccidentFilterRDD = AccidentRDD.filter(lambda line:line!=header)
AccidentSplitRDD = AccidentFilterRDD.map(lambda row: row.split(","))
AccidentMapRDD2=AccidentSplitRDD.map(lambda x : (x[6],1)).reduceByKey(lambda acc, val : acc+val)
AccidentSwappedRDD2=AccidentMapRDD2.map(lambda (a, b): (b, a))
AccidentDescendingRDD2=AccidentSwappedRDD2.sortByKey(0)
for i in AccidentDescendingRDD2.take(20): print(i)


# COMMAND ----------

#Number of accidents and their severity during daytime
new_AccidentSplitRDD=AccidentSplitRDD.filter(lambda x : x[24]=="1")
AccidentMapRDD2=new_AccidentSplitRDD.map(lambda x : (x[6],1)).reduceByKey(lambda acc, val : acc+val)
AccidentSwappedRDD2=AccidentMapRDD2.map(lambda (a, b): (b, a))
AccidentDescendingRDD2=AccidentSwappedRDD2.sortByKey(0)
for i in AccidentDescendingRDD2.take(20): print(i)

# COMMAND ----------

#Number of accidents and their severity during night time

new_AccidentSplitRDD3=AccidentSplitRDD.filter(lambda x : x[24]=="4")
AccidentMapRDD3=new_AccidentSplitRDD3.map(lambda x : (x[6],1)).reduceByKey(lambda acc, val : acc+val)
AccidentSwappedRDD3=AccidentMapRDD3.map(lambda (a, b): (b, a))
AccidentDescendingRDD3=AccidentSwappedRDD3.sortByKey(0)
for i in AccidentDescendingRDD3.take(20): print(i)



# COMMAND ----------

from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.classification import LogisticRegression, OneVsRest
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from collections import namedtuple
from pyspark.sql import SQLContext, Row
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from pyspark.sql.functions import *
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import OneHotEncoder, StringIndexer
from pyspark.ml import Pipeline
from pylab import *

# COMMAND ----------

# printing data
for i in AccidentSplitRDD.take(20): print(i)

#Created schema for the temporary table to be created
parsedData = AccidentSplitRDD.map(lambda p: Row(Accident_Index=p[0],Location_Easting_OSGR=p[1],Location_Northing_OSGR=p[2],Longitude=p[3],Latitude=p[4],Police_Force=p[5],Accident_Severity=p[6],Number_of_Vehicles=p[7],Number_of_Casualties=p[8],Date=p[9],Day_of_Week=p[10],Time=p[11],Local_Authority_District=p[12],Local_Authority_Highway=p[13],first_Road_Class=p[14],first_Road_Number=p[15],Road_Type=p[16],Speed_limit=p[17],Junction_Detail=p[18],Junction_Control=p[19],second_Road_Class=p[20],second_Road_Number=p[21],Pedestrian_Crossing_Human_Control=p[22],Pedestrian_Crossing_Physical_Facilities=p[23],Light_Conditions=p[24],Weather_Conditions=p[25],Road_Surface_Conditions=p[26],Special_Conditions_at_Site=p[27],Carriageway_Hazards=p[28],Urban_or_Rural_Area=p[29],Did_Police_Officer_Attend_Scene_of_Accident=p[30],LSOA_of_Accident_Location=p[31]))

# COMMAND ----------

#Dataframe is created from the parsed data
schemaAllData = spark.createDataFrame(parsedData)#dataframe is created
schemaAllData.printSchema()# schema of the dataframe printed
schemaAllData.show()
schemaAllData=schemaAllData.na.drop()#dropped rows containing null values 
schemaAllData.registerTempTable("AccidentData")#the dataframe is registered to a temporary table named AccidentData

# COMMAND ----------
sql_resultsall = sqlContext.sql("Select Accident_Index,Police_Force,Accident_Severity,Number_of_Vehicles,Number_of_Casualties,Day_of_Week,first_Road_Class,Road_Type,Speed_limit,Junction_Detail,Junction_Control,second_Road_Class,Pedestrian_Crossing_Human_Control,Pedestrian_Crossing_Physical_Facilities,Light_Conditions,Weather_Conditions,Road_Surface_Conditions,Special_Conditions_at_Site,Carriageway_Hazards,Urban_or_Rural_Area from AccidentData")

# COMMAND ----------

#sql commands for transforming time

sql_results = sqlContext.sql("Select Accident_Index,Time from AccidentData where Time>='18:00' and Time <='23:59'")
sql_results1 = sqlContext.sql("Select Accident_Index,Time from AccidentData where Time>='12:00' and Time <='17:59'")
sql_results2 = sqlContext.sql("Select Accident_Index,Time from AccidentData where Time>='06:00' and Time <='11:59'")
sql_results3 = sqlContext.sql("Select Accident_Index,Time from AccidentData where Time>='00:00' and Time <='05:59'")

# Time Datframes converted to rdd and transformed
sql_results3 = sql_results3.rdd
time3 = sql_results3.map(lambda p: (p[0],1))# Time between '00:00' and '05:59' is transformed to 1
sql_results2 = sql_results2.rdd
time2 = sql_results2.map(lambda p: (p[0],2))# Time between '06:00' and '11:59' is transformed to 2
sql_results1 = sql_results1.rdd
time1 = sql_results1.map(lambda p: (p[0],3))# Time between '12:00' and '17:59' is transformed to 3
sql_results = sql_results.rdd
time = sql_results.map(lambda p: (p[0],4))# Time between '18:00' and '23:59' is transformed to 4

timeRDD=time3.union(time2).union(time1).union(time)# created union of all 4 time rdd
timeData=timeRDD.map(lambda p: Row(Accident_Index1=p[0],Time1=p[1]))# created schema

schemaNewTime = spark.createDataFrame(timeData)
schemaNewTime.printSchema()
schemaNewTime.show()
schemaNewTime.registerTempTable("timeData")
sql_TimeResults = sqlContext.sql("Select Accident_Index1,Time1 from timeData")

# COMMAND ----------

# Join operation performed

join = sqlContext.sql("select Accident_Index,Accident_Index1,Police_Force,Accident_Severity as binary_response,Number_of_Vehicles,Number_of_Casualties,Day_of_Week,first_Road_Class,Road_Type,Speed_limit,Junction_Detail,Junction_Control,second_Road_Class,Pedestrian_Crossing_Human_Control,Pedestrian_Crossing_Physical_Facilities,Light_Conditions,Weather_Conditions,Road_Surface_Conditions,Special_Conditions_at_Site,Carriageway_Hazards,Urban_or_Rural_Area,Time1 from timeData,AccidentData where timeData.Accident_Index1 = AccidentData.Accident_Index and AccidentData.Accident_Index IS NOT NULL and timeData.Accident_Index1 IS NOT NULL ")

# All data values are casted into float values 
joinrdd=join.select(join.Police_Force.cast('float'),join.binary_response.cast('float'),join.Number_of_Vehicles.cast('float'),join.Number_of_Casualties.cast('float'),join.Day_of_Week.cast('float'),join.first_Road_Class.cast('float'),join.Road_Type.cast('float'),join.Speed_limit.cast('float'),join.Junction_Detail.cast('float'),join.Junction_Control.cast('float'),join.second_Road_Class.cast('float'),join.Pedestrian_Crossing_Human_Control.cast('float'),join.Pedestrian_Crossing_Physical_Facilities.cast('float'),join.Light_Conditions.cast('float'),join.Weather_Conditions.cast('float'),join.Road_Surface_Conditions.cast('float'),join.Special_Conditions_at_Site.cast('float'),join.Carriageway_Hazards.cast('float'),join.Urban_or_Rural_Area.cast('float'),join.Time1.cast('float'))


# COMMAND ----------

#This section of code is refered from:
#cite:https://vanishingcodes.wordpress.com/2016/06/09/pyspark-tutorial-building-a-random-forest-binary-classifier-on-unbalanced-dataset/
cols_now =['Police_Force','Number_of_Vehicles','Number_of_Casualties','Day_of_Week','first_Road_Class','Road_Type','Speed_limit','Junction_Detail','Junction_Control','second_Road_Class','Pedestrian_Crossing_Human_Control','Pedestrian_Crossing_Physical_Facilities','Light_Conditions','Weather_Conditions','Road_Surface_Conditions','Special_Conditions_at_Site','Carriageway_Hazards','Urban_or_Rural_Area','Time1']
cols_now1=['Police_Force1','Number_of_Vehicles1','Number_of_Casualties1','Day_of_Week1']

indexers = [StringIndexer(inputCol=x, outputCol=x+'_tmp')
            for x in cols_now ]


encoders = [OneHotEncoder(dropLast=False, inputCol=x+"_tmp", outputCol=y)
for x,y in zip(cols_now,cols_now1)]
tmp = [[i,j] for i,j in zip(indexers, encoders)]
tmp = [i for sublist in tmp for i in sublist]


assembler_features = VectorAssembler(inputCols=cols_now, outputCol='features')
labelIndexer = StringIndexer(inputCol='binary_response', outputCol='label')
tmp += [assembler_features, labelIndexer]
pipeline = Pipeline(stages=tmp)

allData = pipeline.fit(joinrdd).transform(joinrdd)
allData.cache()
trainingData, testData = allData.randomSplit([0.8,0.2], seed=0) 

# COMMAND ----------

# COMMAND ----------
# Decision Tree
dt = DecisionTreeClassifier(labelCol="label", featuresCol="features")
model = dt.fit(trainingData)

# Make predictions.
predictions = model.transform(testData)

# Select example rows to display.
predictions.select("prediction", "label", "features").show(5)

# Select (prediction, true label) and compute test error
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Test Error percentage: %"+str((1.0 - accuracy)*100))
print("Accuracy percentage: %"+str(accuracy*100))

# summary only
print(model)

# COMMAND ----------

# COMMAND ----------
#Logistic Regression
lr = LogisticRegression(maxIter=10, tol=1E-6, fitIntercept=True)

# instantiate the One Vs Rest Classifier.
ovr = OneVsRest(classifier=lr)

# train the multiclass model.
ovrModel = ovr.fit(trainingData)

# score the model on test data.
predictions = ovrModel.transform(testData)

# obtain evaluator.
evaluator = MulticlassClassificationEvaluator(metricName="accuracy")

# compute the classification error on test data.
accuracy = evaluator.evaluate(predictions)
print("Test Error percentage: %" +str((1 - accuracy)*100))
print("Accuracy percentage: %" + str(accuracy*100))
