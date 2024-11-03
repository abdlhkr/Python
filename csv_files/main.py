import csv 
# this time course shows without pandas libary
with open("ders5 csv_files/example.csv","r") as file:
    """ print(file.read()) """
    # even it works we cant get just one column or row
    csv_file = csv.reader(file)
    
    print(csv_file) # thats an object and its iterable so
    for item in csv_file:
        if item[3] == "True":
            print(item)
            
# dict reader for taking values as a dict            