#Project 1: If statment
# price = 1000000
# credit = 720
# if credit >= 700:
#   print('Your down payment amount is $' + str(price * 0.1))
#else:
#   print('Your down payment amount is $' + str(price * 0.2))

#Project 2: Condition Statments
#name = 'JQ'

#if len(name) < 3:
    #print('Name is too short, please extend the length your name.')
#elif len(name) > 15:
    #print('Name is too long, please shorten your name')
#else:
    #print('Great Name!')

#Project 3: Convert Weight
#weight = int(input('Weight: '))
#unit = input('(L)bs or (K)g: ')

#if unit.upper() == 'L':
    #kg = (weight) * 0.45
    #print(f'You are {kg} kg.')
#else:
    #lbs = (weight) / 0.45
    #print(f'You are {lbs} lbs')

#Project 4: Guessing Game
#secret_number = 45
#guess_count = 0
#guess_limit = 3

#while guess_count < guess_limit:
    #guess = int(input('Guess the #: '))
    #guess_count += 1
    #if guess < secret_number:
        #print('Wrong Number! Guess is too low.')
    #elif guess > secret_number:
        #print('Wrong Number! Guess is too high.')
    #elif guess == secret_number:
        #print(('Ding ' * 3) + 'Right Answer!')
        #break
#else:
    #print('Number of tries have been depleted.')

#Project 5: Car game
command = ''
started = False
while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print('Car has already been started!')
        else:
            started = True
            print('Car is started.')
    elif command == 'stop':
        if not started:
                print('Car has already been stopped!')
        else:
            started = False
            print('Car has stopped.')
    elif command == 'help':
        print('''
Start - To Start Car 
Stop - To Stop Car 
Quit - To Exit Game
''')
    elif command == 'quit':
        break
    else:
        print("I don't understand that command")
