import pandas as pd

election_csv = "election_data.csv"
election_df = pd.read_csv(election_csv, encoding="ISO-8859-1")

totalvotes = len(election_df)

count = election_df["Candidate"].value_counts()

unique = election_df["Candidate"].unique()

percent = count/totalvotes * 100

results = pd.DataFrame({"Percentage": percent.round(), "Total Votes": count})

maxvotes = results["Total Votes"].max()
winner = results.loc[results['Total Votes'] == maxvotes, "Percentage"]

num1 = "Winner: " + str(winner) + "%"
total= "Total Votes: " + str(totalvotes)
sresults = results.to_string()

print("Election Results")
print("---------------------")
print(total)
print("---------------------")
print(results)
print("---------------------")
print(num1)

file = open("election_results.txt", "w") 
file.write("Election Results")
file.write("\n-------------------------------------\n")
file.write(total)
file.write("\n")
file.write(sresults)
file.write("\n")
file.write(num1)
file.write("\n-------------------------------------")
file.close()