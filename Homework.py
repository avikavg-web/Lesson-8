x = 300
y = 100
z = 700

print("These are the wrong order numbers:")
print("x =", x)
print("y =", y)
print("z =", z)

x, y, z = y, z, x

print("These wre the actual values")
print("x =", x)
print("y =", y)
print("z =", z)