import csv
with open('name.csv', 'r') as file:
    reader = csv.reader(file , delimiter ='\t')
    for row in reader:
        print(row)
          
