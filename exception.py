try:
    age=int(input('age:'))
    income=20000
    risk= income / age
    print(age)
    print(risk)
    
except ZeroDivisionError:
    print("age must be greater than zero")

except ValueError :
    print("invalid value")