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
        voter_ID.append(row[0])

        Total_votes = len(voter_ID)  

        candidate = row[2]

        if candidate not in Candidate_list: 
            Candidate_list.append(candidate)
        if candidate not in Vote_count: 
            Vote_count[candidate] = 1
        else:
            Vote_count[candidate] = Vote_count[candidate] + 1
    
    
winner = max(Vote_count.values())
for key, value in Vote_count.items():
    if value == winner:
        most_votes = key
        break

candidate_info = " "
for candidate in Candidate_list: 
    Vote_percentage = (Vote_count[candidate] / len(voter_ID) * 100)
    candidate_info +=(f"{candidate}: {Vote_percentage:.3f}% ({Vote_count[candidate]})\n")
    
    
print("Election Results")
print("-----------------------")
print(f"Total Votes: {Total_votes}")
print("-----------------------")
print(candidate_info,"-----------------------") 
print(f"Winner: {most_votes}")  
print("-----------------------")  

#to print to a text file
text_output = (
    "Election Results\n"
    "-----------------------\n"
f"Total Votes: {Total_votes}\n"
    "-----------------------\n"
f"{candidate_info}-----------------------\n" 
f"Winner: {most_votes}\n"  
    "-----------------------\n" 
)

file = os.path.join(".", "Analysis", "PyPoll_analysis.txt")
with open (file, "w") as text: 
    text.write(text_output)
    text.close
    








