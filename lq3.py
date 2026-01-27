# Find the greatest element and print its index too

# let the list be l = [20,98,33,69,96,100]
l = [20,98,33,69,96,100]

largest = l[0]
index=0

for i in range (len(l)):
    if l[i]>largest :
        largest = l[i]
        index = i 

print (f"your largest element in the list is {largest} at index {index}")