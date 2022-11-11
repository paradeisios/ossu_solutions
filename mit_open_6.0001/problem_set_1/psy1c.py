#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:29:58 2022

@author: paradeisios
"""

yearly_salary = int(input("Enter the starting salary: "))

house_cost  = 1000000
down_perc   = 0.25
downpayment = house_cost * down_perc
        
investment_return = 0.04
semi_annual_raise = 0.07

target_months = 36

tolerence = 100


monthly_salary = yearly_salary / 12

lower,upper     = 0,10000
to_save         = (lower + upper) / 2 
current_savings = 0

for month in range(target_months):
    
    salary_saved = (monthly_salary * to_save) / 10000

    # estimate how much bonus you get from returns
    monthly_returns = current_savings*investment_return/12
    
    # estimate new savings
    current_savings += salary_saved + monthly_returns
    
    #check if this month, there is an salary increase
    if month % 6 == 0 and month !=0:
        
        monthly_salary += monthly_salary * semi_annual_raise
        
        
steps = 0

while abs(current_savings - downpayment) >= tolerence:
    
    if current_savings > downpayment:
        
        upper = to_save
    
    else:
        
        lower = to_save
        
    to_save         = (upper + lower) / 2
    current_savings = 0
    monthly_salary  = yearly_salary / 12
    
    for month in range(target_months):
        
        if month % 6 == 0 and month !=0:
            
            monthly_salary += monthly_salary * semi_annual_raise
            
        salary_saved = (monthly_salary * to_save) / 10000

        # estimate how much bonus you get from returns
        monthly_returns = (current_savings*investment_return)/12
        
        # estimate new savings
        current_savings += salary_saved + monthly_returns
        
    
    steps +=1 
    
    if steps == target_months:
        break
    
if steps == target_months:
    print("It is not possible to pay the down payment in three years")
else:
    print("Best rate to save : {}".format(to_save/10000))
    print("Steps in bisection search : {}".format(steps))