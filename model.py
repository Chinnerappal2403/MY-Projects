import pandas as pd
from sklearn.model_selection import train_test_split # used for splitting training and testing data
from sklearn.preprocessing import StandardScaler # used for feature scaling
from sklearn.linear_model import LogisticRegression
import pickle
dataset1 = pd.read_excel('test.xlsx')
dataset1.fillna(dataset1.mean(), inplace=True)
C = dataset1.iloc[:, :-1].values # attributes to determine dependent variable / Class
D = dataset1.iloc[:, -1].values# dependent variable / Class
X_train1, X_test1, y_train1, y_test1 = train_test_split(C,D, test_size = 0.23, random_state = 46)
sc_X1 = StandardScaler()
X_train1 = sc_X1.fit_transform(X_train1)
X_test1 = sc_X1.transform(X_test1)
from imblearn.over_sampling import SMOTE 

sm = SMOTE(random_state = 2) 

X_train_res, y_train_res = sm.fit_sample(X_train1, y_train1.ravel()) 
 
LR1=LogisticRegression()

# Train the model
LR1=LR1.fit(X_train_res, y_train_res)

# Saving model to disk
pickle.dump(LR1, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

