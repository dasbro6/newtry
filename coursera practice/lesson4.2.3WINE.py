import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)

try:
    wine = pd.read_csv('winequality-red.csv',sep=';')
except:
    print("Cannot find the file！")

# print(wine.info()) #看一下数据的基本情况
#
# print(wine.duplicated().sum())#计算重复总行数

wine = wine.drop_duplicates()#删除重复记录
# print(wine.describe())
# print(wine.quality.value_counts())#观察quality value的数量
#绘制饼图
# wine.quality.value_counts().plot(kind = 'pie' ,autopct = '%.4f')
# plt.show()

# print(wine.corr().quality)#quality与其他值的相关性
# sns.barplot(x = 'quality',y='volatile acidity',data = wine)
# sns.barplot(x = 'quality',y='alcohol',data = wine)
# plt.show()

from sklearn.preprocessing import LabelEncoder
#划分中高低档
bins = (2,4,6,8)
group_names = ['low','medium','high']
wine['quality_lb'] = pd.cut(wine['quality'],bins =bins,labels= group_names)
print(wine.quality_lb.value_counts())
print(wine)
lb_quality = LabelEncoder()
wine['label'] = lb_quality.fit_transform(wine['quality_lb'])



wine_copy = wine.copy()
wine.drop(['quality','quality_lb'],axis= 1,inplace = True)
X = wine.iloc[:,:-1]
y = wine.label
print(wine)
print(wine.label.value_counts())

#随机森林
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size= 0.2)

from sklearn.preprocessing import scale

print('X_train',X_train)
X_train = scale(X_train)
X_test = scale(X_test)
print('X_train',X_train)

from sklearn.metrics import confusion_matrix

rfc = RandomForestClassifier(n_estimators= 200)
rfc.fit(X_train,y_train)
y_pred = rfc.predict(X_test)
print(confusion_matrix(y_test,y_pred))


#暴力搜索
param_rfc ={"n_estimators":[10,20,30,40,50,60,70,80,90,100,200,300,],
            "criterion":["gini","entropy"]
            }
grid_rfc = GridSearchCV(rfc,param_rfc,iid =False)
grid_rfc.fit(X_train,y_train)
best_param_rfc =grid_rfc.best_params_
print(best_param_rfc)
#暴力后再学习
rfc = RandomForestClassifier(n_estimators= best_param_rfc['n_estimators'])
rfc.fit(X_train,y_train)
y_pred = rfc.predict(X_test)
print(confusion_matrix(y_test,y_pred))