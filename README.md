
## ABOUT:

The project was done as part of final submission for IS843 - "Big Data Analytics for Business" for Questrom School Of Business in Spring,2023.

The project was under guidance of our professor Mohammad Soltanieh-ha.


## Table of Content:
- [Introduction](#introductionn)
    - [Contributors](#contributors)
    - [Database](#database)
    - [Intent](#intent)
- [Packages and Imports](#packages-and-imports)
    - [Packages](#packages)
    - [Imports](#imports)
- [Data Cleaning and EDA](#data-cleaning-and-eda)
- [Supervised Machine Learning](#supervised-machine-learning)
    - [Pipeline](#pipeline)
    - [Random Forest Regressor](#random-forest-regressor)
    - [Linear vs RandomForest Regression](#linear-vs-randomforest-regression)
- [Profile Based Analysis](#profile-based-analysis)
    - [RFormula](#rformula)
    - [Subscriber Stickiness](#subscriber-stickiness)
- [Business Account Prediction](#business-account-prediction)
    - [Feature Engineering](#feature-engineering)
    - [Business Account](#business-account)
- [Conclusions](#conclusions)
- [License](#license)

## Introduction

We, as a team have done our best efforts to analyse Instagram database available on Kaggle, using PySpark and associated tools taught during the semester. We have tried to use demonstrate use of EDA and various machine learning tools. 

### Contributors

Amit P, J Zhang, W Wang, X Yang, Zi Yuan L

### Database

The database can be found here - https://www.kaggle.com/datasets/shmalex/instagram-dataset

Note - Seems like the database was removed from Kaggle few days back.

### Intent

Use of various EDA and machine learning tools to come up with analytics that could establish patterns between various Instagram Features.

## Packages and Imports

### Packages

```bash
!pip install wordcloud
!pip install folium
```

### Imports

```bash
from pyspark.sql.functions import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import folium
from wordcloud import WordCloud, STOPWORDS
from pyspark.ml.feature import StringIndexer, VectorAssembler, OneHotEncoder
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import year, month, dayofweek, hour
from pyspark.sql.types import IntegerType
from pyspark.ml.regression import RandomForestRegressor
from pyspark.sql.window import Window
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator,MulticlassClassificationEvaluator
from pyspark.ml.classification import DecisionTreeClassifier,RandomForestClassifier
from pyspark.sql.types import FloatType
from pyspark.ml.linalg import Vector
```

## Data Cleaning and EDA]

 - Data Description, dropping nulls, creating cache.
 - Mapping the Top 100 Number of Likes and Number of Comments
 - Word Cloud of the Posts Decriptions of Posts with Top 10000 Number of Likes and Number of Comments
 - Top 10 Average Number of Comments and Average Number of Likes per Country
 - Post Time vs. Nunmber of likes and comments


## Supervised Machine Learning

### Pipeline

We created Pipeline with Vector Assembler (as preprocessor) and Linear Regression (as regression model)  with labels as 'numbr_likes'. RMSE = 3321.7373314512065

### Regression Evaluator

Changed the regression type to Random Forest Regression. RMSE = 4452.551173088263

### Linear vs RandomForest Regression

We repeated same test for linear and random forest regression for label as "number_comments". The RMSE is 104.59 in both the cases.


## Profile Based Analysis

We wanted to understand the impact of the profile characteristics like number of comments, likes, followers and followings on each other.

- How Many Profiles Have More Than One Post
- Relationship between Followers and Following
- Linear Regression of Followers on Other Features


### RFormula

We used RFormula as preprocessor and try to come up with linear regression with "followers" as label column. The model has RMSE of 135222 and MAE of 7906.89.

### Subscriber Stickiness

We wanted to analyse the subscriber stickiness. Subscriber stickiness can be best defined as how long does subscriber stay active. In this case, we wanted to how many subscribers stay active, for let's say 1 month, two months and so on.


## Business Account Prediction

Here, we wanted to understand the impact of various features towards an account being a business account.

### Feature Engineering

We used 'partitionBy' and removed outliers to ensure that we have tidy and clean data to process.

### Business Account

Our model tried to analyze if we can classify the profiles into business account or not. Random Forest Classifier had accuracy of around 87%.

## Conclusions

We had lot of key insights. Some of them are:

 - Thanks, Love and Life are some of the most figured keywords in the posts,
 - Posts from uncommon countries is more likely to get high comments and likes.
 - People are more active in the evening times as compared to rest of the day.
 - Most business accounts post a lot but have negligible growth in 'likes' received.
 - Users are typically active for about 1-4 months, after which activity declines rapidly.

### License
Jupyter will always be 100% open-source software, free for all to use and released under the liberal terms of the modified BSD license.
Link - https://jupyter.org/about

