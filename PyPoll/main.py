import os
import csv

election_csv = os.path.join (".","Resources", "election_data.csv")

voter_ID = []
County = []
Candidate = []


with open(election_csv, "r") as csv_file: 
    reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(reader)

    for row in reader:
        t_voters = (voter_ID.append(row[0]))  




print("Election Results")
print("-----------------------------------------")
print(len(voter_ID))
print(f"Total Votes: {t_voters}")
