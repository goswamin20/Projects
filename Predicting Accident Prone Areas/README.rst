Project: Prediction of Accident prone locations
===============================================

Participants
============

Nandini, Goswami, F16-IG-3007, goswamin, goswamin@iu.edu

Bhateja, Sarita, F16-IG-3003, sbhateja, sbhateja@iu.edu

Guruprasad, Kavya, F16-IG-3008, kavya_prasad, prasadk@iu.edu 


Abstract
========

The paper discusses the prediction of road accidents. We have UK road accident dataset for year 2015. The problem is treated as a machine learning classification problem and the outcome is classified as severity of accident on a range of 1-3 where 1 is the least severe and 3 is the most severe. The results have been visualized using bar graphs, line chart, histogram etc. Also, the location of various accident prone areas have been plotted on map. The data related to latitude and longitude of such locations in the dataset helped to achieve it.

References
==========

https://gitlab.com/cloudmesh_fall2016/project-042/blob/master/report/report.bib

Deliverables
============
===================================================================
Instructions on how to import Databricks notebook and run the code

==================================================================

1) Go to https://community.cloud.databricks.com and Sign Up.
2) Select the Community Edition.
3) Sign Up for Databricks Community Edition by entering personal details.
4) Select Workspaces from the left-hand column, and under workspaces, choose shared and select import under the dropdown.
5) Create Clusters by choosing the clusters in the left-hand column, click on te create cluster tab and enter the cluster name and Apache Spark Version Spark 2.0(Auto-Updating, Scala 2.0)
 


Running the Web Application to obtain the Google Map Images
============================================================

1) Install python version 3.4 or higher.

2) Virtual envirnment is needed to run the project. Python virtual environment is 13. To install virtual environment on you machine, the command is pip install virtualenv.

3) To create a virtual environment, the command is "virtualenv folder_name" 

4) Go inside the folder created in the previous command, where you will find bin file or scripts file depending on your OS.

5) Activate the virtual environment using the command "source bin/activate" for Mac and Linux system and "source script/activate

6) Create a database in postgress sql application named “data”. Postgress sql is the database.

7) In the folder src, you will find settings.py file, configure your username and password for postgress sql.

8) Dependencies of the project are there in requirements.txt file. Use pip install -r requirements.txt commands to install those dependencies

9) To run our first migrations(This is to create schemas in our database), command is “python manage.py makemigrations”, second command is “python manage.py migrate”

10) You can start the server using this command- python manage.py runserver.

11) The application runs in this URL:- localhost:8000

12) Used python excel library to export data from Django to database.

13) Exporting the database should be done using the URL:- localhost:8000/import_sheet/ and the database should be in xls format.

We have used simple JQuery, JavaScript in the front-end of the application to show the desired output.

Please find the code for this in the code in the google_map file in code directory

Visualization
==============

We have included the code of histogram.py under the code directory. This histogram is used for visualisation.

The dataset and the code needs to be in the same folder for it to run.
The pre-requisites for this is numpy,pandas,matplotlib and pylab for running the code.
The code saves a histogram image in pdf format
 


