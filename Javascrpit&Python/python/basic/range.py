
# list even number
list=[1,2,3,4,5,6,7,8,9] 
for x in range(0,len(list)):
    item=list[x]
    if(item%2==0):
        print(item)

# same as above deffent method
list=[11,12,13,14,15,16,17,18,19,10] 
for i in list:
    if(i%2==0):
        print(i)

# range working
for i in range(0,10):
    for j in range(0,10):
        print(i,j)        

# list same element display
k=[10,20,30,60,10,20,30,100,80]  
for i in k:
    for j in k:
        if(i==j):
            print(i)
    

