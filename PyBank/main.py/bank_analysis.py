import os
import csv

csv_file_path = "\\Users\\larry\\OneDrive\\Desktop\\Starter_Code\\PyBank\\Resources\\budget_data.csv"  
output_file_path = "\\Users\\larry\\OneDrive\\Desktop\\vbu_mod_3\\python-challenge\\PyBank\\main.py\\analysis\\bank_analysis_results.txt"  

def analyze_and_export_bank_data(csv_file_path, output_file_path):
    total_months = 0
    net_profit_loss = 0
    previous_profit_loss = 0
    changes = []
    greatest_increase = {"date": "", "amount": float("-inf")}
    greatest_decrease = {"date": "", "amount": float("inf")}

    with open(csv_file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader) 

        for row in csvreader:
            total_months = total_months + 1
            net_profit_loss = net_profit_loss + int(row[1])

            if total_months > 1:
                change = int(row[1]) - previous_profit_loss
                changes.append(change)

                if change > greatest_increase["amount"]:
                    greatest_increase["date"] = row[0]
                    greatest_increase["amount"] = change
                elif change < greatest_decrease["amount"]:
                    greatest_decrease["date"] = row[0]
                    greatest_decrease["amount"] = change

            previous_profit_loss = int(row[1])

    average_change = sum(changes) / len(changes)

    print("Bank Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profit/Loss: ${net_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

    with open(output_file_path, mode="w") as textfile:
        textfile.write("Financial Analysis\n")
        textfile.write("-----------------------------\n")
        textfile.write(f"Total Months: {total_months}\n")
        textfile.write(f"Total Profit/Loss: ${net_profit_loss}\n")
        textfile.write(f"Average Change: ${average_change:.2f}\n")
        textfile.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
        textfile.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

    print(f"Analysis results exported to {output_file_path}")

analyze_and_export_bank_data(csv_file_path, output_file_path)

