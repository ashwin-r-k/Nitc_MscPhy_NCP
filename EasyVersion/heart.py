#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:42:48 2022

@author: Sreemish :)
"""

import numpy as np
from matplotlib import pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100)

# Generating x and y data
x = 16 * ( np.sin(theta) ** 3 )
y = 15 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

plt.plot(x, y,"r*")
plt.fill_between(x,y, color='deeppink')
plt.show()