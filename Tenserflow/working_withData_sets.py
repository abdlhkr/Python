import pandas as pd

dataFrame = pd.read_csv("/home/karakuzey/Desktop/PythonTenserflow/Tenserflow/listings.csv")
# verideki column name leri yazdırmak için columns kullanılır
# kaç veri var 
print(len(dataFrame)) # bu kadar hızlı çalışması ilginc
print(dataFrame.columns)
filtered_data = dataFrame[(dataFrame["number_of_reviews"] >= 1000) & (dataFrame["price"] <= 200)]
# print(filtered_data)
filtered_columns = filtered_data[["name", "review_scores_rating","price"]]
print(filtered_columns)

# istanbuldaki evleri ve fiyatlarını yazdırmak için
istanbul_data = dataFrame[(dataFrame["number_of_reviews"] >= 1000) & (dataFrame["price"] <= 2000) & (dataFrame["latitude"] == 41.0082) & (dataFrame["longitude"] == 28.9784)&(dataFrame["instant_bookable"] == "True")]
# anlaşılan istanbulda pek popüler değil
print(istanbul_data[["name", "review_scores_rating","price"]])
