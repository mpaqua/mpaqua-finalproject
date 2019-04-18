import csv, json

infile = open("data.json","r")
outfile =open("data2.csv","w")
writer = csv.writer(outfile)
for row in json.loads(infile.read()):
    writer.writerow(row)

#_______________________________________________________
