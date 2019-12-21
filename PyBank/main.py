import csv

file_to_load = "Resources/budget_data.csv"
file_to_output = "Analysis/Revenue_txt"

total_months = 0
total_revenue = 0
previous_revenue = 0
#* The average of the changes in "Profit/Losses" over the entire period
average_change = []
# Greatest Increase in Profits: Feb-2012 ($1926159)
greatest_increase = ["",0]
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
greatest_decrease = ["",9999999999999]

with open(file_to_load) as financial_data:
    reader=csv.DictReader(financial_data)

    for row in reader:
        total_months += 1
        total_revenue = int(row["Profit/Losses"])
# Revenue Change
        revenue_change = int(row["Profit/Losses"]) - previous_revenue
        previous_revenu = int(row["Profit/Losses"]) 
        average_change = average_change + [row['Date']]
# Greatest Increase
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
# Greatest Decrease
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# revenue_avg

output = (
    f'Total Months: {total_months}'
)

print(output)