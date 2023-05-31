names = "Rina"
def greet_user(name):
    print(f"hello {name} !")
    print('welcome home')

print("start")
greet_user("john")

greet_user(names)
print("finish")

#using key word argument

def greet_user(first_name,last_name):
    print(f"hello {first_name} {last_name} !")
    print('welcome home')

print("start")
greet_user(last_name="john",first_name="smith") # last name and firstname defined on argument are keyword argument
print("finish")
