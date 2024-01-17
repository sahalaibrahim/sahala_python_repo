inputString = input("Enter a string:")
vowelCount = 0
for char in inputString:
    if (char == 'a' or char == 'A' or char == 'i' or
            char == 'I' or char == 'o' or char == 'O' or char == 'e' or char == 'E' or
            char == 'u' or char == 'U'):
        vowelCount += 1

print("Total Vowels:", vowelCount)
print("Total Consonents:", len(inputString) - vowelCount)