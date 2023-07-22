class Organism:
    alive = True 

class Animal(Organism):
    
    def eat(self):
        print("this dog is barking")

class dog(Animal):
    def talk(self):
        print("it barks")


dog = dog()
print(dog.alive)
dog.eat()
dog.talk()
