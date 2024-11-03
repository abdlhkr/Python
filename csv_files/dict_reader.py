import csv
with open("ders5 csv_files\example.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    print(csv_reader)
    total = 0
    for item in csv_reader:
        print(f"ürün adı : " +item["ProductName"] + f" fiyatı = {item["Price"]}")    
        
        