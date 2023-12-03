#Water Budget
#Using the open source data from Grand River Watershed
#to determine statistical calculations in a select month. 
#Calculate average and compare it to other stations 
#in the watershed

#Assumed constant
#Runoff Coefficient assumed to be .25

#--FUNCTIONS--
#-------------


#--DATA FROM CSV--
#-----------------
#import data

list = [[id], [station], [month], [flow 18], [flow22], [precip18], [precip22], [areaha]]


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
# i = Rainfall intensity (mm/hr)
# A = Drainage area (ha)
# Q = Runoff (m^3/s)

C = .25
# Ri = 0
# A = DrainageArea[(selected_station-1)] #grabs indexed station area
# Q = .00278*C*i*A

record = []

for i in range (len(list)):
    #get the station specific records
    record = record + list[i][(selected_station-1)*12:(selected_station)*12]

for j <=12: 

#MONTHLY AVERAGE FLOW, PRECIPITATION
flow_2018 = record[3][selected_month]
flow_2022 = record[4][selected_month]
precip_2018 = record[5][selected_month]
precip_2022 = record[6][selected_month]
DrainageArea = record[7][selected_month]
runoff_2018 = .00278*C*precip_2018*DrainageArea
runoff_2022 = .00278*C*precip_2022*DrainageArea
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
print('2018\t\t' + flow_2018 + '\t\t' + precip_2018  + '\t\t' + runoff_2018)
print('2022\t\t' + flow_2022 + '\t\t' + precip_2022 + '\t\t' + runoff_2022)
print("'18-'22\t\t" + change_flow + '\t\t' + change_precip + '\t\t' + change_runoff)

again = input('Would you like to select another month or location to display? (y/n) ')