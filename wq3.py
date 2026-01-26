# accept a number and check whether it is a pallindrome or not 

a = int (input ("enter the number for which you want to check the pallindrome :"))

#lets create a variable which will store the value of the a because at last the value of the a will be updated to the other value 

copy = a 

rev = 0 

while a >0 :
    rev = rev *10 + a % 10 
    a = a //10


if copy == rev : 
    print ("your number is pallindrome.")
else :
    print ("your number is not a pallindrome .")
