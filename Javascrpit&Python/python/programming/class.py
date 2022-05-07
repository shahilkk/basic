class Laptop:
    lap_name='HP'
    lap_ram='8Gb'
    def poweron(self):
        print(' laptop power on')
    def powerof(self):
        print('laptop power off')
    def print(self):
        print('print item')    

laptop1=Laptop()
laptop1.powerof()        
laptop2=Laptop()
laptop2.poweron()
laptop1.print()





