#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:29:47 2022

@author: paradeisios
"""

# Saving, with a raise

# specify inputs
annual_salary      = int(input("Enter your annual salary: "))
portion_saved      = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost         = int(input("Enter the cost of your dream home: "))
semi_annual_raise  = float(input("Enter the semiannual raise, as a decimal: ")) 


# specify know vars
portion_down_payment = .25
current_savings      = 0
r                    = 0.04

# calculate known vars
monthly_salary = annual_salary / 12
goal           = total_cost * portion_down_payment



months_elapsed = 0

while current_savings < goal:
    

    # estimate how much you save 
    salary_saved = monthly_salary * portion_saved

    # estimate how much bonus you get from returns
    monthly_returns = current_savings*r/12
    
    # estimate new savings
    current_savings += salary_saved + monthly_returns
    
    #increment the months passed
    months_elapsed += 1
    
    #check if this month, there is an salary increase
    if months_elapsed % 6 == 0:
        
        monthly_salary += monthly_salary * semi_annual_raise
    
    
print("Number of months: {}".format(months_elapsed))