# check whether list is sorted or not 

# lets take the list l=[1,2,3,4,5,6,7,8.9]

l=[1,2,3,4,5,6,7,8.9]

for i in range (len(l)-1):
    if l[i]<l[i+1]:
       continue 
    else:
        print ("your list is not sorted")  
        break
else :
    print ("your list is sorted")  