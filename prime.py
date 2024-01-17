def checkPrime():
    x = int(input("enter the num"))
    f = 0
    if x == 0 or x == 1:
        print("neither prime")
        return

    for i in range(2, int(x / 2)):
        if x % i == 0:
            f = 1
            break
    if f == 0:
        print("prime")
    else:
        print("not prime")


print ("execution started")
checkPrime()
print ("execution ended")