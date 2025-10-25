#car class
class car:
    def __init__(int, make, model, year, color):
     int.make=make        #instance attributes
     int.color=color
     int.model=model
     int.year=year
     int.speed=0          #default value
     #creating instances(objects)of car
car1=car("toyato","carry",2022,"red")
car2=car("ford","mustang",2023,"black")
print(car1.make)
print(car2.speed)
