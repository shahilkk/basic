class Product:
    count=0
    def __init__(self,name,category,price):
        self.name=name
        self.category=category
        self.price=price
        Product.count+=1
    def display(self):
        print('name is',self.name)  
        print('category is',self.category)  
        print('price is',self.price)  
    def cal_price(self):
        t_price=self.price+20
        return t_price

class Sales(Product):
        def __init__(self,name,category,price,qua):
            Product.__init__(self,name,category,price)
            self.qua=qua
        def cal_price(self):
            total=Product.cal_price(self)*self.qua
            return total

prod=Product('book','note',10)    
print(prod.cal_price())            

sale=Sales('pen','stationery',20,4) 
print(sale.cal_price())            





        