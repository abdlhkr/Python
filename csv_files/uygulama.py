import csv 
# online food dosyası üzerinde
# 1) online yemek siparişi veren kaç lişi var ? 

# 3) 20 - 30 yaş arası konum listesi

with open("ders5 csv_files\onlinefoods.csv") as file:
    reader = csv.reader(file)
    people = list(reader)
    population = len(people) -1
    print(population)
    
# 2) öğrencileri listeleyin
with open("ders5 csv_files\onlinefoods.csv") as file:
    reader = csv.DictReader(file)
    people = list(reader)
    with open("ders5 csv_files\ogrenci.csv","w",newline="") as new_file:
        headers = ["Age","Martial Status","Occupation","Monthly Income","Educational Qualifications"]
        writer = csv.DictWriter(new_file,headers)
        for person in people:
            if person["Occupation"] == "Student":
                writer.writerow({
                    "Age" : person["Age"],
                    "Martial Status": person["Marital Status"],
                    "Occupation" : person["Occupation"],
                    "Monthly Income" : person["Monthly Income"],
                    "Educational Qualifications" : person["Educational Qualifications"]
                })

# 20-30 yaş arası konum bilgisi :         
with open("ders5 csv_files\onlinefoods.csv") as file:
    reader = csv.DictReader(file)
    people = list(reader)
    counter = 1
    for person in people:
        if  20 <= int(person["Age"]) <= 30:
            print(f"{counter} latitude : {person["latitude"]} ,longitude : {person["longitude"]}")
            counter += 1