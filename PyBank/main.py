# This is for PyBank analysis activity

#add in dependencies
import pandas as pd
import os
import csv

#Define variables for PyBank calculations
months = []
profit_loss_deltas = []

month_count = 0
net_profit_loss = 0
past_month_loss = 0
current_month_loss = 0
profit_loss_delta = 0


#collects data from Resources directory
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#opens and reads csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reads the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

 # Read each row after the header row
    for row in csvreader:
       
        # Counts months in file
        month_count += 1 

        #Calculate net profits and losses over time period
        current_month_loss = int(row[1])
        net_profit_loss += current_month_loss

        if (month_count == 1):
            #Makes value of last month equal to the current
            past_month_loss = current_month_loss
        continue

    else:

        #Calculate change in loss of profit
        profit_loss_delta = current_month_loss - past_month_loss

        #Append each month to variable month[]
        months.append(row[0])

        # Append each profit_loss_change to the profit_loss_changes[]
        profit_loss_deltas.append(profit_loss_delta)

        # Make the current_month_loss to be past_month_profit_loss for the next loop
        past_month_loss = current_month_loss

    #Sum and find the average of the delta in profits and losses over the whole period
    sum_profit_loss = sum(profit_loss_deltas)
    average_profit_loss = round(sum_profit_loss/(month_count - 1), 2)

    # highest and lowest delta in profits and lossees over the whole period
    highest_delta = max(profit_loss_deltas)
    lowest_delta = min(profit_loss_deltas)

    
    #Find the index value of highest and lowest delta profits and lossees over the whole period
    highest_month_index = profit_loss_deltas.index(highest_delta)
    lowest_month_index = profit_loss_deltas.index(lowest_delta)

    # Determine best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]


# Prints to terminal analysis of PyBank
    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months:  {month_count}")
    print(f"Total: ${net_profit_loss}")
    print(f"Average Change: ${average_profit_loss}")
    print(f"Greatest Increase in Profits: {best_month} (${highest_delta})")
    print(f"Greatest Decrease in Profits: {worst_month} (${lowest_delta})")

# Exports the analysis results to a .txt file
    Pybank_file = os.path.join("Analysis", "Pybank_data.txt")
    with open(Pybank_file, "w") as outfile:

     outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {month_count}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_delta})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_delta})\n")