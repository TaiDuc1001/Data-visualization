import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB

iris_data = pd.read_csv('C:\\Users\\DucPhan\\Documents\\Python\\Unuse\\filename2.csv')
iris_data.drop('Unnamed: 0', axis = 1, inplace = True)
x = iris_data.iloc[:,0:4]
y = iris_data.iloc[:,4]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, train_size = 0.8, random_state = 88, shuffle = True, stratify = y)

nb = GaussianNB()
nb.fit(x_train, y_train)
predicted_nb = nb.predict(x_test)

score_nb = cross_val_score(nb, x, y, cv = 10)

print(predicted_nb)
print(accuracy_score(y_test, predicted_nb))

print(score_nb)



















