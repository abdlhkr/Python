import csv
with open("ders5 csv_files/arabalar_two.csv","a",newline="") as file:
    headers = ["Marka","Model","MaxSpeed","angala saksonlar"]
    writer = csv.DictWriter(file,headers)
    writer.writeheader()
    writer.writerow({
        "Marka" : "Koenigsegg",
        "Model" : "Jesko Absolut",
        "MaxSpeed" : 9999
    })
    
with open("ders5 csv_files/arabalar_two.csv") as file:
    csv_reader = csv.DictReader(file)
    cars = list(csv_reader)
    with open("ders5 csv_files/arabalar_three.csv","w",newline="") as new_file:
        header = ["Marka","Model","MaxSpeed","angala saksonlar"]
        writer = csv.DictWriter(new_file,header)
        writer.writeheader()
        for car in cars:
            writer.writerow({
                "Marka" : car["Marka"],
                "Model" : car["Model"],
                "MaxSpeed" : car["MaxSpeed"]
            })