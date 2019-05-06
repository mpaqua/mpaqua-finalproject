import csv, json

#Wrote a CSV file with information from data.json
infile = open("data.json","r")
outfile =open("culture.csv","w")
writer = csv.writer(outfile)

#Wrote a header row
writer.writerow(["Object Number", "Culture"])
for row in json.loads(infile.read()):
    a_row=[]

#Added rows for object numbers and the cultures from which those objects came from
    for c in row["cultures"]:
        a_row.append(row["objectnumber"])
        a_row.append(c)
        writer.writerow(a_row)
