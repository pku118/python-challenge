#Read the CSV File
import os
import csv

# Lists to store data
total_pandl = 0 
pandl_changes = []
prior_pandl = 0
total_months = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]


#Path of csv file. 
budget_csv = os.path.join("PyBank","Resources", "budget_data.csv")

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)

#Read the Header Row and Skip Header Row
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

# Read each row of data after the header
    for row in csv_reader:
        
        #Total Months Count update
        total_months += 1
        
        #total P and L update
        total_pandl += int(row[1])
        
        #Profit/Loss Month to month
        pandl_change = int(row[1]) - prior_pandl
        if prior_pandl != 0:
            pandl_changes.append(pandl_change)

        prior_pandl = int(row[1])

        # Calc greatest increase and decrease
        if pandl_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = pandl_change

        if pandl_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = pandl_change   

avg_change = sum(pandl_changes) / len(pandl_changes)

print("--------------------------------")
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {total_months}")
print(f"Total : ${total_pandl}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")  

#Output to CSV
with open('analysis.csv', mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${total_pandl}"])
    csvwriter.writerow([f"Average Change: ${round(avg_change, 2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"])