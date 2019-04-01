import numpy as np
from sklearn import model_selection, svm
import pandas as pd
import pickle

bearings = ['Bearing1_1', 'Bearing1_2', 'Bearing1_6', 'Bearing1_7']
train_bearings = bearings[:-1]
test_bearings = bearings[-1]

df_train = pd.DataFrame()
for bearing in train_bearings:
    temp = pd.read_csv(bearing + '_final_features.csv')
    df_train = df_train.append(temp)

df_test = pd.DataFrame()
temp = pd.read_csv(test_bearings + '_final_features.csv')
df_test = df_test.append(temp)

X_train = np.array(df_train.drop(['RUL'], 1))
y_train = np.array(df_train['RUL'])
X_test = np.array(df_test.drop(['RUL'], 1))
y_test = np.array(df_test['RUL'])

clf = svm.SVC()
clf.fit(X_train, y_train)

with open('svm.pickle', 'wb') as f:
    pickle.dump(clf, f)

pickle_in = open('svm.pickle', 'rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)
print('Accuracy: {}'.format(accuracy))
