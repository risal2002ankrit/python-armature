#to remove dublicate in a list
numbers =[1,5,9,7,5,6,9,1,4]
list=[]
for num in numbers:
    if num not in list:
        list.append(num)
       
print(list)
