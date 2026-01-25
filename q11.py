# Reverse a string without using in build functions.
s = input ("enter a string :")

rev = ""

for ch in s:
 rev = ch + rev 

print ("reversed string ", rev )