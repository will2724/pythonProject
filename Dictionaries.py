numbers = {'1':'One', '2':'Two', '3':'Three', '4':'Four'}
output = ''

digits = input('Phone: ')
for value in digits:
    output += numbers.get(value, '!') + ' '
print(output)
