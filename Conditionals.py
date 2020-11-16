# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:46:49 2018

@author: nitingera
"""

marks=91
grade="D"

if marks>90:
    grade="A+"
elif marks > 85:
    grade="A"
elif marks > 80:
    grade="B+"
elif marks >75:
    grade="B"
else:
    grade="C"

print("Grade is:",grade)

print ("Eligible to buy alcohol" if marks >=92 else "Ineligible to buy alcohol")