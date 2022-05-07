

class Customer:
    def __init__(self,c_name,c_id):
        self.c_name=c_name
        self.c_id=c_id

class Product:
    def __init__(self,p_price,p_name,p_id):
        self.p_price=p_price
        self.P_name=p_name
        self.p_id=p_id        

class Sales(Customer,Product):
    def __init__(self,c_name,c_id,p_name,p_price,p_id,qua):
        Customer.__init__(self,c_name,c_id)
        Product.__init__(self,p_price,p_name,p_id)
        self.qua=qua
    def display(self):
        total_am=self.p_price*self.qua
        print('customer name is', self.c_name)
        print('customer id is', self.c_id)
        print('product name is', self.P_name)
        print('product price is', self.p_price)
        print('product id is', self.p_id)
        print('quantity',self.qua)
        print('total price is',total_am)
per1=Sales('shahil',21,'shoe',2500,34,4)  
per1.display()      