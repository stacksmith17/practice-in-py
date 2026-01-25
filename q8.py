# Print all the factors of a number
n = int (input("tell the number of which the factors you want:"))

for i in range (1,n+1):
    if n%i==0:
        print (i )