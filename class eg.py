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

#student class
class student:
    def __init__(int, name, branch,id,phno):
        int.name=name
        int.branch=branch
        int.id=id
        int.phno=phno
student1=student("yamini","cse","24b11cs146",9505402611)
student2=student("josh","eee","24b11ee119",9959671921)
print(student1.name)
print(student2.phno)



#student class
class student:
    def __init__(nippu, name, branch,id,phno):
        nippu.name=name
        nippu.branch=branch
        nippu.id=id
        nippu.phno=phno
student1=student("yamini","cse","24b11cs146",9505402611)
student2=student("josh","eee","24b11ee119",9959671921)
print(student1.name)
print(student2.phno)
