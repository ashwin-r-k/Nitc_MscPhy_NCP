#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:44:23 2022

Purpose : To find minima and Maxima of a list of randome list     
@author: Ashwin
Roll no : M220590PH

You can ignore the spaces and comments i had just written them for explaning
the working of code.
"""

#Creating a list
list=[-213,234,743,-272,346,632,788]


#initalizing the min max variable
#taking thefirst element as min and max
min=list[0]
max=list[0]

#loop for checking the values
#here each element from list is taken at a time and comparedwith min max
for i in list:
    
    #if the number i is less then min then change min to that number
    if i<=min:
        min=i
        
    #if the number i is greater then max then change max to that number
    if i>=max:
        max=i

#printing the result
print("The Given list is ",list)
print("THe minimum from given list is = {0}".format(min))
print("THe maximum from given list is = {0}".format(max))

#this .format is a function to formate the string to put the values in any place.
#you can use the % thing that sir taught.
#i prefer this above one.

#Thank You  :)