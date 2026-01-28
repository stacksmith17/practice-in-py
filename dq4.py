# Write a Python program to combine two dictionary by adding values for common keys.

d1 ={10:100,20:200,30:300}
d2 = {20:200,30:300,40:400}

for i in d2 :
    if i in d1.keys():
        d1[i]+=d2[i]
    else :
        d1[i]=d2[i]


print (d1)

