import pandas as pd
import numpy as np

unames = ['user id','age','gender','occunpation','zip code']
users = pd.read_csv('ml-100k/u.user',sep='|',names = unames)
# print(users)
rnames = ['user id','item id','rating','timestamp']
ratings = pd.read_csv('ml-100k/u.data',sep = '\t',names = rnames)
# print(ratings)

users_df = users.loc[:,['user id','gender']]
ratings_df = ratings.loc[:,['user id','rating',]]
rating_df = pd.merge(users_df,ratings_df)
print(rating_df)

print(rating_df.groupby('gender').rating.std())
print(rating_df.groupby('gender').rating.apply(pd.Series.std))


df1 =rating_df.groupby(['user id','gender']).apply(np.mean)
print(type(df1))
print(df1.groupby('gender').rating.std())

print(pd.pivot_table(df1,values= 'rating',index ='gender',aggfunc =pd.Series.std))
table = pd.pivot_table(rating_df,index = ['user id','gender'],values = 'rating')
female = table.query("gender == ['F']")
print(pd.Series.std(female))