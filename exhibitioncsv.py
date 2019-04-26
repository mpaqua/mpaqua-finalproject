
import csv, json

infile = open("data.json","r")
outfile =open("exhibitiondata.csv","w")
writer = csv.writer(outfile)
for row in json.loads(infile.read()):
    a_row=[]
    a_row.append(row["exhibitions"])
    writer.writerow(a_row)
