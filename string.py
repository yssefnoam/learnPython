data = "welcome to first app in python"
print(len(data)) # the length of the string
print(data.upper()) # the string to upper
print(data.lower()) # the string to lower
print(data.split()) # split the string whit spaces
print(data.split("i")) # split the string whit i
x = data.split()
print(x)
y =":".join(x)
print(y)
y =" ".join(x)
print(y)
print(data.find("first")) # find a match
print(data.capitalize())
print("{} {}".format(10, 5))