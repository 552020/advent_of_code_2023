# Python doesn't have array but lists
colors = ["red", "green", "blue", "purple"]

print("Looping directly over elements:")
for color in colors:
	print(color)

print("\nLooping over indices of the list:")
for i in range(len(colors)):
	print(i, colors[i])

print("Looping over indices and elements of the list")
for i, color in enumerate(colors):
	print(i, color)

print("Just the length of the array 'colors'")
print("I mean: of the list 'colors'")
print(len(colors))

# range is a function
	