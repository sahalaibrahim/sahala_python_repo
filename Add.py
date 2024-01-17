# This program is to add numbers from 1 to entered number
x = int(input("enter the number"))
print ("you entered",x)
s = 0
for i in range(x + 1):
    s = s + i
print ("sum is:", s)
