#%%
from sklearn.model_selection import KFold
import pandas as pd
import sklearn.metrics
import autosklearn.classification
import autosklearn.metrics

#%%
df_clean = pd.read_csv('noshowappointments-kagglev2-may-2016_clean.csv')
print(df_clean.head(3))

#%%
kept_columns = ['Scholarship', 'Diabetes', 'Alcoholism', 'SMS_received', 'WaitDays', 'Age']
df_features = df_clean[kept_columns].copy()
print(df_features.head())

#%%
df_labels = df_clean['No-show'].map({True:1, False:0}).copy()
df_labels.head()

#%%
kf = KFold(n_splits=5, shuffle=True, random_state=42)

for train_index, test_index in kf.split(df_features):
    features_train, features_test = df_features.loc[train_index], df_features.loc[test_index]
    labels_train, labels_test = df_labels.loc[train_index], df_labels.loc[test_index]

#%%
automl = autosklearn.classification.AutoSklearnClassifier()
automl.fit(features_train, labels_train)
pred = automl.predict(features_test)

#%%
# Accuracy Score
print("Accuracy score:{}".format(sklearn.metrics.accuracy_score(labels_test, pred)))

#%%
# Precision
print("Precision:{}".format(autosklearn.metrics.precision(labels_test, pred)))

#%%
# Recall
print("Recall:{}".format(autosklearn.metrics.recall(labels_test, pred)))
