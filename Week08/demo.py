my_var = 2
print(my_var)
print(type(my_var))
my_var = 2.0
print(my_var)
print(type(my_var))
my_var = "2"


my_dict = {
    "name": "Fred",
    "age": 30,
    "city": "New York"
}
my_dict['name'] = "Jane"
print(my_dict['name'])
print(my_dict['age'])
print(my_dict.get('address', 'No address found'))