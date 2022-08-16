num = input("Enter a number")
def recur_fac(n):
    if n ==1:
        return n
    elif n < 1:
        return("NA")
    else:
        return n * recur_fac(n-1)
print(recur_fac(int(num)))
