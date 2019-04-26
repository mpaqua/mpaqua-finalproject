import csv, json

infile = open("data.json","r")
outfile =open("culturedata.csv","w")
writer = csv.writer(outfile)
for row in json.loads(infile.read()):
    #a_row=[]
    print (row["cultures"])
    for c in row["cultures"]:
        #a_row.append(row["objectnumber"])
        #a_row.append(c)
        #writer.writerow(a_row)
        writer.writerow([c])




#_______________________________________________________
