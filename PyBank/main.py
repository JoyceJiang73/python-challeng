import os 
import csv

print ("Financial Analysis")
print ("----------------------------")

from pathlib import Path
path = Path('/Users/yanrujiang/Desktop/python-challenge/PyBank/budget_data.csv')
monthcount = []
sumtotal =[]
monthlychange =[]
with open (path, newline ='')as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        monthcount.append(row[0])
        sumtotal.append(int(row[1]))

 #   totalmonth = int(len(monthcount)
 #   total_profit = sum(sumtotal)

 #   for i in range(len(monthcount)):
 #       monthcount[i]=float(monthcount[i])
    for i in range(len(monthcount)-1):
        change = sumtotal[i+1]-sumtotal[i]
        monthlychange.append(change)
    avgchange = round(sum(monthlychange)/int(len(monthcount),2)

maxchange = max(monthlychange)
minchange = min(monthlychange)
maxchange_month = monthcount[monthlychange.index(maxchange)+1]
minchange_month = monthcount[monthlychange.index(minchange)+1]

print("Total Months: " + str(len(monthcount)))
print("Total: $" + str(sum(sumtotal)))
print("Average  Change: $" + str(avgchange))
print("Greatest Increase in Profits: " + str(maxchange_month) +" ($" + str(maxchange) + ")")
print("Greatest Decrease in Profits: " + str(minchange_month) +" ($" + str(minchange) + ")")


