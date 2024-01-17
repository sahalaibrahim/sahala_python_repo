limit = int(input("enter the limit"))
for i in range(1,limit + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif (i % 3 == 0):
        print("fizz")
    elif (i % 5 == 0):
        print("buzz")
    else:
        print(i)
