import csv, json

#Wrote a CSV file with information from data.json
infile = open("data.json","r")
outfile =open("map.csv","w")
writer = csv.writer(outfile)

#Added a row with  headings
writer.writerow(["Culture"])
all_cultures=[]
for row in json.loads(infile.read()):

#Changed format of culture names to match style used by Native-Lands.ca
    for c in row["cultures"]:
        c = c.lower()
        c = c.replace(' ','-')
        all_cultures.append(c)
        #a_row.append(c)
all_cultures= list(set(all_cultures))
url =",".join(all_cultures)
print(url)
for eachc in all_cultures:
    writer.writerow([eachc])
