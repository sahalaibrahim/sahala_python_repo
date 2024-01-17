number = int(input("enter the num"))


def multiplicationUsingForLoop():
    for i in range(1, 11):
        print(i, "*", number, "=", i * number)


def multiplicationUsingWhile():
    i = 1
    while i <= 10:
        print(i, "*", number, "=", i * number)
        i += 1


n = int(input("press 1 for using for loop 2 for using while loop"))
if n == 1:
    multiplicationUsingForLoop()
else:
    multiplicationUsingWhile()
