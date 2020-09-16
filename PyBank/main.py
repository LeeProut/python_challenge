import os
import csv

budget_csv = os.path.join(".", "Resources", "budget_data.csv")

# testing to see if file path to csv was correct
with open(budget_csv, "r") as csv_file: 
     reader = csv.reader(csv_file, delimiter=",")

     headers = next(reader)
     print(headers)

def financial_analysis(budget_data):

    months = str(budget_data[0])
    profits_losses = int(budget_data[1])

    total_months = len(months)
    print(total_months)

    print(f"Total Months: {str(total_months)}")





