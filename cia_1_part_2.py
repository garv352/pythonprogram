

#taking principal amount from the user
p = float(input("Enter the amount = "))


#explaining loan type
print("Choose 'a' for home loan")
print("Choose 'b' for car loan")
print("Choose 'c' for Two wheeler loan")
print("Choose 'd' for personal loan")

#taking loantype from the user
loantype =  input("Please the type of the loan = ")



#taking interest rate and time from user for his home loan
if loantype == "a":
    r = float(input("Enter the interest rate = "))
    if r > 10:
        print("Interest rate should be less than 10%")
        exit()
    t = float(input("Enter the time period = "))
    if t < 5 or t > 25:
        print("Tenure should be in between 5years - 25years")
        exit()
    #applying formula after taking required values 
    amt = p*(1+ (r/100))**t
    #printing final answer
    print("Final Amount for Home loan is", amt)

#taking interest rate and time from user for his car loan        
if loantype == "b":
    r = float(input("Enter the interest rate"))
    if r < 11.45 or r > 13.75:
        print("Interest rate should be lies between 11.45%-13.75%")
        exit()
    t = float(input("Enter the time period"))
    if t < 3 or t > 7:
        print("Tenure should be in between 3years - 7years")
        exit()
        #applying formula after taking required values 
    amt = p*(1+ (r/100))**t
     #printing final answer
    print("Final Amount for your Car loan is", amt)
    
#taking interest rate and time from user for his two wheeler loan 
if loantype == "c":
    r = float(input("Enter the interest rate = "))
    if r < 12.15 or r > 13.95:
        print("Interest rate should be lies between 12.15%-13.95%")
        exit()
    t = float(input("Enter the time period = "))
    if t < 3 or t > 5:
        print("Tenure should be in between 3years - 5years")
        exit()
    #applying formula after taking required values 
    amt = p*(1+ (r/100))**t
     #printing final answer
    print("Final Amount your Two wheeler loan is", amt)

#taking interest rate and time from user for his personal loan 
if loantype == "d":
    r = float(input("Enter the interest rate = "))
    if r < 10.75 or r > 14.5:
        print("Interest rate should be lies between 10.75%-14.5%")
        exit()
    t = float(input("Enter the time period = "))
    if t < 3 or t > 5:
        print("Tenure should be in between 3years - 5years")
        exit()
     #applying formula after taking required values 
    amt = p*(1+ (r/100))**t
     #printing final answer
    print("Final Amount your personal laon is", amt)

