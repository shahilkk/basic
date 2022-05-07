class Product:
    __product_Id=0
    def __init__(self,product_name,price,category,count):
        self.product_name=product_name
        self.price=price
        self.category=category
        self.count=count
        print(self.__product_Id)
    def display(self):
        print(self.product_name,self.price,self.category,self.count) 
p1=Product('orange',25,'fruits',4)        
p1.display()
