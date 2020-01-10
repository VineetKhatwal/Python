def da(basic):
    return basic * 80 / 100

def hra(basic):
    return basic * 15 / 100

def pf (basic):
    return basic * 12 / 100

def itax (gross):
    return gross * 10 / 100

basic = float(input("Please enter the basic salary"))
gross = basic + da(basic) + hra(basic)
print("Gross Salary = ",gross)

netSal = gross - pf(basic) - itax(gross)
print("Net Salary   = ",netSal)

    

    
