trans = int(input("num"))

cost = 200000
revenue = 85000





def pandl(revenue):
    revenue = revenue + trans
    if revenue > cost:
        print("Total revenue is : ", revenue , "and it's profit")
        print(revenue)
        pandl(int(trans))

    elif revenue < cost:
         print("Total revenue is : ", revenue , "and it's loss")
         print(revenue)
         pandl(int(trans))
    else:
        print(revenue)

print(pandl(int(trans)))


    
