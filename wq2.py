# Accept a number and print its reverse 

a = int (input ("enter the number for which you need the reverse of the number :"))

rev = 0 

while a >0 :
    rev = rev *10 + a % 10
    a = a//10 

print (f"your reverse number is :{rev}")