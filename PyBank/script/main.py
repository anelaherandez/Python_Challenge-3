#Main Script for PyBank
# Instructions: 
    #1 Total Number of Months included in the dataset
    #2 Net total amount of Profit/losses over the entire period
    #3 The changes in Profit/Losses over the entire period, AND the average of those changes
    #4 Greatest increase in profits (date and amount) over the entire period
    #5 Greatest decrease in profits (date and amount) over the entire period

import os
import csv
#variables
Total_Months=0
Net_total_pnl=0
Average_pnlchange=0
Greatest_increase=0
Greatest_decrease=0
Months=[]
Profit_Loss=[]
Pnl_Change=[]

csvpath=os.path.join('..', 'Resources', 'budget_data.csv')
out_path=os.path.join('..', 'Analysis', 'Analysis.txt')


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')

    for row in csvreader:
        
    # 1 Total number of Months included in the dataset
        Total_Months +=1

    # 2 net total of profit/losses
        Net_total_pnl+=int(row[1])
    # 3 Change in Profit/Losses for entire period
        Profit_Loss.append(int(row[1]))
        Months.append(row[0])
    for i in range(1, Total_Months):
        change=Profit_Loss[i]-Profit_Loss[i-1]
        Pnl_Change.append(change)
    # Find the average Profit/Loss change for entire period
    Average_pnlchange=sum(Pnl_Change)/len(Pnl_Change)
    # 4 Find the Greatest increase in profits (date and amount) over the entire period
    Greatest_increase=max(Pnl_Change)
    Greatest_index=Pnl_Change.index(Greatest_increase)
    Max_Month=Months[Greatest_index +1]

    # 5 Find the Greatest decrease in profits (date and amount) over the entire period
    Greatest_decrease=min(Pnl_Change)
    GreatestD_index=Pnl_Change.index(Greatest_decrease)
    Min_Month=Months[GreatestD_index +1]

 
    print(f"Net Total Profit "  +  str(Net_total_pnl))
    print(f"Total Months "  +  str(Total_Months))
    print(f"Average Change: " + str(round(Average_pnlchange,3)))
    print(f'Greatest Increase {Greatest_increase} and {Max_Month}')
    print(f'Greatest Decrease {Greatest_decrease} and {Min_Month}')


# Write Analysis Results to Txt File
with open(out_path, "w") as textfile:
    textfile.write('Financial Analysis \n-------------------------- \n')
    textfile.write("Total Months: "  +  str(Total_Months)+'\n')
    textfile.write("Net Total Profit "  + "$"+  str(Net_total_pnl)+'\n')
    textfile.write("Average Change: " + "$"+ str(round(Average_pnlchange,3))+'\n')
    textfile.write(("Greatest Increase in Profits: " + str(Max_Month) + " "  + "($"+str(Greatest_increase)+")" +'\n'))
    textfile.write(("Greatest Decrease in Profits: " + str(Min_Month) + " " + "($" + str(Greatest_decrease)+")" +'\n'))

    
    
    



        

