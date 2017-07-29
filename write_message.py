filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write('I love programming!\n')
    file_object.write('I love abc.\n')

with open(filename,'a') as file_object:
    file_object.write('I love fad.\n')