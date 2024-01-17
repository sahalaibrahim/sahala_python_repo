name = input("enter the name")
length = len(name)
isPal = True
print(name)
for i in range(0, (int(length / 2))):
    if name[i] != name[length - i - 1]:
        isPal = False
        break
if isPal:
    print(name, "Is palindrome")
else:
    print(name, "is not palindrome")
