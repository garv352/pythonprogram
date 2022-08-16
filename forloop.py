num = int(input("Enter the number"))
print("The Multiplication Table of:", num)

def table():
      for count in range(1,11):
            print(num,'x',count,'=',num*count)

table()
