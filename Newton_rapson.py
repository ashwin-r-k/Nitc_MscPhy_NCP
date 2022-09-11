#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:06:20 2022

Purpose : To find the root of the given function using the Newton rapson method.     
@author: Ashwin
Roll no : M220590PH
"""

#importing the required definations
import numpy as np
from matplotlib import pyplot as plt

#creating the defination for given function
def fn(x):
    y=-4*x+np.cos(x)+2
    return y

def fn_p(x):
    y=-4-np.sin(x)
    return y

def new_raps(x0,esp):
    
    xip1=x0
    xi=xip1+10*esp
    #just taking xi as a higher value
    
    while abs(xip1-xi)>=esp:
        xi=xip1
        xip1=xi-fn(xi)/fn_p(xi)
    return xip1

x0=0.5
esp=0.0001
root=new_raps(x0, esp)
print("Root is at {0}".format(root))


#Method 2 for rinding nth root of givenn number

def nr_bthroot(xi,a,b,esp):
    xip1=x0
    xi=xip1+10*esp
    #just taking xi as a higher value
    
    while abs(xip1-xi)>=esp:
        xi=xip1
        xip1=1/b*((b-1)*xi + a/pow(xi,b-1))
    return xip1

a=12
b=3
x0=2.5
esp=0.0001

root=nr_bthroot(x0, a, b, esp)
print("{0} th root of {1} is {2}".format(b,a,root))
    