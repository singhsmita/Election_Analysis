# add your dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialise a total vote counter.
total_votes = 0

# Declare a new list for candidate_names.
candidate_list = []

# Declare an empty dictionary.
candidate_votes = {}

# Winning candidate and winning votes tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

   # Print the header row.
    headers=next(file_reader)


    # Print each row in CSV file.
    for row in file_reader:
        
        # Add the total vote count.
        total_votes += 1

       # print the candidates names from each row
        candidate_name = row[2]

        if candidate_name not in candidate_list:
        
            # add the candidate names to the declared list.
            candidate_list.append(candidate_name)

            # Initialise candidate votes as 0
            candidate_votes[candidate_name] = 0

            # Increment candidate votes
        candidate_votes[candidate_name] += 1

#  Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:

# Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    # Calculate vote % for each candidate
    vote_percentage = float(votes) / float(total_votes) * 100
    
#Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent = vote_percentage.
         
         winning_count = votes
         winning_percentage = vote_percentage

         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
         
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

    
    








