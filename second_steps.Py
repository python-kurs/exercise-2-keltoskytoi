#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:48:53 2019

@author: keltoskytoi
"""

# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]
sat_database["GOES"] = 2000 
sat_database["WORLDVIEW"] = 0.31  

print(sat_database)
print(sat_database.keys())
#dict_keys(['METEOSAT', 'LANDSAT', 'MODIS', 'GOES', 'WORLDVEIW'])

print(sat_database.values())
#dict_values([3000, 30, 500, 2000, 0.31])

print ("I have the following satellites in my database {}{}:".format(sat_database.values(), sat_database.keys()))
#we want only the key

print ("I have the following satellites in my database:", list(sat_database.keys()))

# 2) print out all satellite names contained in the dictionary [2P]
print(sat_database.keys())

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]

answer = input("Of which Satellite do you want to know the resolution?")

# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

if answer == "METEOSAT":
    print ("You are lucky, METEOSAT is in the database.")
    
elif answer == "LANDSAT":
    print ("You are lucky, LANDSAT is in the database.")
    
elif answer == "MODIS":
    print ("You are lucky, MODIS is in the database.")
    
elif answer == "GOES":
    print ("You are lucky, GOES is in the database.")
    
elif answer == "WORLDVIEW":
    print ("You are lucky, WORDLVIEW is in the database.")
    
else:
    print("Sorry, the Satellite, which you are looking for is not available in our database. Have you checked the spelling?")

# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 
    
if answer == "METEOSAT":
   print("The satellite METEOSAT has the following resolution:", sat_database[answer],".")
    
elif answer == "LANDSAT":
     print("The satellite LANDSAT has the following resolution:", sat_database.get(answer),".")
    
elif answer == "MODIS":
     print("The satellite MODIS has the following resolution:", sat_database["MODIS"],".")
    
elif answer == "GOES":
     print("The satellite GOES has the following resolution:", sat_database.get("GOES"),".")  
     
     
 sat_database["MODIS"]    