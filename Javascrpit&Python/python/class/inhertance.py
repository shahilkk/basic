class Student:
    def __init__(self,name):
        self.name=name
    def dis(self):
        print(self.name)       
class Division(Student):
    def __init__(self,roll,name):
        self.roll=roll
        Student.__init__(self,name)
    def dis(self):
        print(self.roll) 
        print(self.name)   



div=Division(43,'shadil')
div.dis()





# simple model
class Student:
    name="harshin"
class Division(Student):
    roll=23
  

div1=Division()
print(div1.name)
# end