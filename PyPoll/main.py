#!/usr/bin/env python
# coding: utf-8

# In[105]:


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


# In[106]:


with open (path, newline ='')as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        Total_Votes.append(row[0])
        Candidate.append(row[2])


# In[107]:


#    for d in range(len(Total_Votes)):
#        Name_List.append(Candidate[d+1]!=Candidate[d])
#        break

#        for i in range(len(Total_Votes)):
#            Khan.append(Candidate[i]=="Kahn")
#        for a in range(len(Total_Votes)):
#            Correy.append(Candidate[a]=="Correy")
#        for b in range(len(Total_Votes)):
#            Li.append(Candidate[b]=="Li")
#        for c in range(len(Total_Votes)):
#            OTooley.append(Candidate[c]=="O'Tooley")
        for i in range(len(Total_Votes)):
            if Candidate[i]=="Khan":
                Khan.append(Candidate[i])
            elif Candidate[i]=="Correy":
                Correy.append(Candidate[i])
            elif Candidate[i]=="Li":
                Li.append(Candidate[i])
            elif Candidate[i]=="O'Tooley":
                OTooley.append(Candidate[i])


# In[108]:


Khan_Count = len(Khan)
Correy_Count = len(Correy)
Li_Count = len(Li)
OTooley_Count= len(OTooley)


# In[109]:


print(Khan_Count+Correy_Count+Li_Count+OTooley_Count)


# In[110]:


Khan_percent = round(len(Khan)/len(Total_Votes)*100,3)
Correy_percent=round(len(Correy)/len(Total_Votes)*100,3)
Li_percent=round(len(Li)/len(Total_Votes)*100,3)
OTooley_percent=round(len(OTooley)/len(Total_Votes)*100,3)


# In[111]:


#Name = ["Khan","Correy","Li","O'Tooley"]
#Count = [Khan_Count,Correy_Count,Li_Count,OTooley_Count]
#match = zip(Name,Count)
#max_vote = max[Count]
#winner=name[max_vote.index(max_vote)]
#winner = max[Khan_Count,Correy_Count,Li_Count,OTooley_Count]


# In[112]:


print ("Election Results")
print ("----------------------------")
print( "Total Votes: " + str(len(Total_Votes)))
print ("----------------------------")
print(f"Khan: {Khan_percent}% ({Khan_Count})")
print(f"Correy: {Correy_percent}% ({Correy_Count})")
print(f"Li: {Li_percent}% ({Li_Count})")
print(f"O'Tooley: {OTooley_percent}% ({OTooley_Count})")
print ("----------------------------")
print(f"Winner: Khan")
print ("----------------------------")   


# In[113]:


output_file = Path("Output.txt")


# In[114]:


with open(output_file,"w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Total Votes: " + str(len(Total_Votes)))
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Khan: {Khan_percent}% ({Khan_Count})")
    file.write("\n")
    file.write(f"Correy: {Correy_percent}% ({Correy_Count})")
    file.write("\n")
    file.write(f"Li: {Li_percent}% ({Li_Count})")
    file.write("\n")
    file.write(f"O'Tooley: {OTooley_percent}% ({OTooley_Count})")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: Khan")
    file.write("\n")
    file.write("----------------------------")   


# In[ ]:




