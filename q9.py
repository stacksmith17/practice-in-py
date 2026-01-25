#Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself . 
n = int (input ("enter the number for which you need to find wether it is perfect or not :"))

sum = 0

for i in range (1,n):
    if n%i==0:
        sum = sum +i 

if sum == n :
    print ("your number is perfect")
else :
    print ("your number is not perfect")
    
