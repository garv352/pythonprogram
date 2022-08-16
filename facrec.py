n = int(input("Enter the Number"))
fac = 1
if int(n) >= 1:
    for i in range(1,25):
        fac = fac * i
        print(i, "Factorial of", n, "is:", fac)

