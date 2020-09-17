import os
import csv

budget_csv = os.path.join(".", "Resources", "budget_data.csv")

months = []
profit_losses = []
profit_change = []
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


print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {t_months}")
print (f"Total: {sum_profit_losses}")
print (f"Average Change: {average_change}")
print (f"Greatest Increase in Profits: {max_profit_increase}")
print (f"Greatest Decrease in Profits: {greatest_profit_decrease}")

    #  net = []
    #  for row in reader:
    #     net = column [1]
    #     total += value
    #     print(f"Total: {net}")


#for profits_losses in reader: 
# with open(budget_csv, "r") as csv_file: 
#     total = 0
#     for profits_losses in reader:
#         #with open(budget_csv, "r") as csv_file:
#         next(reader)
#         value = column [1]
#         total += value
#         print(f"Total: {profits_losses}")

#     reader = csv.reader(csv_file, delimiter=",")
#     next(reader)
#     profits_losses = sum(list(reader))
#     print(f"Total: {profits_losses}") 



# for months in budget_csv: 


#      months = str(budget_csv[0])
#      profits_losses = int(budget_csv[1])

     

#      headers = next(reader)
#      print(headers)

# def financial_analysis(budget_data):

#     months = str(budget_data[0])
#     profits_losses = int(budget_data[1])

#     total_months = len(months)
#     print(total_months)

#     print(f"Total Months: {str(total_months)}")





