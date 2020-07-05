from csv import writer,reader, DictWriter, DictReader

filename = "./fighthers.csv"

#with open(filename,"a") as file:
#    csv_writer = writer(file)
#    csv_writer.writerow(["Jhosua","Usa","192"])
#    csv_writer.writerow(["Mike","Usa","189"])

def cm_to_in(cm):
    return float(cm) * 0.393701

with open(filename) as file:
    csv_reader = reader(file)
    next(csv_reader)
    with open(filename, "w") as file:
        csv_writer = writer(file)
        csv_writer.writerow(["name", "country","height"])
        for row in csv_reader:
            csv_writer.writerow([fighter.upper() for fighter in row])

with open(filename) as file:
    csv_reader = DictReader(file)
    with open("fighthers_inches.csv", "w") as file:
        csv_writer = DictWriter(file, fieldnames=csv_reader.fieldnames)
        csv_writer.writeheader()
        for row in list(csv_reader):
            csv_writer.writerow({
                csv_writer.fieldnames[0]: row[csv_writer.fieldnames[0]],
                csv_writer.fieldnames[1]: row[csv_writer.fieldnames[1]],
                csv_writer.fieldnames[2]: cm_to_in(row[csv_writer.fieldnames[2]])
            })


with open("cats.csv", "w") as file:
    headers = ["name", "breed", "age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()

    csv_writer.writerow({
       "name":"Garfield",
       "breed": "Orange Tabby",
       "age": 10
    })



