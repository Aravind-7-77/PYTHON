class animal:
    def make_sound(self):
        print("some generic animal sound.")
class dog(animal):
    def make_sound(self):
        print("woof!")
class cat(animal):
    def make_sound(self):
        print("meow!")
class bird(animal):
    def make_sound(self):
        print("tweet!")
animals=[dog(),cat(),bird()]
for animal in animals:
    animal.make_sound()


                                   
