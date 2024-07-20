import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd



if __name__ == '__main__':
    timeCharged = float(input().strip())
    df = pd.read_csv('trainingdata.txt', header = None)


# In[215]:


    df.head()


    # In[216]:


    from matplotlib import pyplot as plt


    # In[217]:


    plt.scatter(df.iloc[:,:1],df.iloc[:,-1])
    plt.xlabel('Time')
    plt.ylabel('Battery')


    # In[218]:


    df[df[1]>= 8].min()


    # In[226]:


    from sklearn.linear_model import Ridge, LinearRegression
    from sklearn.metrics import r2_score
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler

    df = df[df[0]<4.11]
    plt.scatter(df.iloc[:,:1],df.iloc[:,-1])
    plt.xlabel('Time')
    plt.ylabel('Battery')
    X = df.iloc[:,:1]
    y = df.iloc[:,-1]
    #print('X',X.shape)
    #print('y',y.shape)
    X_train, X_test, y_train, y_test = train_test_split(X,y,train_size = 0.8)
    X_train = X_train.to_numpy()
    X_test = X_test.to_numpy()
    y_train = y_train.to_numpy()
    y_test = y_test.to_numpy()
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    poly = PolynomialFeatures(degree = 1)
    X_train = poly.fit_transform(X_train)
    X_test = poly.transform(X_test)
    #print('X_train',X_train.shape)
    #print('X_test',X_test.shape)
    #model = Ridge(alpha = 0.0089)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)
    y_hat = model.predict(X_test)
    #print('Training score is: {:.2f}'.format(r2_score(y_train, y_pred)))
    #print('Test score is: {:.2f}'.format(r2_score(y_test, y_hat)))


    # In[230]:


    inp = timeCharged
    if inp >= 4.11:
        print(8)
    else:
        X_ = scaler.transform(np.array([[inp]]))
        X_poly = poly.transform(X_)
        print('{:.2f}'.format(model.predict(X_poly)[0]))


    # In[ ]: