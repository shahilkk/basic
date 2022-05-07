

array1=[10,30,70,85,37,87]
temp=0
def sort(val):
    for i in range(0,len(val)):
        for j in range(0,len(val)):
            if val[i]<val[j]:
                temp=val[i]
                val[i]=val[j]
                val[j]=temp
    print(val) 

sort(array1)               


        
            


        
