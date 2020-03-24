from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
x = pd.DataFrame(iris.target)
print(x)
print(x[0].value_counts())