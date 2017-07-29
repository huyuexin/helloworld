
from name_function import get_formatted_name
print('Enter Q to end!')
while True:
    first = input('your first name is?')
    if first == 'q':
        break
    last = input('your last name is?')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("your name is " + formatted_name)

