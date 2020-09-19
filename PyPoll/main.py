import os
import csv

election_csv = os.path.join (".","Resources", "election_data.csv")

voter_ID = []
Candidate_list = []

Vote_count = {}

with open(election_csv, "r") as csv_file: 
    reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(reader)

    for row in reader:
        t_voters = (voter_ID.append(row[0]))  
        
        
    candidate = row[2]    
    for row in reader:
        if candidate not in Candidate_list: 
            Candidate_list.append(candidate)
        if candidate not in Vote_count: 
            Vote_count[candidate] = 1
        else:
            Vote_count[candidate] = Vote_count[candidate] + 1

    for candidate in Candidate_list: 
        print((candidate, Vote_count[candidate], Vote_count[candidate] / len(voter_ID)) * 100)  

    
print("Election Results")
print("-----------------------------------------")
print(len(voter_ID))

