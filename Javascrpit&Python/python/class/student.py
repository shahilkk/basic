class student:
    id=12
    name='shahil'
    age=22
    gender='male'
    course='computer science'
    fee=35000
    def display(self):
        print(self.id,self.name,self.course,self.age,self.fee)

stu=student()
stu.display()
print(stu.name)