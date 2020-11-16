# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:56:30 2018

@author: nitingera
"""

subjectList = ["English", "Spanish", "Algebra", "Geography", "Theater"]
gpas = [3.12, 3.45, 2.99]

if subjectList[0] == "Geography":
    takingGeograhy=True
elif subjectList[1] == "Geography":
    takingGeograhy=True
elif subjectList[2] == "Geography":
    takingGeograhy=True
elif subjectList[3] == "Geography":
    takingGeograhy=True
elif subjectList[4] == "Geography":
    takingGeograhy=True
else:
    takingGeograhy=False
    
print("Taking Geography" if takingGeograhy==True else "Not Taking Geography")

print("average more than 3.33" if (gpas[0] + gpas[1] + gpas[2])/3 > 3.33 else "Average less than 3.33")

average = (gpas[0] + gpas[1] + gpas[2])/3
if(average > 3.33):
    print("average more than 3.33")
else:
    print("Average less than 3.33")