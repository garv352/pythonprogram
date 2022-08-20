f = open("Untitled.txt", "r")
for x in f:
    print(x)
f.close()





#close



f = open("untitled.txt", "r")
print(f.readline())
f.close()



#append and write

f = open("untitled.txt", "w")
f.write("HELLU")
f.close()



f = open("untitled.txt", "r")
print(f.readline())
f.close()
