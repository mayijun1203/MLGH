import pandas as pd  
import numpy as np
import sklearn.model_selection
import keras



df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/logistic regression/bank.csv',sep=';')
df['deposit']=np.where(df['y']=='yes',1,0)
df['default']=np.where(df['default']=='yes',1,0)
df['housing']=np.where(df['housing']=='yes',1,0)
df['loan']=np.where(df['loan']=='yes',1,0)
df=df[['deposit','age','default','balance','housing','loan','campaign']].reset_index(drop=True)




# Keras
xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['age','default','balance','housing','loan','campaign']],df['deposit'],test_size=0.2)
xtrain,xval,ytrain,yval=sklearn.model_selection.train_test_split(xtrain,ytrain,test_size=0.25)
nn=keras.models.Sequential()
nn.add(keras.layers.Dense(units=12,input_dim=6,activation='relu'))
nn.add(keras.layers.Dense(units=1,activation='sigmoid'))
nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
nn.fit(xtrain,ytrain,epochs=150,batch_size=10)

ypred=pd.DataFrame({'val':ytrain,'prob':[x[0] for x in nn.predict(xtrain)],'pred':[x[0] for x in nn.predict_classes(xtrain)]})
_,accuracy=nn.evaluate(xtrain,ytrain)
print('Accuracy: %.2f' % (accuracy*100)+'%')

ypred=pd.DataFrame({'val':yval,'prob':[x[0] for x in nn.predict_proba(xval)],'pred':[x[0] for x in nn.predict_classes(xval)]})
_,accuracy=nn.evaluate(xval,yval)
print('Accuracy: %.2f' % (accuracy*100)+'%')

ypred=pd.DataFrame({'val':ytest,'prob':[x[0] for x in nn.predict_proba(xtest)],'pred':[x[0] for x in nn.predict_classes(xtest)]})
_,accuracy=nn.evaluate(xtest,ytest)
print('Accuracy: %.2f' % (accuracy*100)+'%')













