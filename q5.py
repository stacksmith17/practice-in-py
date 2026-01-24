# sum upto n terms 

n = int (input ("enter the number to which you need the sum of "))
sum = 0 

for i in  range (1,n+1):
    sum = sum + i 
print (f"your sum is {sum}")