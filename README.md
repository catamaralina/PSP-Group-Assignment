# PSP-Group-Assignment
## Title: Water Budget
## Date: Tuesday, December 5, 2023
## Author Contributions:
### Mengie 
Created the Arcpy portion that will change the symbology of the station(s) 
selected by the user on a map to either green or red or remained the same 
depending on if the change in flow was positive or negative.  
### Tali
Created implementation portion of code: CSV import, user input & loop, getting station specific data from import, calculations, output table.
### Ryan
Created efficiencies in the arcpy code by turning the code into a function.  Completed the user input (y/n) loop and created comments. 
### Hannah
Combined the data of five stations from each month between the years 2018 and 2022 into one combined csv - 
and wrote the comments for the top of the code. Filled out the test values excel file. Did the error coding for user inputs. 
## Purpose: 
Runoff is described to be the total amount of water discharged from a watershed via river or streams, and the runoff ratio 
is the runoff for each watershed divided by the precipitation for that watershed (Minnesota Pollution Control Agency). This 
program uses open sourced data collected from the Grand River Watershed to determine statistical calculations of a selected 
specific station in a select month and then compares between 2018 and 2022. As well, calculates the average and compares it 
to other stations in the watershed.
## Description of Structure: 
The code begins with importing the data csv in read only. The code asks the user for inputs of selected 
stations and chosen month in numerical form. The csv is formatted the data in a list of lists. Calculation 
is made from the formula and then the change between the values for the change in flow between the years, 
change in precipitation, and then change in runoff. In the terminal, the original values are printed and 
then in a table format the calculated answers are displayed. The option to loop the program is given if the 
user wishes to see the difference from another station.
## Assumptions
Runoff Coefficient assumed to be constant value of .25
## Limitations
As the coefficent in the formula remains constant (for the averaged landuse of the watershed), there is a limtation to 
accuracy for the specific areas of stations.
## Special Cases/Known Problems
Exceptions will be raised to limit what the user can input in the form of producing an error letting the
use correct their input. Otherwise there are no known problems.
## Inputs/Output
There are only three inputs taken from the user: From 1-5 the station the use would like to compare, from 1-12 the 
month the user would like to compare, and 'y/n' if the user would like to loop the program and compare another station.
The output of the program displays the inputted variables (flow and precipitation from 2018 and 2022 of the selected 
month), the calculated runoff, and the changes between the two sets of numbers in the form of a table generated in the 
terminal - as well as a map that changes symbology of the station depending on if the change in flow was positive or negative. 
## References:
### https://www.roseke.com/how-to-calculate-runoff/ 
We got our formula used for the calculations from this site.
### https://www.oregon.gov/ODOT/GeoEnvironmental/Docs_Hydraulics_Manual/Hydraulics-07-F.pdf
This site contains a thorough list of the coefficient used within the formula, where we got our constant 0.25 due to the watershed being made up of 70% farms.
### https://data.grandriver.ca/downloads-monitoring.html
From the Grand River Conservation Authority we downloaded the open data used to make up the csv.
### https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
For the csv to list import. 
