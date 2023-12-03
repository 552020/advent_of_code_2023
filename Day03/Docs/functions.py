def my_function():
  print("Hello from a function")

my_function()

def my_other_function(name):
  print("Hello from " + name)

my_other_function("Emil")
my_other_function("Tobias")
my_other_function("Linus")

def my_third_function(greeting, name):
  print(greeting + " from " + name)
greeting = "Hello"
other_greeting = "Cheers"
my_third_function(greeting, "Emil")
my_third_function(other_greeting, "Tobias")
my_third_function("Bye", "Linus")

def my_function_with_return(x):
  return 5 * x

print(my_function_with_return(3))
print(my_function_with_return(5))
print(my_function_with_return(9))