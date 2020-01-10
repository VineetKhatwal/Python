from StructuredProg import *

basic = float(input("Please enter the basic salary"))
gross = basic + da(basic) + hra(basic)
print("Gross Salary = ",gross)

netSal = gross - pf(basic) - itax(gross)
print("Net Salary   = ",netSal)

if _name_ == '_main_':
    print("This code runs as a program")
else:
    print("This code runs as module")
