# escape sequence charcters (\n) ie: new line character
#{ here # is the single line comment syntax }
print("hey i am a good boy\n and i am good at this") 

''' this is the multi line comment '''
'''hello ! 
my name is ankrit 
i am current an IT student '''
""" double quote can also be used as comment line """
#using double quote escape sequence ie: \" and \"
print("hey i am \"a good boy\"\n and i am good at this")

#using single quote escape sequence ie: \' and \'
print('hey i am \'a good boy\'\n and i am good at this')

# multiple values in print statement 
print ("hey",6,sep="~",end="009\n") #sep= seperator
print("hello")

#data types 
a=8
b=12.02
c=False
print(a,b,c)
print("a =",type(a))
print("b =",type(b))
print("c =",type(c))

# list= mutable(can be changed with time)
list1=[8,5.4,34,65]
print(list1)

#tuple =immutable(cannot be change with time)
tuple=[("hen","parrot"),("cow","dog")]
print(tuple)

#dictonary unorderd collection of data 
dict={"name":"ankrit","age":22,"rollno":13}
print(dict)

#using operators 
a=50;
b=15;
print("the sum is",a,"+",b,"is:",a+b)
sum=a+b
print("the value of a+b is :",sum)
