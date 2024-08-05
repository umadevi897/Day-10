class Bikes: # class declaration or defination
    def __init__(self,brand,mileage,cost,cc,color):
        self.a=brand
        self.x=mileage
        self.z=cost
        self.s=cc
        self.j=color

    def bike_details(self):
        print('Bike Brand',self.a)
        print('Bike Mileage',self.x)
        print('Bike Cost',self.z)
        print('Bike CC',self.s)
        print('Bike Color',self.j)
    
brands=input('Enter the Brand Name:')
Mileages=input('Enter the Mileage:')
Costs=float(input('Enter the Cost:'))
ccs=input('Enter the CC:')
colors=input('Enter the Colors:')
Bike_obj=Bikes(brands,Mileages,Costs,ccs,colors)
Bike_obj.bike_details()