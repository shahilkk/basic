# largest number & second largest
# ---------------------------------------
def gre(num):
    large=0
    second=0
    for i in num:
        if i>large:
            large=i
        if i==large:
            pass
        elif i>second:
            second=i 
    return large,second    
        

a=[7,9,801,60,544,200]
b,c=gre(a)
print('%d largest'%(b),'%d second largest'%(c))
# end largest number & second largest
# ---------------------------------------