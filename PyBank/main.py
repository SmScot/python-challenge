import os
import csv

budgetdata_csv = os.path.join("Resources", "budget_data.csv")

# lists to store data
Months = []
ProfitLoss_total = []
ProfitLoss_change = []

#open as csvfile
with open(budgetdata_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#start loop from second row
    next(csv_reader)

    for line in csv_reader:
        
        Months.append(line[0])
        ProfitLoss_total.append(line[1])

total_months = len(Months)
print(total_months)

for i in range(0, len(ProfitLoss_total)):
    ProfitLoss_total[i] = int(ProfitLoss_total[i])

Profit = sum(ProfitLoss_total)
print(Profit)

for i in range(1, len(ProfitLoss_total)):    
    ProfitLoss_change.append(ProfitLoss_total[i]-ProfitLoss_total[i - 1])
print(ProfitLoss_change)

Ave_Change = round(sum(ProfitLoss_change)/(total_months - 1), 2)
print(Ave_Change)

max_change = max(ProfitLoss_change)
print(max_change)

min_change = min(ProfitLoss_change)
print(min_change)

i_max = ProfitLoss_change.index(max_change)
date_max = Months[i_max + 1]
print(date_max)

i_min = ProfitLoss_change.index(min_change)
date_min = Months[i_min + 1]
print(date_min)

Results = (f"Financial Analysis\n------------------\nTotal Months: {len(Months)}\nNet Total: ${Profit}\nAverage Change: ${Ave_Change}\nGreatest Increase in Profits: {date_max} (${max_change})\nGreatest Decrease in Profits: {date_min} (${min_change})")
print(Results)

text_path = os.path.join("Analysis", "Results.txt")
file = open(text_path, "w")
file.write(Results)
file.close()


