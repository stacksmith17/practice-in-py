# Count all letters, digits, and special symbols from a given strings 
# Given: str1 = "P@#yn26at^&i5ve" 
""" Expected Outcome:
Total counts of chars, digits, and symbols
Chars = 8
Digits = 3
Symbol = 4 """
a = "P@#yn26at^&i5ve" 
char = 0
digits = 0
symbol = 0
for i in a :
    if i.isdigit():
        digits +=1
    elif i.isalpha():
        char+=1
    else:
        symbol +=1

print (f" char = {char}\ndigits = {digits}\nsymbol = {symbol}")