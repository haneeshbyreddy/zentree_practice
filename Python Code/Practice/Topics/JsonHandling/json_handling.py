import json

# Dictionary to JSON
# dictionary to json object
my_dict = {'name': 'rob', 'age': '24', 'married': False, ('2023', '2024'): 'New York'}
with open('JsonFile.json', mode='w', encoding='utf-8') as write_file:
    json.dump(my_dict, write_file, skipkeys=True)


# adding json object to json object from file
my_dict_1 = {'name': 'robert', 'age': '28', 'married': True, ('2023', '2024'): 'Singapore'}
arr = []
with open('JsonFile.json', mode='r', encoding='utf-8') as read_file:
    my_dict_temp = json.load(read_file)
    if type(my_dict_temp) is list:
        arr = my_dict_temp
    else:
        arr.append(my_dict_temp)
    arr.append(my_dict_1)
with open('JsonFile.json', mode='w', encoding='utf-8') as write_file:
    json.dump(arr, write_file, skipkeys=True)
