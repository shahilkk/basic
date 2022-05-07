class Product:
   
    def calc_price(self):
        print("haai")

class Sales(Product):
    def display(self):
        print("wow")

    def calc_price(self):
        print("hello")        

product1=Product()
product1.calc_price()

sales1=Sales()
sales1.calc_price()