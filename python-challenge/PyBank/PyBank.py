import os
import csv

csv_path = os.path.abspath(os.path.join("Resources", "budget_data.csv"))

print("Financial Analysis")
print("------------------------")

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    first_row = next(csv_reader)
  
    total_months = 1
    total_profit = 1088983
    previous_month = 1088983
    dates_list = []
    monthly_change_list = []
    for row in csv_reader:
        total_months += 1
        total_profit += int(row[1])
        monthly_change = int(row[1]) - previous_month
        dates_list.append(str(row[0]))
        monthly_change_list.append(monthly_change)
        previous_month = int(row[1])

    print("Total Months: ", total_months)
    print("Total: " + "$" + str(total_profit))

    average_change = sum(monthly_change_list) / len(monthly_change_list)
    print("Average Change: " + "$" + str(round(average_change, 2)))

    greatest_increase = max(monthly_change_list)
    greatest_increase_index = monthly_change_list.index(greatest_increase)
    greatest_increase_date = dates_list[greatest_increase_index]

    print("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")")
    
    greatest_decrease = min(monthly_change_list)
    greatest_decrease_index = monthly_change_list.index(greatest_decrease)
    greatest_decrease_date = dates_list[greatest_decrease_index]

    print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")")

    with open('PyBankAnalysis.txt', 'w') as f:
        f.write("Financial Analysis\n")
        f.write("------------------------\n")
        f.write("Total Months: " + str(total_months) + "\n")
        f.write("Total: " + "$" + str(total_profit) + "\n")
        f.write("Average Change: " + "$" + str(round(average_change, 2)) + "\n")
        f.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")\n")
        f.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")\n")
