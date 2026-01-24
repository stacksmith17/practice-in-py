# factorial of a number 
n = int (input ("please enter number you want the factorial of :"))


fact = 1 
for i in range (1,n+1):
    fact = fact*i

print (f"your factorial is {fact}")