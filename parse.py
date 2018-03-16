import csv

years = []
life = []

with open('rates.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter = "," )
    for row in reader:
        print row[0]
        years.append(row[0])
        life.append(row[3])

str = '['
for age in life:
    str += age + ', '

str += ']'
print str

str = '['
for x in years:
    str += x +", "

str += ']'
print str