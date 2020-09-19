import os
import csv

budget_csv = os.path.join(".", "Resources", "budget_data.csv")

months = []
profit_losses = []
profit_change = []
greatest_increase = []
greatest_decrease = []
dates = []
with open(budget_csv, "r") as csv_file: 
     reader = csv.reader(csv_file, delimiter=",")
     csv_header = next(reader)
     
     for p_l in reader:
         profit_losses.append(int(p_l[1]))
         months.append(str(p_l[0]))

     for p_c in range(len(profit_losses)-1):
         profit_change.append(profit_losses[p_c + 1] - profit_losses[p_c]) 

     
t_months = len(months)
sum_profit_losses = sum(profit_losses)
average_change = round(sum(profit_change) / len(profit_change),2)

max_profit_increase = max(profit_change)
greatest_profit_decrease = min(profit_change)
months[profit_change.index(max_profit_increase)+1]
months[profit_change.index(greatest_profit_decrease)+1]

max_profit_increase = max(profit_change)
greatest_profit_decrease = min(profit_change)
month_max_profit_increase = months[profit_change.index(max_profit_increase)+1]
month_greatest_profit_decrease = months[profit_change.index(greatest_profit_decrease)+1]


print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {t_months}")
print (f"Total: {sum_profit_losses}")
print (f"Average Change: {average_change}")
print (f"Greatest Increase in Profits: {max_profit_increase}")
print (f"Greatest Decrease in Profits: {greatest_profit_decrease}")
print (f"Greatest Increase in Profits: {month_max_profit_increase} (${max_profit_increase})")
print (f"Greatest Decrease in Profits: {month_greatest_profit_decrease} (${greatest_profit_decrease})")


#to print to a text file 
text_output = (
    "Financial Analysis\n"
    "---------------------------------------\n"
f"Total Months: {t_months}\n"
f"Total: {sum_profit_losses}\n"
f"Average Change: {average_change}\n"
f"Greatest Increase in Profits: {max_profit_increase}\n"
f"Greatest Decrease in Profits: {greatest_profit_decrease}\n"
f"Greatest Increase in Profits: {month_max_profit_increase} (${max_profit_increase})\n"
f"Greatest Decrease in Profits: {month_greatest_profit_decrease} (${greatest_profit_decrease})\n"
)

file = os.path.join(".", "Analysis", "PyBank_analysis.txt")
with open (file, "w") as text: 
    text.write(text_output)
    text.close     






