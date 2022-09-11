#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:27:30 2022

Purpose : To find the root of the given function using th bisection method.     
@author: Ashwin
Roll no : M220590PH
"""
 
#importing the needed packages
import numpy as np
from matplotlib import pyplot as plt

#Defining the Function which we want to find root for.
def fn(x):
    y=np.sin(x-1)
    return y

#defining the bisection method
def bisection(a,b,esp):
    itter=0
    
    while abs(a-b)>=esp:
        m=(a+b)/2
        itter=itter+1
        
        if fn(a)==0:
            return a
        elif fn(b)==0:
            return b
        elif fn(a)*fn(m)<0:
            b=m
        elif fn(m)*fn(b)<0:
            a=m
        else:
            print("No Root in given Range")
            break

    return m,itter

#defining the range and values
a=2
b=5
esp=pow(10,-4)


#ploting the given function
x=np.linspace(a,b,int(abs(b-1)/esp))
plt.plot(x,fn(x),label="$Sin(x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(color="red")
plt.axvline(color="red")


# solving the bisection method
root,itter=bisection(a,b,esp)
plt.plot(root,fn(root),"k*",label="Root at x={0}".format(round(root,4)))
plt.legend()

print("The root of given function in given range [{a} {b}] is {root}".format(a=a,b=b,root=round(root,4)))
print("Number of iteration is {itter}".format(itter=itter))