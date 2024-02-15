import csv

# Define the path to the CSV file
file_path = ("PyPoll","Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)
    
    # Count the total number of votes and calculate votes for each candidate
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        
        # If candidate is already in dictionary, increment their vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        # If candidate is not in dictionary, add them with one vote
        else:
            candidates[candidate_name] = 1

# Find the winner
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Calculate the percentage of votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (percentage, votes)

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, (percentage, votes) in candidates.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_file = "election_results.txt"
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, (percentage, votes) in candidates.items():
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"Results have been exported to {output_file}")
