from itertools import count, product
from tkinter.messagebox import showerror
from traceback import print_exception
from unicodedata import category


class Product:
    product_name=""
    price=0
    category=""
    count=0
    def addproduct(self,product_name,price,category,count):
        self.product_name=product_name
        self.price=price
        self.category=category
        self.count=count
    def display(self):
        print(self.product_name,self.price,self.category,self.count)    
pro1=Product()  
pro1.addproduct('shoe',2500,'casual',2)      
pro1.display()
pro1.product_name='shirt'
pro1.price=999
pro1.display()  

pro2=Product()
pro2.addproduct('mobile',7000,'iphone',2)
pro2.display()
        