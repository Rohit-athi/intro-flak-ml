import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data ={
    "age" : [1,2,3,1,4,5,2,6,3,5,6,3],
    "size" : [500,700,800,
            1000,1100,1250,
            900,2000,1750,
            2000,2200,1100],
    "price" : [5000,7000,9000,10000,11000,13000,9500,20000,19000,21000,25000,12000]
}
df=pd.DataFrame(data)
# print(df)
x = df.drop(columns=['price'])
y = df['price']
model = LinearRegression()
model.fit(x,y)
pickle.dump(model,open('model1.pkl','wb'))