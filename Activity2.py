numerator = int(input("Give me a numerator number: "))
denominator = int(input("Give me a denominator number: "))



if numerator%denominator == 0:
    print(numerator, "can be divided by", denominator)
else:
    print(numerator, "can not be divided by", denominator)

