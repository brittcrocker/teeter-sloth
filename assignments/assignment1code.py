import csv
# Open our input and output files
csvfile = open('./cleanme.csv', 'r')
outfile = open('./assignment1-clean.csv', 'w')

#now a dictreader and dictwriter
#dictreader and dictwriter are imported libraries

reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)
#dictwriter writes to outfile
#reader.fieldname refers to the headers

#write headers
writer.writeheader()

#clean and write the data to output
for row in reader: 
    row['first_name'] = row['first_name'].upper()
    row['zip'] = row['zip'].zfill(5)
    row['city'] = row['city'].replace('&nbsp'," ")
    if float (row['amount']) > 1000.0:
        writer.writerow(row)

