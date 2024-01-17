x = int(input("enter the number"))
reverse = 0
while (x != 0):
    reminder = x % 10
    reverse = (reverse * 10 )+ reminder
    x = int(x / 10)
print(reverse)
