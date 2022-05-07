mark=[]
for i in range(0,5):
    a=int(input("enter the mark  "))
    mark.append(a)
sum=0
for j in mark:
    sum+=j
print(' total mark obtained',sum)  
avg=sum/len(mark)
print(' avg is',avg)
totalmark=len(mark)*100
per=(sum/totalmark)*100
print(' Percentage',per) 
if per<100 and per>=90:
    print('A grade')
elif per>=80:
    print('B grade')
elif per>=70:
    print('C grade')
elif per>=60:
    print('D grade')
elif per>=50:
    print('E grade') 
else:
    print('failed')           
