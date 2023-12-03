my_tuple = tuple(range(3))
my_list = list(range(3))
my_set = set(range(3))
my_dict = {i: f"value_{i}" for i in range(3)} 
my_dict_2 = {i: number for i, number in enumerate(range(5, 8))}
my_other_dict = {f"key_{i}": i for i in range(3)} 
my_string = ''.join(str(i) for i in range(3))
my_other_string = ''.join(map(str, range(3)))

#Using range in a for loop with lists, tuples, dictionaries, strings

print(my_tuple)
print(my_list)
print(my_set)
print(my_dict)
print(my_other_dict)
print(my_string)
print(my_other_string)

# Using range in a for loop with different data structures

# List
colors = ["red", "green", "blue", "yellow" ]
for i in range(len(colors)):
	print(colors[i])

for color in colors:
	print(color)

# Dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

for key in person:
	print(key)

for value in person.values():
	print(value)

for key, value in person.items():
	print(key, value)

# Tuple

coordinates = {10, 20, 30}
for coordinate in coordinates:
	print(coordinate)

# Strings

text = "hello"
for i in range(len(text)):
	print(text[i])

for char in text:
	print(char)
