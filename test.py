#numbers = [5, 2, 5, 2, 2]
#value_x = 0
#for x in numbers:
    #for value in numbers:
        #print(f'{value_x}'*(numbers))
#for x in numbers:
    #for multi in numbers:
        #print(multi * 'x')
    #print()
#for x_count in numbers:
    #output = ''
    #for count in range(x_count):
       # output += 'x'
   # print(output)

#numbers = [1, 1, 1, 1, 5]

#for x_count in numbers:
    #output = ''
    #for count in range(x_count):
        #output += 'x'
    #print(output)


#secert_number = 38


#for number in range(1,4):
#    guess = int(input('>'))
#    print('Attempt', number)
#    if guess > secert_number:
#        print(f'{guess} is too high.')
#    elif guess < secert_number:
#        print(f'{guess} is too low.')
#    elif guess == secert_number:
#        print('Ding! ' * 3 + f'{guess} is correct!')
#        break
#else:
#    print('No more attempts remaining.')


#weight = float(input('Weight: '))
#unit = input('unit: ').lower()

#for symbol in unit:
#    if unit == 'lbs':
#        converted = weight*0.45
#        print(str(converted) + ' kg')
#        break
#    elif unit == 'kg':
#        converted = weight/0.45
#        print(str(converted) + ' lbs')
#        break

#command = ''
#started = False

#while True:
#    command = input('> ').lower()
#    if command == 'help':
#        print('''
#type strat - to start car
#type stop - to stop car
#type exit - to exit game
#''')
#    elif command == 'start':
#        if started:
#            print('Car is already started!')
#        else:
#            started = True
#            print('Car started.')
#    elif command ==  'stop':
#        if not started:
#            print('Car has already stopped!')
#        else:
#            started = False
#            print('Car stopped.')
#    elif command == 'exit':
#        break
#    else:
#        print("I don't understand that command.")

#numbers = [1, 1, 1, 1, 10]

#for number in numbers:
#    letter = ''
#    for count in range(number):
#        letter += 'l'
#    print(letter)

#data = [7, 0.00002, 0.8, 3, 400, 10]
#value = data[0]
#for number in data:
#    if number < value:
#        value = number
#print(f'{value} is the largest number.')

#data_set = [3, 7, 7, 9, 5, 3, 2, 6]
#new_data_set = []

#for number in data_set:
#    if number not in new_data_set:
#        new_data_set.append(number)
#print(new_data_set)

#phone_number = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four'}
#phone = ''
#digits = input('Phone: ')

#for numbers in digits:
#    phone += phone_number.get(numbers, '!') +' '
#print(phone)

#constants = {'pi':3.14, 'e':271, 'root':1.14}
#print(constants)

#total = 0
#for sum in constants.values():
#    total += sum
#print(total)

#def reverse_lookup(keys, values):


#Guessing Game
#secert_num = 19
#guess_count = 0
#guess_count_max = 3

#while guess_count != guess_count_max:
#    guess = int(input('Guess a number: '))
#    guess_count += 1
#    if guess < secert_num:
#        print('Your guess was too low.')
#    elif guess > secert_num:
#        print('Your guess was too high.')
#    elif guess == secert_num:
#        print('Your guess was correct!')
#        break
#else:
#    print('You are out of guesses!')


#help = 'type start - to start car\ntype stop - to stop car\ntype quit - to exit'
#tarted = False

#while True:
#    command = input('>').lower()
#    if command == 'start':
#        if started:
#            print('Car is already started!')
#        else:
#            started = True
#            print('Car is strated.')
#    elif command == 'stop':
#        if not started:
#            print('Car is already stopped!')
#        else:
#            started = False
#            print('Car has stopped.')
#    elif command == 'quit':
#        break
#    elif command == 'help':
#        print(help)
#    else:
#        print('I dont understand.')

#prices = [10, 20, 30]
#total = 0

#for items in prices:
#    total += items
#print(f'Your total is ${total}.00')

#numbers = [5, 2, 5, 2, 2]

#for num in numbers:
#    output = ''
#    for x in range(num):
#        output += 'x'
#    print(output)

#list = [10000, 5, 80, 300, 66, 200]
#max = list[0]

#for largest in list:
#    if largest > max:
#        max = largest
#print(max)










