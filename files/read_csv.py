from csv import reader

filename = "fighthers.csv"

with open("./"+filename) as file:
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
       print(f"Figther: {row[0]}\nFrom: {row[1]}\nHeight:{row[2]}\n")
        

from csv import DictReader

with open("./"+filename) as file:
    csv_dict = DictReader(file)
    for row in csv_dict:
        print(f"Fighther: {row['name']}\nFrom: {row['country']}\nHeight: {row['heigth (in cm)']}\n")
