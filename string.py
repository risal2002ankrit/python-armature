course=" 'Python's course for begineers\n"
print(course)
course='Pythons course for "begineers"'
print(course)
#email pattern
email ='''
Hi Ram
this is out first email to you.

thank you,

the team supports
'''
print(email)

#index of the string 
course='Pythons course for "begineers"'
# here  0123456 so index of 1=y  print's
print(course[1])
#-2 means index from the last 
print(course[-2])
# print index form 0,1,2 ie 0 to 2 but not 3
print(course[0:3])
#exclude 1st char and print remaining all
print(course[1:])
# starts form 0(start index) to 5(end index)
print(course[:5])
# using another varible 
another= course[:]
print(another)




