#PyPoll Python code to election analysis

# Import dependencies
import os
import csv
import collections
from collections import Counter

# Define variables for PyPoll's activity
candidate_votes = []
votes_per_candidate = []

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    #print(f"Header: {csv_header}")
    
    # Reads data from each row that after the header
    for row in csv_reader:

        candidate_votes.append(row[2])

    # Sort the (ascending)
    sorted_list = sorted(candidate_votes)

    #sorted_list = sorted(candidate_votes, reverse=True) 
    #sorted_list.sort(reverse=True) 

    #for key, group in groupby(sorted_list):
    
    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    #count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # calculate the percentage of votes per candicate in 3 digital points
    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
      #  fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
          
    # print(c.most_common())
    #print(c.values())
    
    
# -->>  Prints the outcome results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


# -->>  Exports results to a .txt file in Analysis folder
election_results = os.path.join("Analysis", "election_results.txt")
with open(election_results, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    outfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    outfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    outfile.write("-------------------------\n")  
