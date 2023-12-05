# Title: Water Budget
# Date: Tuesday, December 5, 2023
# Author Contributions:
#	Mengie: Created the Arcpy portion that will change the symbology of the two stations selected by the user on a map either 
#           green or red depending on runoff ratio of the watershed.
#	Tali: Created implementation portion of code: CSV import, loop for user, getting data from import, calculations, output table.
#	Ryan: code :D
#	Hannah: Combined the data of five stations from each month between the years 2018 and 2022 into one combined csv - and wrote the 
#           comments for the top of the code.
# Purpose: Runoff is described to be the total amount of water discharged from a watershed via river or streams, and the runoff ratio 
#          is the runoff for each watershed divided by the precipitation for that watershed (Minnesota Pollution Control Agency). This 
#          program uses open sourced data collected from the Grand River Watershed to determine statistical calculations of a selected 
#          specific station in a select month and then compares between 2018 and 2022. As well, calculates the average and compares it 
#          to other stations in the watershed.
# Description of Structure: The code begins with importing the data csv in read only. The code asks the user for inputs of selected 
#                           stations and chosen month in numerical form. The csv is formatted the data in a list of lists. Calculation 
#                           is made from the formula and then the change between the values for the change in flow between the years, 
#                           change in precipitation, and then change in runoff. In the terminal, the original values are printed and 
#                           then in a table format the calculated answers are displayed. The option to loop the program is given if the 
#                           user wishes to see the difference from another station.
# Assumptions: Runoff Coefficient assumed to be constant value of .25
# Limitations: As the coefficent in the formula remains constant (for the averaged landuse of the watershed), there is a limtation to 
#              accuracy for the specific areas of stations.
# Special Cases/Known Problems: Exceptions will be raised to limit what the user can input in the form of producing an error letting the
#                               use correct their input. Otherwise there are no known problems.
# Inputs/Output: There are only three inputs taken from the user: From 1-5 the station the use would like to compare, from 1-12 the 
#                month the user would like to compare, and 'y/n' if the user would like to loop the program and compare another station.
#                The output of the program displays the inputted variables (flow and precipitation from 2018 and 2022 of the selected 
#                month), the calculated runoff, and the changes between the two sets of numbers in the form of a table generated in the 
#                terminal - as well as a map that changes symbology of the two points depending on the results. 
# References:
# https://www.roseke.com/how-to-calculate-runoff/ - We got our formula used for the calculations from this site.
# https://www.oregon.gov/ODOT/GeoEnvironmental/Docs_Hydraulics_Manual/Hydraulics-07-F.pdf - This site contains a thorough list of the 
# coefficient used within the formula, where we got our constant 0.25 due to the watershed being made up of 70% farms.
# https://data.grandriver.ca/downloads-monitoring.html - From the Grand River Conservation Authority we downloaded the open data used 
# to make up the csv.
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/ - For the csv to list import. 

#--Import arcpy module --
import arcpy

# Arcpy: A function for creating the station layer uses user input
def change_station_symbology(selected_station_name, change_flow, m):
    lyr = m.listLayers(selected_station_name)[0]
    sym = lyr.symbology
    #List the colours that we will be using
    red = {"RGB": [255, 0, 0, 100]}
    green = {"RGB": [115, 175, 0, 100]}

    if change_flow >0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
        sym.renderer.symbol.color = green
    elif change_flow < 0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
        sym.renderer.symbol.color = red

    lyr.symbology = sym

#--DATA FROM CSV--
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
# LIST FORMAT:
# list = [[id], [station], [month], [flow 18], [flow22], [precip18], [precip22], [areaha]]

#Again = y for looping purposes. 
again = 'y'

while again.lower()== 'y': 
    #--USER INPUT--
    #ADD IN HANDLERS FOR INPUT VALUES THAT ARE NOT INTEGERS
    while True:
        try:
            selected_station = int(input("Select a station (1-5, see map for reference): "))
        except ValueError:
            print("Must enter an integer!")
        else:
            if 1 <= selected_station <=5:
                break 
            else:
                print ("Out of Range.")

    while True:
        try:
            selected_month = int(input("Select a month (1-12): "))-1
        except ValueError:
            print("Must enter an integer!")
        else:
            if 1 <= selected_month <=12:
                break 
            else:
                print ("Out of Range.")
    
    ##OBTAINING STATION SPECIFIC RECORDS
    record = []
    for i in list:
        # Values for 5 stations, 12 months in one list
        # Starting value for next station will be 12 records after the previous
        index = selected_station*12-12
        start = (selected_station-1)*12
        stop = (selected_station)*12
        record = list[start:stop]

    #--CALCULATIONS--
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
    print("Runoff coefficient in the Grand River watershed is assumed to be .25")
    print("Selected station: ", selected_station)
    print("Selected month: ", (selected_month+1)) #Took a -1 at the beginning for indexing purposes. 
    print('year\t\tFlow(m^3/s)\t\tPrecipitation(mm/hr)\t\tRunoff(m^3/s)')
    print('2018\t\t' + str(flow_2018) + '\t\t' + str(precip_2018)  + '\t\t' + str(runoff_2018))
    print('2022\t\t' + str(flow_2022) + '\t\t' + str(precip_2022) + '\t\t' + str(runoff_2022))
    print("'18-'22\t\t" + str(change_flow) + '\t\t' + str(change_precip) + '\t\t' + str(change_runoff))


    #Accessing our ArcGIS Pro File
    aprx = arcpy.mp.ArcGISProject("GrandRiver.aprx")
    #Accessing the Map 
    m = aprx.listMaps("Map")[0]

    station_names_list = ["StationOne", "StationTwo", "StationThree", "StationFour", "StationFive"]
    if 1 <= selected_station <= 5:
        change_station_symbology(station_names_list[selected_station - 1], change_flow, m)

    aprx.saveACopy("GrandRiver_Symbology.aprx")
    del aprx

    #Ask user if they want to go again
    again = input('Would you like to select another month or location to display? (y/n) ')
    
    if again.lower() not in ['y','n']:
        print("Please enter 'y' or 'n'")
