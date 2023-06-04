import random
 
members=['ram','hari','shyam','shiv']
leader = random.choice(members)
print(leader)


class dice:
    import random
    roll =(1,2,3,4,5,6)
    dice_value = random.choice(roll),random.choice(roll)
    print(dice_value)

        #OR

import random
class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second


dice=Dice()
print(dice.roll())








                


