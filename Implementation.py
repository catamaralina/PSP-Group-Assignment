#Water Budget
#Using the open source data from Grand River Watershed
#to determine statistical calculations in a select month. 
#Calculate average and compare it to other stations 
#in the watershed

#Assumed constant
#Runoff Coefficient assumed to be .25

#--DATA FROM CSV--
#-----------------
#input runoff



#input rainfall
#convert mm to in



#--USER INPUT--
#--------------
selected_station = input("Select a station (1-5, see map for reference): ")
selected_month = input("Select a month (1-12): ")

#--CALCULATIONS--
#----------------
#RUNOFF (Roseke, 2013)
# C = Runoff coefficient = .25 
# i = Rainfall intensity (in/hr)
# A = Drainage area (ha)
# Q = Runoff (ft^3/s)

C = .25
i = 0
A = 0
Q = C*i*A







#MONTHLY AVERAGE FLOW, PRECIPITATION
flow_2018 = 
flow_2022 = 
precip_2018 = 
precip_2022 = 
runoff_2018 = 
runoff_2022 = 
#CHANGE
change_flow = flow_2018-flow_2022
change_precip = precip_2018-precip_2022
change_runoff = runoff_2018-runoff_2022




#--OUTPUT--
#----------

print("Runoff coefficient in the Grand River watershed is assumed to be .25")
print("Selected station: ", selected_station)
print("Selected month: ", selected_month)
print('year\t\tFlow\t\tPrecipitation\t\tRunoff')
print('2018\t\t' + + '\t\t' + + '\t\t' + )
print('2022\t\t' + + '\t\t' + + '\t\t' + )
print("'18-'22\t\t" + change_flow + '\t\t' + change_precip + '\t\t' + change_runoff)

again = input('Would you like to select another month or location to display? (y/n) ')