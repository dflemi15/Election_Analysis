# Election_Analysis

# Project Overview
We have been tasked with providing analysis of the election results of a local congressional elction in Colorado. The following steps were followed to successfully complete the analysis.

1. Find the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the percentage of votes each candidate won
4. Calculate the total number of votes each candidate won
5. Deteermine the winner of the election based on popular votes

# Resources
Data Source: election_results.csv

Software: Python (3.6.1), Visual Studio Code, GitBash

# Challenge Overview
The purpose of the challenege was to add the voting data as collected for each county. This includes the total votes submitted in addition to the percentage of votes submitted for each county. We then used this data to determine the largest voter turnout amongst the counties that were analyzed. This analysis was done so that we could determine the full outome of the election and build a framework that be used for future elections.

# Election results
- How many votes were cast in this congressional election?
  
  Our analysis indicates that a total of 369,711 votes were casts during the election.  

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

  The data revealed that the three counties included in the election were Jefferson, Denver and Arapahoe. Each district generated 38,855, 306,055, and 24,001 votes   respectively. The percentage breakdown yielded 10.5% for Jefferson, 82.8% for Denver, and 6.7% for Arapahoe. These numbers were obtained by writing a for loop   that iterated through the county dictionary and increased each vote count by one for everytime a county waS entered in the data. Then an "if" statement was generated to determin the largest county. The code used can be identified below:
<img width="521" alt="image" src="https://user-images.githubusercontent.com/107585908/177059407-f6b07734-241b-48e2-9128-54cb820f0c8f.png">
 
- Which county had the largest number of votes?
  
  Denever had the largest number of votes which totalled to 306,055 (82.8%). The code used to determine this number can be viewed above.
  
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received. 
- Which candidate won the election, what was their vote     count, and what was their percentage of the total votes?

  Raymon Anthony Doane received 11,606 votes(3.1%) which put him in third place. Charles Casper Stockham received 85,213 votes (23%) which was second place. Diane Degetta wo the election by  a wide  margin that totalled to 272,892 votes (73.8%)

# Challenge Summary
