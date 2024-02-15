#Read the CSV File
import os
import csv

# Variables
total_votes = 0 
candidate = {}
winner = ""
win_votes = 0 

#Path of csv file. 
election_csv = os.path.join("PyPoll","Resources", "election_data.csv")

#open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")


#Read the Header Row and Skip Header Row
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

# Read each row of data after the header
    for row in csv_reader:
        
        #Total vote Count update
        total_votes += 1
        
        #total votes per candidate
        candidate_name = row[2]
        if candidate_name in candidate:
            candidate[candidate_name] += 1
        # If candidate is not in dictionary, add them with one vote
        else:
            candidate[candidate_name] = 1
        
# Who is the winner
for candidates, votes in candidate.items():
    if votes > win_votes:
        winner = candidates
        win_votes = votes

# Calculate the percentage of votes for each candidate
for candidates, votes in candidate.items():
    percentage = (votes / total_votes) * 100
    candidate[candidates] = (percentage, votes)

# Print the analysis to the terminal
print("Election Results")
print("------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------")
for candidates, (percentage, votes) in candidate.items():
    print(f"{candidates}: {percentage:.3f}% ({votes})")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")

# Export the results to a text file
output_file = "election_results.txt"
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("------------------------------\n")
    for candidates, (percentage, votes) in candidate.items():
        txtfile.write(f"{candidates}: {percentage:.3f}% ({votes})\n")
    txtfile.write("------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("------------------------------\n")