#Paulina Romo Villalobos
def findThrees(m):
    sum = 0
    for p in m:
        if(p % 3 == 0):
            sum = sum + p
    return sum

l = []
print ("Press 0 to stop the program.")
n = (input("Enter a number: "))
while (n!="0"):
    l+= [int(n)]
    n = (input("Enter another number: "))
print(findThrees(l))
