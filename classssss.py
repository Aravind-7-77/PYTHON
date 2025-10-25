class student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    
    def display(self):
        print("Student Name:{}\nRollno:{}\nMarks:{}".format(self.name,self.rollno,self.marks))
s1=student("Esther",496,80)
s1.display()
s2=student("Sunny",102,10)
s2.display()
