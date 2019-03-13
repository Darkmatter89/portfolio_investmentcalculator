
P = float(input("Enter deposit amount: "))
i = float(input("Enter interest rate: "))
t = float(input("Enter number of years: "))
interest = str(input("Enter interest type, 'simple' or 'compound': ").lower())

if interest == "simple":
    pay = P *((1+(i/100)) * t)
    print("You will get paid R" + str(round(pay,2)))
elif interest == "compound":
    pay = P * (1 + (i/100))**t
    print("You will get paid R" + str(round(pay,2)))
