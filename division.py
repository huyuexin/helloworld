print("give me two numbers")
print("enter Q to quit")

while True:
    first_number=input("\n First number is ?")
    if  first_number == 'q':
        break
    second_number=input("\n second number is ?")
    if  second_number == 'q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by zero!")
    else:
        print(answer)