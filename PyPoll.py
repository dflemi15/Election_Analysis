# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes

# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Set total vote counter to zero
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the csv file
    for row in file_reader:
        total_votes  += 1
        # Print candidate name from each row
        candidate_name = row[2]

        # Only print unique candidate names
        if candidate_name not in candidate_options:
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name] = 0
        # Flush with the if statement allows us to increment each vote for the candidates 
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine the percentage of votes for each candidate by looping through the counts.
        # Iterate through the candidate list.
        for candidate_name in candidate_votes:
                # Retrieve vote count of a candidate.
                votes = candidate_votes[candidate_name]
                # Calculate the percentage of votes.
                vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
                candidate_results  = (
                        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                # Print each candidate's voter count and percentage to the terminal.
                print(candidate_results)
                #  Save the candidate results to our text file.
                txt_file.write(candidate_results)

                # Determine winning vote count and candidate
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                        winning_count = votes
                        winning_percentage = vote_percentage
                        winning_candidate = candidate_name

        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)
