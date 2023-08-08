#Chapter 1.6 Exercises

#Exercise 1: Mailing Address
#Create a program that displays your name and complete mailing address. The address
#should be printed in the format that is normally used in the area where you live. Your
#program does not need to read any input from the user.

#print('My Name is:\n\t Sharod Williams\nMy mailing address is:\n\t123 Main St.\n\tEast Lansing, MI 48824')

#Exercise 3: Area of a Room

#Write a program that asks the user to enter the width and length of a room. Once
#these values have been read, your program should compute and display the area of
#the room. The length and the width will be entered as floating-point numbers. Include
#units in your prompt and output message; either feet or meters, depending on which
#unit you are more comfortable working with.

#width = int(input('What is the width of your room? '))
#length = int(input('What is the length of your room? '))
#area = width*length
#print(area)

#2.5 Nested If Statements
#num = float(input('Enter a number: '))

#if num > 0:
#    adjective = ' '
#    if num >= 100000:
#        adjective = ' really big '
#    elif num >= 1000:
#        adjective = ' big '
#    result = "That's a" + adjective + 'positive number'
#elif num < 0:
#    result = "That's a negative number"
#else:
#    result = "That's zero"
#print(result)

#Exercise 35: Even or Odd?
#Write a program that reads an integer from the user. Then your program should
#display a message indicating whether the integer is even or odd.

#num = int(input('What is your number? '))
#if num % 2 == 0:
#    print('Your number is even.')
#else:
#    print('Your number is odd')

#xercise 36:Dog Years

#It is commonly said that one human year is equivalent to 7 dog years. However this
#simple conversion fails to recognize that dogs reach adulthood in approximately two
#years. As a result, some people believe that it is better to count each of the first two
#human years as 10.5 dog years, and then count each additional human year as 4 dog years.

#Write a program that implements the conversion from human years to dog years
#described in the previous paragraph. Ensure that your program works correctly for
#years. Your program should display an appropriate error message if the user enters
#a negative number.

#dog_age = int(input('How old is your dog? '))
#dog_to_human_age = 0
#if dog_age > 2:
#    dog_to_human_age = round((10.5*2)+((dog_age-2)*4))
#else:
#    dog_to_human_age = round(10.5*dog_age)
#print('Your dog is', dog_to_human_age, 'years old')
#Exercise 37:Vowel or Consonant
#In this exercise you will create a program that reads a letter of the alphabet from the
#user. If the user enters a, e, i, o or u then your program should display a message
#indicating that the entered letter is a vowel. If the user enters y then your program
#should display a message indicating that sometimes y is a vowel, and sometimes y is
#a consonant. Otherwise your program should display a message indicating that the
#letter is a consonant.
#vowels = ['a', 'e', 'i', 'o', 'u']
#letter = input("Enter a letter: ")

#if letter in vowels:
#    print(f'{letter} is a vowel.')
#elif letter == 'y':
#    print("Sometimes 'y' is a vowel and sometimes 'y' is a constant.")
#else:
#    print(f'{letter} is a constant.')

#Exercise 38:Name That Shape

#Write a program that determines the name of a shape from its number of sides. Read
#the number of sides from the user and then report the appropriate name as part of
#a meaningful message. Your program should support shapes with anywhere from 3
#up to (and including) 10 sides. If a number of sides outside of this range is entered
#then your program should display an appropriate error message.

#sides = int(input('How many sides are in your shape? '))
#shapes = {'Triangle': 3, 'quadrilateral': 4, 'Pentagon': 5, 'Hexagon': 6, 'Heptagon': 7, 'Octagon': 8,
#          'Nonagon': 9, 'Decagon': 10}

#if sides == shapes.values():
#    print(shapes.keys())
#else:
#    print('Number of sides entered is outside of this range.')

#5.2 Loops and List
#data = [2.71, 3.14, 1.41, 1.62]
#total = 0

# find the value for all the values in data
#for value in data:
#    total += value
#print('The total is', round(total,2))

#find the largest value in data
#largest_value = 0
#for l in range(1, len(data)):
#    if data[l] > data[largest_value]:
#        largest_value = l
#print('The largest value is', data[largest_value], 'which is at index', largest_value)

#data = [0, -1, 4, 1, 0]
#i = 0

#while i < len(data) and data[i] <= 0:
#    i += 1
#if i < len(data):
#    print("The 1st positive number is at index", i)
#else:
#    print('The list does not contain a positive number')

#5.5 Exercies
#Exercise 110: Sorted Order
#Write a program that reads integers from the user and stores them in a list. Your
#program should continue reading values until the user enters 0. Then it should display
#all of the values entered by the user (except for the 0) in ascending order, with one
#value appearing on each line. Use either the sort method or the sorted function
#to sort the list.

#numbers = []
#enter = int(input('Enter a number: '))

#while enter != 0:
#    numbers.append(enter)
#    enter = int(input('Enter a number: '))
#    numbers.sort()
#print('The values, sorted into ascending order, are:')
#for enter in numbers:
#    print(enter)

#Exercise 112:Remove Outliers

#When analysing data collected as part of a science experiment it may be desirable
#to remove the most extreme values before performing other calculations. Write a
#function that takes a list of values and an non-negative integer, n, as its parameters.
#The function should create a new copy of the list with the n largest elements and the
#n smallest elements removed. Then it should return the new copy of the list as the
#function’s only result. The order of the elements in the returned list does not have to
#match the order of the elements in the original list.
#Write a main program that demonstrates your function. It should read a list of
#numbers from the user and remove the two largest and two smallest values from it by
#calling the function described previously. Display the list with the outliers removed,
#followed by the original list. Your program should generate an appropriate error
#message if the user enters less than 4 values.

#n = []
#values = int(input('Enter values from your experiment (if no more values enter 0): '))

#while values != 0:
#    n.append(values)
#    n.sort()
#    values = int(input('Enter values from your experiment (if no more values enter 0): '))
#if len(n) < 4:
#    print('ERROR! Not enough values entered!')
#print(n[0:2], n[-2:0])
#print(n[2:-2])
#print(n)
#45, 81, 79, 99, 97, 83, 66, 79, 87, 83, 86
















