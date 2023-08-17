# inheritance allows one class to inherit attributes
# and methods from another class

class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class dog(animal):
    def speak(self):
        return "woof"
class cat(animal):
    def speak(self):
        return "meow"
class pig(animal):
    def speak(self):
        return "snort"
class horse(animal):
    def speak(self):
        return "neigh"
# this are objects
doggy=dog("buddy")
cat=cat("whiskers")
pig=pig("piggy")
horse=horse("horsey")
print(doggy.speak())
print(cat.speak())
print(pig.speak())
print(horse.speak())