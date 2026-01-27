# Find the second greatest element 
# lets take the list l = [17,19,21,14,15]
l = [17,19,21,14,15]

largest = l[0]
sec_largest = l[0]

for i in l :
    if i > largest :
        sec_largest = largest 
        largest = i 
    elif i> sec_largest :
        sec_largest = i

print (sec_largest , largest )