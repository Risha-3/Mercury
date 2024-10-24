import random

random_numbers = []

for _ in range(10):
    random_numbers.append(random.randint(1,100))
print("The list of ten random numbers are: ", random_numbers)

i = 0
while i < len(random_numbers):
    if random_numbers[i] % 2 == 0:
        random_numbers.pop(i)
    else:
        i += 1


print("The remaining odd numbers are: ", random_numbers)
