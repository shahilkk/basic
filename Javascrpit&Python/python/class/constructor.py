class employee:
    count=0
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        employee.count+=1
    def view(self):
        print(self.name,self.age,self.place)
    def total(self):
        print('total count: ',employee.count)    

emp1=employee('shahil',21,'agkg')  
emp2=employee('harshin',11,'agkg')  
emp3=employee('sreee',21,'agkg')  

emp1.view() 
emp2.view() 
emp3.view() 
emp3.total()

# using for loop

# for i in range(3):
#     name=input('enter a name ')
#     age=int(input('enter a age '))
#     place=input('enter a place ')
#     emp=employee(name,age,place)
#     emp.view()



    