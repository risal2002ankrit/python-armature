customer ={
    "name": "Ankrit Risal",
    "age":21,
    "is_verified": True
}
print(customer)
print(customer["name"])
'''print(customer["birthdate"]) # key error'''
print(customer.get("birthdate"))
print(customer.get("birthdate", "March 4 2002"))

#adding new key or modifying existing key
customer["name"]= "Hari Khadka"
print(customer["name"])

customer["birthdate"]= "2058 Falgun 20"
print(customer["birthdate"])





