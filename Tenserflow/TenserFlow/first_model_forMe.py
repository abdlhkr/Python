import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.models import Sequential

pandasFrame = pd.read_csv("TenserFlow/gym_members_exercise_tracking.csv")
print(pandasFrame.columns)
print(pandasFrame.head())


egitimSeti = pandasFrame[["Age","Weight (kg)","Height (m)","Workout_Frequency (days/week)","Max_BPM","Avg_BPM","Experience_Level"]].values
sonucSeti = pandasFrame["Calories_Burned"].values

train_egitim , test_egitim , train_sonuc , test_sonuc = train_test_split(egitimSeti,sonucSeti,test_size=0.33,random_state=15)
sclaler = MinMaxScaler()
sclaler.fit(train_egitim)
train_egitim = sclaler.transform(train_egitim)
test_egitim = sclaler.transform(test_egitim)
# şu an verileri hazırladık scale ettik model kurma zamanı 
# 4 veri girişi olduğu için input_shape=(4,) dedik
model = Sequential()
model.add(Dense(4,activation='elu',input_shape=(7,)))
model.add(Dense(7,activation='elu'))
model.add(Dense(7,activation='elu'))
model.add(Dense(7,activation='elu'))
model.add(Dense(7,activation='elu'))
model.add(Dense(7,activation='elu'))
model.add(Dense(7,activation='elu'))
model.add(Dense(7,activation='elu'))
model.add(Dense(1))

model.compile(optimizer='adam',loss='mse')
model.fit(train_egitim,train_sonuc,epochs=250)

plt.plot(model.history.history['loss'], label='Train Loss')
plt.title('Model Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()


train_loss =  model.evaluate(train_egitim,train_sonuc,verbose = 0)
test_loss = model.evaluate(test_egitim,test_sonuc,verbose=0)

print(f"train loss : {train_loss} , test loss : {test_loss}")

tahmini_sonuc = model.predict(test_egitim)
plt.scatter(test_sonuc,tahmini_sonuc)
plt.xlabel('Gerçek Sonuç')
plt.ylabel('Tahmini Sonuç')
plt.title('Gerçek ve Tahmini Sonuçlar')
plt.show()

# bun modelde normalde işleme katmadığım çok fazla değişken olduğu için
# modelin doğruluğu biraz düşük oldu ama şimdilik bu şekişlde devam edelim
# girdi olarak parametre ekledikçe modelin doğruluğu artıyor
sonuc_Frame = pd.DataFrame(test_sonuc,columns=['Gerçek Sonuç'])
tahmini_Frame = pd.DataFrame(tahmini_sonuc,columns=['Tahmini Sonuç'])
dataFrame = pd.concat([sonuc_Frame,tahmini_Frame],axis=1)
print(dataFrame.head())