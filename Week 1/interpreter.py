equation = (input("Expression:"))

x, y, z = equation.split() 
x = int(x)
z = int(z)

# Return only works inside of a function
if y == "+":
    value = x + z

elif y ==  "-":
    value = x - z

elif y == "*":
    value = x * z

elif y == "/":
    value = x / z
# As it is a format specifier, and therefore must be inside a string, typically f-string.
print(f"{value:,.1f}")


