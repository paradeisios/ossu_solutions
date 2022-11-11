#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:19:48 2022

@author: paradeisios
"""
import numpy as np


x = input("Enter number x: ")
y = input("Enter number y: ")

power = np.power(int(x),int(y))
log   = np.log2(int(x))

print("x**y = {}".format(power))
print("log(x) = {}".format(log))