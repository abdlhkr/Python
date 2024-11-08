from pandas_ods_reader import read_ods
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.models import Sequential
# import seaborn as sbn
import pandas as pd

# ods file ları pandas ile kullanabilmek için 
# pandas_ods_reader kütüphanesini kullanıyoruz.

pandasFrame = read_ods("TenserFlow/cycle.ods", 1)
print(pandasFrame.head())
# head parametre verilmezse ilk 5 satırı getirir.
#  sayı verirsek o kadar satır getirir
# sbn ile grafik görselleştirme
# sbn.pairplot(pandasFrame)
# plt.show()


# veriyi test ve train olarak ayırma

# y = mx + b
# y = label fiyat
y = pandasFrame['Fiyat'].values
# x feature (özellik) 
x = pandasFrame[["BisikletOzellik1","BisikletOzellik2"]].values
# burda x i özellikler y yi ise label yani fiyat olarak ayırdık
# train_test_split fonksiyonu ile veriyi rasgele ikiye ayırıyoruz
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.33,random_state=15)
print(x_train.shape) 
print(x_test.shape)
print(y_train.shape)    
print(y_test.shape)

# scaler nöronlara vereceğimiz değerleri 1 - 0 arasında olmasını sağlar
# bu sayede nöronlar daha iyi ve hızlı öğrenir
scaler = MinMaxScaler()
scaler.fit(x_train) # fit max mini bulur scaler buna göre 1, 0 arasına koyar
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
# print(x_train)
# print(x_test)

# MODEL OLUŞTURMA VE KATMAN EKLEME
model = Sequential()
# bağımısız olarak bisiklet özellik1 ve 2 oolmak üzere iki özellik var 
# bu yüzden her katmanda 2 nöron ayarladık daha fazla olabilir
model.add(Dense(4, activation='elu', input_shape=(2,)))  # 2 giriş özelliği olduğu için input_shape=(2,)
# yukarıda tanımladığım katman normalde otomatik ayarlanır ama biz belirttik
model.add(Dense(8,activation='elu'))
model.add(Dense(8,activation='elu'))
model.add(Dense(8,activation='elu'))
model.add(Dense(1)) # çıkış katmanı
model.compile(optimizer='adam',loss='mse')
model.fit(x_train,y_train,epochs=400)


plt.plot(model.history.history['loss'], label='Train Loss')
plt.title('Model Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()
# bu durumda bile hata olarak oldukça iyi sonuçlara ulaştık katman sayısını
# değitirmeden nöron sayısını değiştirerek tekrar deneyelim
# modelin basitliğinden yada epochs sayısından kaynaklı olabilir çok değişmedi
# evet burda epochs sayısı katman sayısı ve nöron sayısı aldığımız sonucu pek
# etkilemedi bunun sebebi veri sayısının azlığı yada modelin basitliği olabilir
train_loss =  model.evaluate(x_train,y_train,verbose = 0)
test_loss = model.evaluate(x_test,y_test,verbose=0)

print(f"train loss : {train_loss} , test loss : {test_loss}")

real_value = pd.Series(y_test)

prediction = model.predict(x_test)
print(f"""gerçek değer shape i : {real_value.shape} : {type(real_value)}
      prediction shape : {prediction.shape} : {type(prediction)}""")

prediction = pd.Series(prediction.reshape(330,))
print(f"gerçek değer : {real_value}")
print(f"tahmin değer : {prediction}")

dataFrame = pd.DataFrame({'Gerçek Değer':real_value,'Tahmin Değer':prediction})
print(dataFrame.head())
# plt.scatter(real_value,prediction)
# plt.xlabel("Gerçek Değer")
# plt.ylabel("Tahmin Değer")
# plt.title("Gerçek Değer ve Tahmin Değer")
# plt.show()


