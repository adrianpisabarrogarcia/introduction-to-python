array = ["separar"]
'''separate each letter in the string'''
for i in range(len(array[0])):
    array.append(array[0][i])
array.remove("separar")
'''print the array'''
print(array)
