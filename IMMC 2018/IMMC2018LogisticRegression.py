# IMMC 2018 HSMR Logistic Regression Model Calculation
# Team # US-7680

import sklearn
import pandas
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler
import pandas_ml as pdml
from imblearn.combine import SMOTETomek
import time
t0 = time.time()
import numpy
from sodapy import Socrata

client = Socrata("health.data.ny.gov", "Y4nGvKjaPPX0Hs04klcxbEKsN", username="crooksnoah@gmail.com", password="Slypie11!")

l = 1645096
results = pandas.read_csv("D:\Hospital_Inpatient_Discharges__SPARCS_De-Identified___2016.csv") #client.get("y93g-4rqn", limit = l)

e = 0
# Convert to pandas DataFrame
aresults = results

#results_df.filter(items=["Age Groups", "apr_drg_description", "apr_mdc_description", "APR Medical Surgical Description", "apr_risk_of_mortality",  "Facility Name", " patient_disposition", "Payment Typology 1", "Race","Type of Admission"]) 
aresults = aresults.rename(columns={"Patient Disposition":"y"})

print aresults
test1 = aresults.loc[(aresults["Facility Id"] == 1450.0)]
test1 = test1.drop(test1.columns[[0,1,2,3,4,6,9,13,13,14,15,16,17,18,19,22,23,24,24,27,28,30,31,33,34,36, 35, 20, 21, 32, 29]], axis=1)
print test1.columns
print test1
test1 = test1.reset_index()
locate1 = test1.loc
del test1['index']
for i in xrange(0,len(test1)):
    if locate1[i,"y"] == "Expired":
        locate1[i,"y"] = 1
        
    else:
        locate1[i,"y"] = 0
    if locate1[i, "Gender"] == "M":
        locate1[i,"Gender"] = 1
    else:
        locate1[i,"Gender"] = 0
    if locate1[i, "APR Medical Surgical Description"] == "Medical":
        locate1[i, "APR Medical Surgical Description"] = 1
    else:
        locate1[i, "APR Medical Surgical Description"] = 0
    if locate1[i,"Age Group"] == "0 to 17":
        locate1[i,"Age Group"] = 0
    elif locate1[i,"Age Group"] == "18 to 29":
        locate1[i,"Age Group"] = 1
    elif locate1[i,"Age Group"] == "30 to 49":
        locate1[i,"Age Group"] = 2
    else:
        locate1[i,"Age Group"] = 3
    if locate1[i, "Race"] == "White":
        locate1[i, "Race"] = 0
    else:
        locate1[i,"Race"] = 1
    if locate1[i,"Type of Admission"] == "Elective":
        locate1[i,"Type of Admission"] = 0
    elif locate1[i,"Type of Admission"] == "Emergency":
        locate1[i,"Type of Admission"] = 2
    else: 
        locate1[i,"Type of Admission"] = 1
    if locate1[i, "Payment Typology 1"] == "Medicare":
       locate1[i, "Payment Typology 1"] = 0
    elif locate1[i, "Payment Typology 1"] == "Medicare":
       locate1[i, "Payment Typology 1"] = 1 
    elif locate1[i, "Payment Typology 1"] == "Blue Cross/Blue Shield":
        locate1[i, "Payment Typology 1"] = 2
    else:
        locate1[i, "Payment Typology 1"] = 3
    if locate1[i,"y"] == 1:
        e = e+1    
print e
print "1"
test2 = aresults.loc[(aresults["Facility Id"] == 1456.0)]
test2 = test2.drop(test2.columns[[0,1,2,3,4,6,9,13,13,14,15,16,17,18,19,22,23,24,24,27,28,30,31,33,34,36, 35, 20, 21, 32, 29]], axis=1)

test2 = test2.reset_index()
locate1 = test2.loc
del test2['index']
for i in xrange(0,len(test2)):
    if locate1[i,"y"] == "Expired":
        locate1[i,"y"] = 1
        
    else:
        locate1[i,"y"] = 0
    if locate1[i, "Gender"] == "M":
        locate1[i,"Gender"] = 1
    else:
        locate1[i,"Gender"] = 0
    if locate1[i, "APR Medical Surgical Description"] == "Medical":
        locate1[i, "APR Medical Surgical Description"] = 1
    else:
        locate1[i, "APR Medical Surgical Description"] = 0
    if locate1[i,"Age Group"] == "0 to 17":
        locate1[i,"Age Group"] = 0
    elif locate1[i,"Age Group"] == "18 to 29":
        locate1[i,"Age Group"] = 1
    elif locate1[i,"Age Group"] == "30 to 49":
        locate1[i,"Age Group"] = 2
    else:
        locate1[i,"Age Group"] = 3
    if locate1[i, "Race"] == "White":
        locate1[i, "Race"] = 0
    else:
        locate1[i,"Race"] = 1
    if locate1[i,"Type of Admission"] == "Elective":
        locate1[i,"Type of Admission"] = 0
    elif locate1[i,"Type of Admission"] == "Emergency":
        locate1[i,"Type of Admission"] = 2
    else: 
        locate1[i,"Type of Admission"] = 1
    if locate1[i, "Payment Typology 1"] == "Medicare":
       locate1[i, "Payment Typology 1"] = 0
    elif locate1[i, "Payment Typology 1"] == "Medicare":
       locate1[i, "Payment Typology 1"] = 1 
    elif locate1[i, "Payment Typology 1"] == "Blue Cross/Blue Shield":
        locate1[i, "Payment Typology 1"] = 2
    else:
        locate1[i, "Payment Typology 1"] = 3
print "2"
test3 = aresults.loc[(aresults["Facility Id"] == 1438.0)]
test3 = test3.drop(test3.columns[[0,1,2,3,4,6,9,13,13,14,15,16,17,18,19,22,23,24,24,27,28,30,31,33,34,36, 35, 20, 21, 32, 29]], axis=1)

test3 = test3.reset_index()
locate1 = test3.loc
del test3['index']
for i in xrange(0,len(test3)):
    if locate1[i,"y"] == "Expired":
        locate1[i,"y"] = 1
        
    else:
        locate1[i,"y"] = 0
    if locate1[i, "Gender"] == "M":
        locate1[i,"Gender"] = 1
    else:
        locate1[i,"Gender"] = 0
    if locate1[i, "APR Medical Surgical Description"] == "Medical":
        locate1[i, "APR Medical Surgical Description"] = 1
    else:
        locate1[i, "APR Medical Surgical Description"] = 0
    if locate1[i,"Age Group"] == "0 to 17":
        locate1[i,"Age Group"] = 0
    elif locate1[i,"Age Group"] == "18 to 29":
        locate1[i,"Age Group"] = 1
    elif locate1[i,"Age Group"] == "30 to 49":
        locate1[i,"Age Group"] = 2
    else:
        locate1[i,"Age Group"] = 3
    if locate1[i, "Race"] == "White":
        locate1[i, "Race"] = 0
    else:
        locate1[i,"Race"] = 1
    if locate1[i,"Type of Admission"] == "Elective":
        locate1[i,"Type of Admission"] = 0
    elif locate1[i,"Type of Admission"] == "Emergency":
        locate1[i,"Type of Admission"] = 2
    else: 
        locate1[i,"Type of Admission"] = 1
    if locate1[i, "Payment Typology 1"] == "Medicare":
       locate1[i, "Payment Typology 1"] = 0
    elif locate1[i, "Payment Typology 1"] == "Medicare":
       locate1[i, "Payment Typology 1"] = 1 
    elif locate1[i, "Payment Typology 1"] == "Blue Cross/Blue Shield":
        locate1[i, "Payment Typology 1"] = 2
    else:
        locate1[i, "Payment Typology 1"] = 3
print "3"
test4 = aresults.loc[(aresults["Facility Id"] == 1463.0)]
test4 = test4.drop(test4.columns[[0,1,2,3,4,6,9,13,13,14,15,16,17,18,19,22,23,24,24,27,28,30,31,33,34,36, 35, 20, 21, 32, 29]], axis=1)

test4 = test4.reset_index()
locate1 = test4.loc
del test4['index']
for i in xrange(0,len(test4)):
    if locate1[i,"y"] == "Expired":
        locate1[i,"y"] = 1
        
    else:
        locate1[i,"y"] = 0
    if locate1[i, "Gender"] == "M":
        locate1[i,"Gender"] = 1
    else:
        locate1[i,"Gender"] = 0
    if locate1[i, "APR Medical Surgical Description"] == "Medical":
        locate1[i, "APR Medical Surgical Description"] = 1
    else:
        locate1[i, "APR Medical Surgical Description"] = 0
    if locate1[i,"Age Group"] == "0 to 17":
        locate1[i,"Age Group"] = 0
    elif locate1[i,"Age Group"] == "18 to 29":
        locate1[i,"Age Group"] = 1
    elif locate1[i,"Age Group"] == "30 to 49":
        locate1[i,"Age Group"] = 2
    else:
        locate1[i,"Age Group"] = 3
    if locate1[i, "Race"] == "White":
        locate1[i, "Race"] = 0
    else:
        locate1[i,"Race"] = 1
    if locate1[i,"Type of Admission"] == "Elective":
        locate1[i,"Type of Admission"] = 0
    elif locate1[i,"Type of Admission"] == "Emergency":
        locate1[i,"Type of Admission"] = 2
    else: 
        locate1[i,"Type of Admission"] = 1
    if locate1[i, "Payment Typology 1"] == "Medicare":
       locate1[i, "Payment Typology 1"] = 0
    elif locate1[i, "Payment Typology 1"] == "Medicare":
       locate1[i, "Payment Typology 1"] = 1 
    elif locate1[i, "Payment Typology 1"] == "Blue Cross/Blue Shield":
        locate1[i, "Payment Typology 1"] = 2
    else:
        locate1[i, "Payment Typology 1"] = 3
print "4"
test5 = aresults.loc[(aresults["Facility Id"] == 1439.0)]
test5 = test5.drop(test5.columns[[0,1,2,3,4,6,9,13,13,14,15,16,17,18,19,22,23,24,24,27,28,30,31,33,34,36, 35, 20, 21, 32, 29]], axis=1)
test5 = test5.reset_index()
locate1 = test5.loc
del test5['index']
for i in xrange(0,len(test5)):
    if locate1[i,"y"] == "Expired":
        locate1[i,"y"] = 1
        
    else:
        locate1[i,"y"] = 0
    if locate1[i, "Gender"] == "M":
        locate1[i,"Gender"] = 1
    else:
        locate1[i,"Gender"] = 0
    if locate1[i, "APR Medical Surgical Description"] == "Medical":
        locate1[i, "APR Medical Surgical Description"] = 1
    else:
        locate1[i, "APR Medical Surgical Description"] = 0
    if locate1[i,"Age Group"] == "0 to 17":
        locate1[i,"Age Group"] = 0
    elif locate1[i,"Age Group"] == "18 to 29":
        locate1[i,"Age Group"] = 1
    elif locate1[i,"Age Group"] == "30 to 49":
        locate1[i,"Age Group"] = 2
    else:
        locate1[i,"Age Group"] = 3
    if locate1[i, "Race"] == "White":
        locate1[i, "Race"] = 0
    else:
        locate1[i,"Race"] = 1
    if locate1[i,"Type of Admission"] == "Elective":
        locate1[i,"Type of Admission"] = 0
    elif locate1[i,"Type of Admission"] == "Emergency":
        locate1[i,"Type of Admission"] = 2
    else: 
        locate1[i,"Type of Admission"] = 1
    if locate1[i, "Payment Typology 1"] == "Medicare":
       locate1[i, "Payment Typology 1"] = 0
    elif locate1[i, "Payment Typology 1"] == "Medicare":
       locate1[i, "Payment Typology 1"] = 1 
    elif locate1[i, "Payment Typology 1"] == "Blue Cross/Blue Shield":
        locate1[i, "Payment Typology 1"] = 2
    else:
        locate1[i, "Payment Typology 1"] = 3
print "5"
aresults = aresults.drop(aresults.columns[[0,1,2,3,4,6,9,13,13,14,15,16,17,18,19,22,23,24,24,27,28,30,31,33,34,36, 35, 20, 21, 32, 29]], axis=1)
#results_df = results_df.drop(results_df.columns[[5,6,7,8,10,12,13,15,16,18]], axis=1)

aresults = aresults.loc[(aresults["Type of Admission" ]!="Newborn")]
aresults = aresults.loc[(aresults["y"] != "Left Against Medical Advice")]
aresults = aresults.dropna()
aresults = aresults.reset_index()
del aresults['index']



#test1 = locate[:"Facility Name"] == "New York Presbyterian Hospital - Columbia Presbyterian Center" | "New York Presbyterian Hospital - New York Weill Cornell Center"
#print test1
aresults = aresults.drop(aresults.index[100001:])
print aresults
for i in xrange(0,len(aresults)):
    if aresults.loc[i,"y"] == "Expired":
        aresults.loc[i,"y"] = 1
    else:
        aresults.loc[i,"y"] = 0
    if aresults.loc[i, "Gender"] == "M":
        aresults.loc[i,"Gender"] = 1
    else:
        aresults.loc[i,"Gender"] = 0
    if aresults.loc[i, "APR Medical Surgical Description"] == "Medical":
        aresults.loc[i, "APR Medical Surgical Description"] = 1
    else:
        aresults.loc[i, "APR Medical Surgical Description"] = 0
    if aresults.loc[i,"Age Group"] == "0 to 17":
        aresults.loc[i,"Age Group"] = 0
    elif aresults.loc[i,"Age Group"] == "18 to 29":
       aresults.loc[i,"Age Group"] = 1
    elif aresults.loc[i,"Age Group"] == "30 to 49":
        aresults.loc[i,"Age Group"] = 2
    else:
        aresults.loc[i,"Age Group"] = 3
    if aresults.loc[i, "Race"] == "White":
        aresults.loc[i, "Race"] = 0
    else:
        aresults.loc[i,"Race"] = 1
    if aresults.loc[i,"Type of Admission"] == "Elective":
        aresults.loc[i,"Type of Admission"] = 0
    elif aresults.loc[i,"Type of Admission"] == "Emergency":
        aresults.loc[i,"Type of Admission"] = 2
    else: 
        aresults.loc[i,"Type of Admission"] = 1
    if aresults.loc[i, "Payment Typology 1"] == "Medicare":
       aresults.loc[i, "Payment Typology 1"] = 0
    elif aresults.loc[i, "Payment Typology 1"] == "Medicare":
       aresults.loc[i, "Payment Typology 1"] = 1 
    elif aresults.loc[i, "Payment Typology 1"] == "Blue Cross/Blue Shield":
        aresults.loc[i, "Payment Typology 1"] = 2
    else:
        aresults.loc[i, "Payment Typology 1"] = 3
print "aresults"    
#print df
test1 = test1.replace("120 +", 120)
test2 = test2.replace("120 +", 120)
test3 = test3.replace("120 +", 120)
test4 = test4.replace("120 +", 120)
test5 = test5.replace("120 +", 120)
scaler = MinMaxScaler()

test1 = pdml.ModelFrame(scaler.fit_transform(test1), columns = test1.columns)
test2 = pdml.ModelFrame(scaler.fit_transform(test2), columns = test2.columns)
test3 = pdml.ModelFrame(scaler.fit_transform(test3), columns = test3.columns)
test4 = pdml.ModelFrame(scaler.fit_transform(test4), columns = test4.columns)
test5 = pdml.ModelFrame(scaler.fit_transform(test5), columns = test5.columns)



bresults = aresults.replace("120 +", "120")

bresults = pdml.ModelFrame(scaler.fit_transform(bresults), columns = bresults.columns)

import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


##creates heatmap to test independence
#sns.heatmap(bresults.corr())
#plt.show()



X = (bresults.as_matrix(bresults.columns[[0,1,2,3,5,6]]))
y = (bresults.as_matrix(bresults.columns[[4]]))
y = y.astype(int)
X = X.astype(int)
X_test1 = test1.as_matrix(test1.columns[[0,1,2,3,5,6]])
X_test1 = X_test1.astype(int)
y_test1 = test1.as_matrix(test1.columns[[4]])
print y_test1
y_test1 =y_test1.astype(int)
X_test2 = test2.as_matrix(test2.columns[[0,1,2,3,5,6]])
X_test3 = test3.as_matrix(test3.columns[[0,1,2,3,5,6]])
X_test4 = test4.as_matrix(test4.columns[[0,1,2,3,5,6]])
X_test5 = test5.as_matrix(test5.columns[[0,1,2,3,5,6]])
y_test2 = test2.as_matrix(test2.columns[[4]])
y_test3 = test3.as_matrix(test3.columns[[4]])
y_test4 = test4.as_matrix(test4.columns[[4]])
y_test5 = test5.as_matrix(test5.columns[[4]])
y=numpy.ravel(y)
y_test2 =y_test2.astype(int)
y_test3 =y_test3.astype(int)
y_test4 =y_test4.astype(int)
y_test5 =y_test5.astype(int)
X_test2 = X_test2.astype(int)
X_test3 = X_test3.astype(int)
X_test4 = X_test4.astype(int)
X_test5 = X_test5.astype(int)
#print X
#print y
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

ros = SMOTETomek( ratio="minority", random_state=42, k=5)
X_res, y_res = ros.fit_sample(X_train, y_train)

classifier = LogisticRegression(random_state=0,C=1, penalty="l2", solver = "sag", class_weight= {1:1, 0:3})
classifier.fit(X_res, y_res)
y_pred1 = classifier.predict(X_test1)
print y_pred1
y_pred2 = classifier.predict(X_test2)
y_pred3 = classifier.predict(X_test3)
y_pred4 = classifier.predict(X_test4)
y_pred5 = classifier.predict(X_test5)
from sklearn.metrics import confusion_matrix

#print(confusion_matrix(y_test, y_pred_p))
confusion_matrix1 = confusion_matrix(y_test1, y_pred1)
confusion_matrix2 = confusion_matrix(y_test2, y_pred2)
confusion_matrix3 = confusion_matrix(y_test3, y_pred3)
confusion_matrix4 = confusion_matrix(y_test4, y_pred4)
confusion_matrix5 = confusion_matrix(y_test5, y_pred5)
print confusion_matrix1
print confusion_matrix2
print confusion_matrix3
print confusion_matrix4
print confusion_matrix5
prob1 = classifier.predict_proba(X_test1)
prob2 = classifier.predict_proba(X_test2)
prob3 = classifier.predict_proba(X_test3)
prob4 = classifier.predict_proba(X_test4)
prob5 = classifier.predict_proba(X_test5)
print(classification_report(y_test1, y_pred1, target_names=["alive", "dead"]))

roc = sklearn.metrics.roc_auc_score(y_test1,y_pred1)
print sum(prob1)
print sum(prob2)
print sum(prob3)
print sum(prob4)
print sum(prob5)
print roc

print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_res, y_res)))

