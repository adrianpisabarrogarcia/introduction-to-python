'''create an arra of random numbers'''
import random
array_of_numbers = []
for i in range(10):
    array_of_numbers.append(random.randint(0, 100))
print("antes de ordenar: ", array_of_numbers)
array_of_numbers.sort()
print("despues de ordenar: ", array_of_numbers)

