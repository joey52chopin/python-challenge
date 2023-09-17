import csv
import os
import pandas as pd

# Specify the full path to the CSV file
csv_path = r"Resources/election_data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)
df.head()

#The total number of votes cast
# Initialize a variable to count the total number of votes
total_votes = 0
# Count the total number of votes (rows)
total_votes = len(df)

# A complete list of candidates who received votes
# Get the unique list of candidates who received votes
candidates_list = df["Candidate"].unique()
# Print the list of candidates
print("Candidates who received votes:")
for candidate in candidates_list:
    print(candidate)

# Create a DataFrame to store candidate vote counts
candidate_votes = df["Candidate"].value_counts().reset_index()
candidate_votes.columns = ["Candidate", "Votes"]

# Calculate the percentage of votes each candidate won
candidate_votes["Percentage"] = (candidate_votes["Votes"] / total_votes) * 100

file_to_output = os.path.join("analysis", "election_analysis.txt")

with open(file_to_output, "w") as txt_file:
   
    # Print the results
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for index, row in candidate_votes.iterrows():
     print(f"{row['Candidate']}: {row['Percentage']:.3f}% ({row['Votes']})")
     txt_file.write(f"{row['Candidate']}: {row['Percentage']:.3f}% ({row['Votes']})\n")

    print("-------------------------")
    txt_file.write("-------------------------\n")

    # Find the winner
    winner = candidate_votes["Candidate"].iloc[0]
    print(f"Winner: {winner}")
    txt_file.write(f"Winner: {winner}\n")
    print("-------------------------")
    txt_file.write("-------------------------")
