import csv

file_to_load = "Resources/budget_data.csv"
file_to_output = "Analysis/Revenue_txt"

total_months = 0
total_revenue = 0
previous_revenue = 0
month_of_change = []
revenue_change_list = []
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
        previous_revenue = int(row["Profit/Losses"]) 
        revenue_change_list = revenue_change_list+[revenue_change]
        month_of_change = month_of_change + [row['Date']]
# Greatest Increase
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
# Greatest Decrease
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# revenue_avg
revenue_avg = sum(revenue_change_list)/len(revenue_change_list)
output = (
    '\nFinancial Analysis\n' +
    '-----------------------------\n'+
    'Total Months: {}\n'.format(total_months) +
    'Total Revenue: {}\n'.format(total_revenue) +
    'Average Revenue Change: {}\n'.format(revenue_avg) +
    'Greatest Increase in Revenue: {} $({})\n'.format(greatest_increase[0],greatest_increase[1]) +
    'Greatest Decrease in Revenue: {} $({})\n'.format(greatest_decrease[0],greatest_decrease[1])
)

print(output)

with open (file_to_output, 'w') as txt_file:
    txt_file.write(output)