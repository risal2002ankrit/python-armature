weight= input("enter your weight")
unit = input ("(L) lbs or (K) kg:")
 
if unit.upper() == "L":
    converted = int(weight)* 0.45
    print (f"you are {converted} kilos")

if unit.upper() == "K":
    converted = int(weight)/ 0.45
    print (f"you are {converted} kilos")