
import csv, json

#Wrote a CSV file with information from data.json
outfile =open("dataviz.csv","w")
infile = open("data.json","r")
writer = csv.writer(outfile)

#Added a row with headings
writer.writerow(["Object Number", "Title", "Provenance"])

#Identified just the latest entry in the provenance row - year of accession
for row in json.loads(infile.read()):
    years = list(map(int,row["provenance"]))
    if len(years)>0:
        biggestyear=max(years)
    else:
        biggestyear = "Null"
    a_row=[]

#Wrote the remaining rows
    a_row.append(row["objectnumber"])
    a_row.append(row["title"])
    a_row.append(row["cultures"])
    a_row.append(biggestyear)
    writer.writerow(a_row)
