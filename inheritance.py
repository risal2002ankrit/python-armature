class Mammels:
    def walk(self):
        print("walk")
class Dog(Mammels):        #syantax: Class derived_class(parent_class)
    pass

class cat(Mammels):
    def talk(self):
        print("cat meow")


dog1=Dog()
dog1.walk()

cat1=cat()
cat1.walk()
cat1.talk()

