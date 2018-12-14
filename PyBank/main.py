#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[14]:


import os 
import csv
from pathlib import Path
path = Path('/Users/yanrujiang/Desktop/python-challenge/PyBank/budget_data.csv')
monthcount = []
sumtotal =[]
monthlychange =[]
print ("Financial Analysis")
print ("----------------------------")


# In[15]:


with open (path, newline ='')as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        monthcount.append(row[0])
        sumtotal.append(int(row[1]))


# In[16]:


#totalmonth = int(len(monthcount)
#totalprofit = sum(sumtotal)


# In[17]:


for i in range(len(monthcount)-1):
    change = sumtotal[i+1]-sumtotal[i]
    monthlychange.append(change)
avgchange = round(sum(monthlychange)/len(monthcount),2)


# In[18]:


#maxincrease = max(monthlychange)
#maxdecrease = min(monthlychange)
#maxincrease_month = monthcount[monthlychange.index(maxincrease)+1]
#maxdecrease_month = monthcount[monthlychange.index(maxdecrease)+1]
#monthlychange starts from zero
maxchange = max(monthlychange)
minchange = min(monthlychange)
maxchange_month = monthcount[monthlychange.index(maxchange)]
minchange_month = monthcount[monthlychange.index(minchange)]


# In[11]:


print("Total Months: " + str(len(monthcount)))
print("Total: $" + str(sum(sumtotal)))
print("Average  Change: $" + str(avgchange))
print("Greatest Increase in Profits: " + str(maxincrease_month) +" ($" + str(maxincrease) + ")")
print("Greatest Decrease in Profits: " + str(maxdecrease_month) +" ($" + str(maxdecrease) + ")")


# In[12]:


output_file = Path("Output.txt")


# In[13]:


with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Total Months: " + str(len(monthcount)))
    file.write("\n")
    file.write("Total: $" + str(sum(sumtotal)))
    file.write("\n")
    file.write("Average  Change: $" + str(avgchange))
    file.write("\n")
    file.write("Greatest Increase in Profits: " + str(maxincrease_month) +" ($" + str(maxincrease) + ")")
    file.write("\n")
    file.write("Greatest Decrease in Profits: " + str(maxdecrease_month) +" ($" + str(maxdecrease) + ")")


# In[ ]:





# In[ ]:




