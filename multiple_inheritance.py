class Prey:
    def flee(self):
        print("this animal flees")

class Predetor:
    def hunt(self):
        print("this animal is hunting ")

class Rabbit(Prey):
    pass

class Hwak(Predetor):
    pass

class fish(Prey,Predetor):
    pass 


rab = Rabbit()
Hwk = Hwak()
fsh = fish()

rab.flee()
fsh.flee()


