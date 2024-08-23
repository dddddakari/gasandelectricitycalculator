# Defining Variables #
fixedMonthlyFee = 120.62
fixedTransactionFee = 1.32
taxRates = {'AB': 0.05, 'BC': 0.05, 'MB': 0.05, 'NT': 0.05, 'NU': 0.05,
             'QC': 0.05, 'SK': 0.05, 'YT': 0.05,'ON': 0.13,'NB': 0.15, 
             'NL': 0.15, 'NS': 0.15, 'PE': 0.15}

# User Input #
print("Welcome to Global Energy bill calculator!")
accNumber = input("Enter your account number: ")
month = (input("Enter the month number (e.g., for January, enter 1): "))
electricityPlan = input("Enter your electricity plan (EFIR or EFLR): ")
electricityUsed = float(input("Enter the amount of electricity you used in month " + month + " (in kWh): "))
gasPlan = input("Enter your gas plan (GFIR or GFLR): ")
gasUsed = float(input("Enter the amount of gas you used in month " + month + " (in GJ): "))
province = input("Enter the abbreviation for your province of residence (two letters): ")

# Calculate electricity cost #

if electricityPlan == 'EFIR':    
    if electricityUsed >= 1000:        
        electricityCost = 1000 * 0.0836 
    else:        
        electricityCost = electricityUsed * 0.0941   
elif electricityPlan == 'EFLR':
        electricityCost = electricityUsed * 0.0911
else:
        print("That is not a valid plan!")

# Calculate gas cost #
if gasPlan == 'GFIR':    
    if gasUsed > 950:       
        gasCost = 950 * 0.0456
    else:
        gasPlan == 'GFLR'
        gasCost = gasUsed * 0.0589
elif gasPlan == 'GFLR':   
        gasCost = gasUsed * 0.0393 
else:
     print("That is not a valid plan!")
# Calculate total cost #



totalCosttaxless = fixedMonthlyFee + fixedTransactionFee + electricityCost + gasCost
totalCosttax = totalCosttaxless * taxRates[province]
totalCost = totalCosttaxless + totalCosttax


print(f"Thank you! Your total amount due is now: {totalCost:.2f}")

