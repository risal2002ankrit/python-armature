phone =input("phone:")
mapping ={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output=""
for ch in phone:
   output += mapping.get(ch,"!") + " "
print(output)


