#Testing,
selected_station = 2
change_flow = 5

#import the arcpy module
import arcpy

# A function for creating the station layer uses user input
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

#Accessing our ArcGIS Pro File
aprx = arcpy.mp.ArcGISProject("GrandRiver.aprx")

#Accessing the Map 
m = aprx.listMaps("Map")[0]

station_names_list = ["StationOne", "StationTwo", "StationThree", "StationFour", "StationFive"]

if 1 <= selected_station <= 5:
    change_station_symbology(station_names_list[selected_station - 1], change_flow, m)

aprx.saveACopy("GrandRiver_Symbology.aprx")
del aprx