class Person:
    def __init__(self ,A):       #constructor
        self.A = A

    def talk(self):
        print("hello, it's me {self.A}")
    
    

person= Person("ram")
print(person.A)
person.talk()
