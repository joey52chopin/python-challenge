import csv
import os
import pandas as pd

# Specify the full path to the CSV file
csv_path = r"C:\Users\joey5\Desktop\Module 3\Starter_Code\PyBank\Resources\budget_data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)
df.head()

# Calculate the total number of months
total_months = df["Date"].nunique()

# Calculate the net total amount of "Profit/Losses"
total = df["Profit/Losses"].sum()


# Calculate the changes in "Profit/Losses" and store them in a new column
df["Profit/Loss Change"] = df["Profit/Losses"].diff()

# Calculate the average change
average_change = df["Profit/Loss Change"].mean()

# Calculate the changes in "Profit/Losses" and store them in a new column
df["Profit/Loss Change"] = df["Profit/Losses"].diff()

# Find the row with the greatest increase in profits
greatest_increase_row = df[df["Profit/Loss Change"]
                           == df["Profit/Loss Change"].max()]
# Extract the date and amount of the greatest increase
greatest_increase_date = greatest_increase_row.iloc[0]["Date"]
greatest_increase_amount = greatest_increase_row.iloc[0]["Profit/Loss Change"]

# Find the row with the greatest increase in profits
greatest_decrease_row = df[df["Profit/Loss Change"]
                           == df["Profit/Loss Change"].min()]
# Extract the date and amount of the greatest increase
greatest_decrease_date = greatest_decrease_row.iloc[0]["Date"]
greatest_decrease_amount = greatest_decrease_row.iloc[0]["Profit/Loss Change"]

file_to_output = os.path.join("analysis", "budget_analysis.txt")

with open(file_to_output, "w") as txt_file:

    print(f"Financial Analysis\n")
    txt_file.write(f"Financial Analysis\n")
    print("-----------------------------------------\n")
    txt_file.write("-----------------------------------------\n")

    # Print the total number of months
    print(f"Total Months: {total_months}\n")
    txt_file.write(f"Total Months: {total_months}\n")

    # Print the net total amount
    print(f"Total : ${total}\n")
    txt_file.write(f"Total : ${total}\n")

    # Print the changes and the average change
    print(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")

    # Print the greatest increase in profits
    print(
        f"Greatest Increase in Profits: {greatest_increase_date} (${int(greatest_increase_amount)})\n")
    txt_file.write(
        f"Greatest Increase in Profits: {greatest_increase_date} (${int(greatest_increase_amount)})\n")
    
    # Print the greatest increase in profits
    print(
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${int(greatest_decrease_amount)})\n")
    txt_file.write(
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${int(greatest_decrease_amount)})\n")
