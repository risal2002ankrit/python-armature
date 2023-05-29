'''name ="J"

if len(name) < 3 :
    print("name must be at least 3 character")
elif len(name) > 50:
    print("name must be a maximum 50 character ")
else:
    print("name look good ")
'''
name = input("enter your name ")
if len(name) < 3:
    print("string must be of minimum 3 character")
elif len(name) > 50:
    print("string must be of maximum of 50 character")
else:
    print("name looks good")
