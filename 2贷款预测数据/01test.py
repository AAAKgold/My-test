#########################################################################
# File Name: test.py
# Author: Kgod
# mail: 17621512033@163.com
# Created Time: 2019年01月02日 星期三 22时51分25秒
#########################################################################
#!usr/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")#Reading the dataset in a dataframe using Pandas

print(df.head(10))
print(df.describe())
#print(df['Property_Area'].value_counts())
#print(df['Credit_History'].value_counts())

#print(df['ApplicantIncome'].hist(bins=50))
#plt.show()
'''
print(df.boxplot(column='ApplicantIncome'))
plt.show()
'''
#df.boxplot(column = 'ApplicantIncome',by ='Education')
#plt.show()

#df['LoanAmount'].hist(bins=50)
#plt.show()
'''
df.boxplot(column='LoanAmount')
plt.show()
'''

temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
#print('Frequency Table for Credit History:')
#print(temp1)

#print('\nProbility of getting loan for each Credit_History class:')
#print(temp2)

'''
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Credit_History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title("Applicants by Credit_History")
temp1.plot(kind='bar')
#plt.show()
ax2 = fig.add_subplot(122)
temp2.plot(kind = 'bar')
ax2.set_xlabel('Credit_History')
ax2.set_ylabel('Probability of getting loan')
ax2.set_title("Probability of getting loan by credit history")
#plt.show()
'''
#下面的操作和上面效果一样
#temp3 = pd.crosstab(df['Credit_History'],df['Loan_Status'])
#temp3.plot(kind='bar',stacked=True,color=['red','blue'],grid=False)
#plt.show()


# missing values
#print(df.apply(lambda x: sum(x.isnull()),axis=0))

#df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)
#f = df.boxplot(column='LoanAmount',by=['Self_Employed','Education'])
#plt.show()


df['Self_Employed'].fillna('No',inplace=True)

table = df.pivot_table(values='LoanAmount',index='Self_Employed',columns='Education',aggfunc=np.median)

#Define function to return value of this pivot_table
def fage(x):
    return table.loc[x['Self_Employed'],x['Education']]
#Replace missing values
df['LoanAmount'].fillna(df[df['LoanAmount'].isnull()].apply(fage,axis=1),inplace=True)

#f = df.boxplot(column='LoanAmount',by=['Self_Employed','Education'])
#plt.show()


#df['LoanAmount_log'] = np.log(df['LoanAmount'])
#df['LoanAmount_log'].hist(bins=20)
#plt.show()


#df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']
#df['TotalIncome_log'] = np.log(df['TotalIncome'])
#df['TotalIncome_log'].hist(bins=20)
#plt.show()


df['Gender'].fillna(df['Gender'].mode()[0],inplace=True)
df['Married'].fillna(df['Married'].mode()[0],inplace=True)
df['Dependents'].fillna(df['Dependents'].mode()[0],inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0],inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0],inplace=True)

from sklearn.preprocessing import LabelEncoder

var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']
le = LabelEncoder()
for i in var_mod:
    df[i] = le.fit_transform(df[i])
df.dtypes

#Import model form scikit learn module
from sklearn.linear_model import LogisticRegression

##from sklearn.cross_validation import KFold 
from sklearn.model_selection import KFold 

#For K-fold cross validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn import metrics

'''
#Generic function for making a classification model and acessing performance:
def classification_model(model,data,predictors,outcome):
    #Fit the model:
    model.fit(data[predictors],data[outcome])

    #Make predictions on training set:
    predictions = model.predict(data[predictors])

    #Print accuracy
    accuracy = metrics.accuracy_score(predictions,data[outcome])
    print("Accuracy : %s" % "{0:.3%}".format(accuracy))

    #Preform k-fold cross-validation with 5 folds 
    kf = KFold(data.shape[0],n_folds=5)
    error = []
    for train,test in kf:
        #Filter training data
        train_predictors = (data[predictors].iloc[train,:])

    #The target we're using to train the algorithm.
    train_target = data[outcome].iloc[train]

    #Training the algorithm using the predictors and target
    model.fit(train_predictors,train_target)

    #Record error from each cross-validation run
    #error.append(model.score(data[predictors].iloc[test,:],data[outcome].iloc[test]))

    print("Cross-Validation Score : %s " % "{0:.3%}".format(np.mean(error)))

    #Fit the mdoel again so that it can be refered outside the function
    model.fit(data[predictors],data[outcome])


outcome_var = ['Loan_Status']
model = LogisticRegression()
predictor_var = ['Credit_History']
classification_model(model,df,predictor_var,outcome_var)
有误KFold(交叉检验)
'''


#Decision Tree

#model = DecisionTreeClassifier()
#predictor_var = ['Credit_History','Gender','Married','Education']
#classification_model(model,df,predictor_var,outcome_var)

#We can try different combination of variables:
#predictor_var = ['Credit_History','Loan_Amount_Term','LoanAmount_log']
#classification_model(model,df,predictor_var,outcome_var)


#Random Forest

model = RandomForestClassifier(n_estimators=100)

model.fit()

predictor_var = ['Gender','Married','Dependents','Education','Self_Employed','Loan_Amount_Term','Credit_History','Property_Area','LoanAmount_log','TotalIncome_log']
#classification_model(model,df,predictor_var,outcome_var)


#Create a series with feature importances:
featimp = pd.Series(model.feature_importances_,index=predictor_var).sort_values(ascending=False)
print(featimp)






























