# Main script for PyPoll
# Instructions:
    #1 Total number of votes cast
    #2 Complete list of candidates who received votes
    #3 Percentage of Votes each Candidate won
    #4 Total Number of Votes Each Candidate Won
    #5 Winner of the Election Based on Popular Vote

import os
import csv

#variables
Total_Votes_Cast=0
Candidates=[]
candidate_name=[]
Candidate_Vote={}
Vote_Percentage=0
Total_Vote_Cand=0
Vote_Percentage_list=[]
Clean_Vote_Percent=0
Summary=[]


csvpath=os.path.join('..', 'Resources', 'election_data.csv')
out_path=os.path.join('..', 'Resources', 'Analysis.txt')

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')    

    for row in csvreader:
        # total votes cast for election
        Total_Votes_Cast=Total_Votes_Cast+1
        # Designation of index position in csv equivalent for list Candidates
        Candidates=row[2]
        # adding candidates into name list and gathering their votes
        if Candidates not in candidate_name:
            candidate_name.append(Candidates)
            Candidate_Vote[Candidates]=0
        Candidate_Vote[Candidates]=Candidate_Vote[Candidates]+1
    # looping to get the percentage of votes received for each candidate
    for Candidates in Candidate_Vote:
        Vote_Percentage=(f'{Candidates}:{Candidate_Vote[Candidates]/Total_Votes_Cast*100} %')
        Summary=[Vote_Percentage]
        print(Summary)
        
         
print(Total_Votes_Cast)
print(Candidate_Vote)
# Combining the candidate vote data to find the winner of the election
Winner=max(zip(Candidate_Vote.values(), Candidate_Vote.keys()))[1]
print(Winner)

with open(out_path, "w") as textfile:
        textfile.write('Election Results \n-------------------\n')
        textfile.write('Total Votes: '+ str(Total_Votes_Cast)+ '\n-------------------\n')
        textfile.write('Percentage of Votes Won By Candidate: ' + str(Summary) + '\n------------------\n')
        textfile.write('Total Votes Received by Candidate: ' + str(Candidate_Vote)+ '\n------------------\n')
        textfile.write('Election Winner: '+ str(Winner))

