from constructor  import employee


class company:
    count=0
    def __init__(self,cname,cmodel,cmilage,cmaxspeed,ccap,ccolor):
        self.cname=cname
        self.cmodel=cmodel
        self.cmilage=cmilage
        self.cmaxspeed=cmaxspeed
        self.ccap=ccap
        self.ccolor=ccolor
        company.count+=1

    def car(self):
        print('car name is',self.cname,'car model is',self.cmodel,'car milage is',self.cmilage,'car maxspeed is',self.cmaxspeed,'car site capacity is',self.ccap,'car color is',self.ccolor)
    def totalcar(self):
        print('total count: ',company.count) 
car1=company('swift',2017,17,250,5,'black')
car2=company('bmw',2021,10,320,4,'blue')
car1.car()
car2.car()
car2.totalcar()

name=employee('shahil',21,'agkg')
name.view()
