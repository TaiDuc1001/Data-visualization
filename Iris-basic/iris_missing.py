import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
# print(iris.target)
iris_data = pd.DataFrame(iris.data, columns = iris.feature_names)
iris_data['label'] = iris.target
# iris_data.to_csv('filename2.csv')

plt.scatter(iris_data.iloc[:,2], iris_data.iloc[:,3], c= iris.target)
plt.xlabel('Petal Lenght (cm)')
plt.ylabel('Petal width (cm)')
plt.grid()
plt.show()












