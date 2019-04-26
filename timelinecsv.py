
import csv, json
import pandas as pd
outfile =open("timeline.csv","w")
infile = open("data.json","r")
writer = csv.writer(outfile)
for row in json.loads(infile.read()):
    writer.writerow(["Object Number", "Date", "Provenance"])
    a_row=[]
    for c in row["provenance"]:
        a_row.append(row["objectnumber"])
        a_row.append(row["datecreated"])
        a_row.append(c)
        writer.writerow(a_row)
        file_name="timeline.csv"
        file_name_output ="timeline_without_dupes.csv"
        df = pd.read_csv(file_name, sep="\t or ,")
        df.drop_duplicates(subset=None, inplace=True)
        df.to_csv(file_name_output)
