#Water Budget
#Using the open source data from Grand River Watershed
#to determine statistical calculations in a select month. 
#Calculate average and compare it to other stations 
#in the watershed

#Assumed constant
#Runoff Coefficient assumed to be .25


#--DATA FROM CSV--
#-----------------
#Import Data
import csv
rows = []
header = []
with open("Complete_Table.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    for row in csvreader:
        rows.append(row)
list = list(rows)

#list = [[id], [station], [month], [flow 18], [flow22], [precip18], [precip22], [areaha]]
#         [0]   [1]         [2]     [3]         [4]         [5]         [6]         [7]

#Again = y for looping purposes. 
again = 'y'

while again == 'y': 
    #--USER INPUT--
    #--------------

    #ADD IN HANDLERS FOR INPUT VALUES THAT ARE NOT INTEGERS
    while True:
        try:
            selected_station = int(input("Select a station (1-5, see map for reference): "))
        except TypeError
            print("Must enter an integer!")
        else:
            if 1 <= selected_station <5
                break 
            else:
                print ("Out of Range.")

    while True:
        try:
            selected_month = int(input("Select a month (1-12): "))-1
        except TypeError
            print("Must enter an integer!")
        else:
            if 1 <= selected_month <12
                break 
            else:
                print ("Out of Range.")
    
    ##Obtaining the station specific records
    record = []
    for i in list:
        index = selected_station*12-12
        start = (selected_station-1)*12
        stop = (selected_station)*12
        record = list[start:stop]

    #--CALCULATIONS--
    #----------------
    #MONTHLY AVERAGE FLOW, PRECIPITATION
    flow_2018 = float(record[selected_month][3])
    flow_2022 = float(record[selected_month][4])
    precip_2018 = float(record[selected_month][5])
    precip_2022 = float(record[selected_month][6])

    #RUNOFF (Roseke, 2013)
    # C = Runoff coefficient = .25 
    # i = Rainfall intensity (mm/hr)
    # A = Drainage area (ha)
    # Q = Runoff (m^3/s)
    # Q = .00278*C*i*A
    C = float(.25)
    DrainageArea = float(record[selected_month][7])
    runoff_2018 = .00278*C*precip_2018*DrainageArea
    runoff_2022 = .00278*C*precip_2022*DrainageArea



    #CHANGE
    change_flow = flow_2018-flow_2022
    change_precip = precip_2018-precip_2022
    change_runoff = runoff_2018-runoff_2022

    #--OUTPUT--
    #----------
    #Maybe add units?
    print("Runoff coefficient in the Grand River watershed is assumed to be .25")
    print("Selected station: ", selected_station)
    print("Selected month: ", (selected_month+1)) #Took a -1 at the beginning for indexing purposes. 
    print('year\t\tFlow(m^3/s)\t\tPrecipitation(mm/hr)\t\tRunoff(m^3/s)')
    print('2018\t\t' + str(flow_2018) + '\t\t' + str(precip_2018)  + '\t\t' + str(runoff_2018))
    print('2022\t\t' + str(flow_2022) + '\t\t' + str(precip_2022) + '\t\t' + str(runoff_2022))
    print("'18-'22\t\t" + str(change_flow) + '\t\t' + str(change_precip) + '\t\t' + str(change_runoff))

    #Ask user if they want to go again
    again = input('Would you like to select another month or location to display? (y/n) ')
    if again.lower() not in ['y','n']:
        print("Please enter 'y' or 'n'")