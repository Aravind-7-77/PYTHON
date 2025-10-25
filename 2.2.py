class animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
       print(f"{self.name}is eating,")
class dog(animal):
    def bark(self):
       print(f"{self.name}is barking.")
class cat(animal):
    def meow(self):
       print(f"{self.name}is meowing.")
dog=dog("buddy")
cat=cat("whiskers")
dog.eat()
dog.bark()
cat.eat()
cat.meow()
