import json
import csv


#input data file containing all the stuff
dataFileName = "glintWS/data/BengalElection2021Replies.csv"
data = []
outputFileName = "glintWS/data/bengal_election_2021_replies.csv"

with open (dataFileName) as f:
        for line in f:
            data.append(json.loads(line))


# now we will open a file for writing
data_file = open(outputFileName, 'w')
 

# create the csv writer object
csv_writer = csv.writer(data_file, delimiter ='\t',quoting=csv.QUOTE_MINIMAL)
print("Printing headers for inspection")
print(data[0].keys())

csv_writer.writerow(data[0].keys())

for row in data:
    csv_writer.writerow(row.values())
data_file.close()