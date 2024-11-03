import csv

""" with open("ders5 csv_files/arabalar.csv","w",newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Marka","Model","MaxSpeed"])
    csv_writer.writerow(["Toyota","Corolla",300])
    csv_writer.writerow(["Mazda","CX-5",400])
    
    # if we wanna add multiple rows hepsini bi liste içine al oldu bitti
    csv_writer.writerows([["Toyota","Corolla",300],["Toyota","Corolla",300],["Toyota","Corolla",300]]) """
    
# ekleme yapma    
""" with open("ders5 csv_files/arabalar.csv","a",newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["porche","chaiman","900"])
    csv_writer.writerow(["mercedes","cl 63","2000"])
    csv_writer.writerow(["honda","civic","1000"])
 """
# bi dosyadan aldığımız bilgileri farklı dosyaya yazma

""" with open("ders5 csv_files/arabalar.csv") as file:
    reader = csv.reader(file)
    with open ("ders5 csv_files/arabalar_two.csv" , "w", newline= "") as new_data:
        writer = csv.writer(new_data)
        for row in reader:
            writer.writerow(row) """

with open("ders5 csv_files/arabalar.csv", "r+", newline="") as file:
    # we use new line character cause we dont wanna see empty blank lines7
    writer = csv.writer(file, quoting=csv.QUOTE_NONE)
    reader = csv.reader(file)
    next(reader)
    # başlıkları okumasın diye
    cars = [[car[0],car[1],car[2]] for car in reader]
    file.seek(0) # bunu yamazsan ekleme yapar sanırım 
    writer.writerow(["Marka,Model,MaxSpeed"])
    writer.writerows(cars)