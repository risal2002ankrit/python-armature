class Mammels:
    def mammals(self):
        print("it is an mammals")
    def walk(self):
        print("it can walk")
    def eat(self):
        print('it can eat')

class Dog(Mammels):        #syantax: Class derived_class(parent_class)
    def talk(self):
        print('dog barks')

class cat(Mammels):
    def talk(self):
        print("cat meow")


dog1=Dog()
dog1.mammals()
dog1.walk()
dog1.eat()
dog1.talk()
print("now, for cats")
cat1=cat()
cat1.mammals()
cat1.walk()
cat1.talk()
cat1.eat()


