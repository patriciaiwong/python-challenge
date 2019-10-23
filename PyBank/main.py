import pandas as pd

budget_csv = "budget_data.csv"
budget_df = pd.read_csv(budget_csv, encoding="ISO-8859-1")

number_of_months = len(budget_df)
total = budget_df["Profit/Losses"].sum()

delta = budget_df["Profit/Losses"].diff()

budget_df["Change"] = delta

average_delta = budget_df["Change"].mean(skipna = True)

maxdelta = budget_df["Change"].max()
mindelta = budget_df["Change"].min()


greastest_increase = budget_df.loc[budget_df['Change'] == maxdelta, 'Date']
greastest_decrease = budget_df.loc[budget_df['Change'] == mindelta, 'Date']

string_months = "Total Months: " + str(number_of_months)
total_print = "Total: $" + str(total)
av_delta_print = "Average of the Changes in Profit/Losses: $" + str("{0:.2f}".format(average_delta))
gip = "Greatest Increase in Profits: $" + str(maxdelta) + str(greastest_decrease)
gdp = "Greatest Decrease in Profits: $" + str(mindelta) + str(greastest_increase)

print("Financial Analysis")
print("-------------------------------------")
print(string_months)
print(total_print)
print(av_delta_print)
print(gip)
print(gdp)

file = open("Summary.txt", "w") 
file.write("Financial Analysis")
file.write("\n-------------------------------------\n")
file.write(string_months)
file.write("\n")
file.write(total_print)
file.write("\n")
file.write(av_delta_print)
file.write("\n")
file.write(gip)
file.write("\n")
file.write(gdp)
file.close()