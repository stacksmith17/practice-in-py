# this dq will contain the questions related to the dictionary questions 
#Write a Python script to merge two Python dictionaries


#let 
d1 = {10:100, 20:200}
d2 = {30:300,40:400}

d1.update(d2) # this is the first method of the using the update function 


print (d1)

# using the loop we can merge them 

for i in d2 :
    d1[i]=d2[i]

print (d1)
