#Water Budget
#Using the open source data from Grand River Watershed
#to determine statistical calculations in a select month. 
#Calculate average and compare it to other stations 
#in the watershed

#Assumed constant
#Runoff Coefficient assumed to be .25

#--FUNCTIONS--
#-------------
#Delete if using Acess -- Function to convert hours into month
def MonthHours(month):
    month28 = [2]
    month30 = [4, 6, 9, 11]
    month31 = [1, 3, 5, 7, 8, 10, 12]

    if month in month28:
        monthly_hours = 28*24
    elif month in month30:
        monthly_hours = 30*24
    elif month in month31: 
        monthly_hours = 31*24
    else:
        print("invalid")
    return monthly_hours



#--DATA FROM CSV--
#-----------------
#import runoff



#import rainfall
#convert mm to in


#drainage area (ha)
#Climate Station [Luther Marsh, Guelph Lake, Laurel Creek, York, Rd 32 WQ]
#                [Legatt, Victoria Road, Erbsville, York, Rd 32 WQ Stn]
#County          [Dufferin, Guelph/Eramosa, Waterloo, Haldimand, Wellington]
DrainageArea = [148677, 29284, 6406, 125045, 266536]

#--USER INPUT--
#--------------
selected_station = input("Select a station (1-5, see map for reference): ")
selected_month = input("Select a month (1-12): ")

#--CALCULATIONS--
#----------------
#HOURS IN MONTHS


#----------------
#RUNOFF (Roseke, 2013)
# C = Runoff coefficient = .25 
# i = Rainfall intensity (in/hr)
# A = Drainage area (ha)
# Q = Runoff (ft^3/s)

C = .25
i = 0
A = DrainageArea[(selected_station-1)]
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