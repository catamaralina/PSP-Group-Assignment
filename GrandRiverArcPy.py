

#Testing,
selected_station = 2
change_flow = 5

#import the arcpy module
import arcpy

# A function for creating the station layer uses user input
def change_station_symbology(selected_station_name, change_flow, m):
    lyr = m.listLayers("selected_station_name")[0]
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
aprx = arcpy.mp.ArcGISProject("C:/Users/daime/Desktop/GEOM67_PS/GrandRiver/GrandRiver.aprx")
#Accessing the Map 
m = aprx.listMaps("Map")[0]

# #Each station is a different layer. If Station one is Selected. 
# if selected_station == 1:
#     lyr = m.listLayers("StationOne")[0]
#     sym = lyr.symbology
#     #List the colours that we will be using
#     red = {"RGB": [255, 0, 0, 100]}
#     green = {"RGB": [115, 175, 0, 100]}

#     if change_flow >0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
#         sym.renderer.symbol.color = green
#         lyr.symbology = sym
#     elif change_flow < 0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
#         sym.renderer.symbol.color = red
#         lyr.symbology = sym
#     else: 
#         aprx.save()
#         del aprx


# #Each station is a different layer. If Station Two is Selected. 
# if selected_station == 2: 
#     lyr = m.listLayers("StationTwo")[0]
#     sym = lyr.symbology
#     #List the colours that we will be using
#     red = {"RGB": [255, 0, 0, 100]}
#     green = {"RGB": [115, 175, 0, 100]}

#     if change_flow >0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
#         sym.renderer.symbol.color = green
#         lyr.symbology = sym
#     elif change_flow < 0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
#         sym.renderer.symbol.color = red
#         lyr.symbology = sym
#     else: 
#         aprx.save()
#         del aprx

# #Each station is a different layer. If Station Three is Selected.
# if selected_station == 3:
#     lyr = m.listLayers("StationThree")[0]
#     sym = lyr.symbology
#     #List the colours that we will be using
#     red = {"RGB": [255, 0, 0, 100]}
#     green = {"RGB": [115, 175, 0, 100]}

#     if change_flow >0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
#         sym.renderer.symbol.color = green
#         lyr.symbology = sym
#     elif change_flow < 0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
#         sym.renderer.symbol.color = red
#         lyr.symbology = sym
#     else: 
#         aprx.save()
#         del aprx

# #Each station is a different layer. If Station Four is Selected.
# if selected_station == 4:
#     lyr = m.listLayers("StationFour")[0]
#     sym = lyr.symbology
#     #List the colours that we will be using
#     red = {"RGB": [255, 0, 0, 100]}
#     green = {"RGB": [115, 175, 0, 100]}

#     if change_flow >0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
#         sym.renderer.symbol.color = green
#         lyr.symbology = sym
#     elif change_flow < 0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
#         sym.renderer.symbol.color = red
#         lyr.symbology = sym
#     else: 
#         aprx.save()
#         del aprx

# #Each station is a different layer. If Station Five is Selected.
# if selected_station == 5:
#     lyr = m.listLayers("StationFive")[0]
#     sym = lyr.symbology
#     #List the colours that we will be using
#     red = {"RGB": [255, 0, 0, 100]}
#     green = {"RGB": [115, 175, 0, 100]}

#     if change_flow >0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
#         sym.renderer.symbol.color = green
#         lyr.symbology = sym
#     elif change_flow < 0 and lyr.isFeatureLayer and hasattr(sym, "renderer"):
#         sym.renderer.symbol.color = red
#         lyr.symbology = sym
#     else: 
#         aprx.save()
#         del aprx

# List of station names on the map
station_names_list = ["StationOne", "StationTwo", "StationThree", "StationFour", "StationFive"]

if 1 <= selected_station <= 5:
    change_station_symbology(station_names_list[selected_station - 1], change_flow, m)

aprx.save()
del aprx