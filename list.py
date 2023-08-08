#list = [1, 2, 3, 400, 5, 6, 7, 8, 100]
#max = list[0]

#print(max(list))

#for number in list:
#    if number > max:
#        max = number
#print(f'{max} is the largest number.')

#matrix = [
   # [1, 2, 3],
   # [4, 5, 6],
   # [7, 8, 9]
#]

#print(matrix[2][2])

#for loop in matrix:
#    for repeat in loop:
#        print(repeat)

#numbers = [15, 5, 5, 8, 1, 17, 5, 23, 2, 17]
#unique_numbers = []
#for number in numbers:
#        if number not in unique_numbers:
            #unique_numbers.append(number)
#print(unique_numbers)


#list = [1, 4, 8, 3, 6]
#max = list[0]

#for number in list:
#    if number > max:
#        max = number
#print(max)

list = [2, 8, 4, 7, 1, 8, 4, 6]
unique = []

for number in list:
    if number not in unique:
        unique.append(number)
print(unique)