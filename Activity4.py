a = int(input("Enter first speed: "))
b = int(input("Enter second speed: "))
c = int(input("Enter third speed: "))

mean = (a + b + c)/3
print(mean)

if a or b or c < mean:
    print("One of your speeds are less than the mean")
else:
    print("All of your speeds are more than the mean")