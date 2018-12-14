import os
import csv

from pathlib import Path
path = Path('/Users/yanrujiang/Desktop/python-challenge/PyPoll/election_data.csv')
Total_Votes=[]
Candidate = []
Khan=[]
Correy=[]
Li=[]
OTooley=[]
Name_List=[]

with open (path, newline ='')as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        Total_Votes.append(row[0])
        Candidate.append(row[2])

    for d in range(len(Total_Votes)):
        Name_List.append(Candidate[d+1]!=Candidate[d])
        break

        for i in range(len(Total_Votes)):
            if Candidate[i]==Name_List[0]:
                Khan.append(Candidate[i])
            elif Candidate[i]=="Correy":
                Li.append(Name_List[1])
            elif Candidate[i]=="Li":
                Correy.append(Name_List[2])
            elif Candidate[i]=="O'Tooley":
                OTooley.append(Name_List[3])

Khan_Count = len(Khan)
Correy_Count = len(Correy)
Li_Count = len(Li)
OTooley_Count= len(OTooley)

Khan_percent = round(len(Khan)/len(Total_Votes)*100,3)
Correy_percent=round(len(Correy)/len(Total_Votes)*100,3)
Li_percent=round(len(Li)/len(Total_Votes)*100,3)
OTooley_percent=round(len(OTooley)/len(Total_Votes)*100,3)

#winner = max[Khan_Count,Correy_Count,Li_Count,OTooley_Count]

print ("Election Results")
print ("----------------------------")
print( "Total Votes: " + str(len(Total_Votes)))
print ("----------------------------")
print(f"Khan: {Khan_percent}% ({Khan_Count})")
print(f"Correy: {Correy_percent}% ({Correy_Count})")
print(f"Li: {Li_percent}% ({Li_Count})")
print(f"O'Tooley: {OTooley_percent}% ({OTooley_Count})")

