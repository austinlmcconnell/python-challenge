import os
import csv

csv_path = os.path.join(r'..', 'Resources','budget_data.csv')

print("Financial Analysis")
print("------------------------")

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)

    total_months = 0
    for row in csv_reader:
        total_months += 1
        print("Total Months: ", total_months)
