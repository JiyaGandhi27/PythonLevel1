import random

max_length = 6

numbers = ['0','1','2','3','4','5','6','7','8','9']

combinedList = numbers

randomNumbers = random.choice(numbers)

password = randomNumbers

for i in range(max_length-1):
    password = password + random.choice(combinedList)

print(password)