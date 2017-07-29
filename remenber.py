import json

def get_stored_usename():
    filename = 'use_name.json'
    try:
        with open(filename) as f_obj:
            usename = json.load(f_obj)

    except FileNotFoundError:
        return None
    else:
        return usename

def get_new_usename():
    filename = 'use_name.json'
    usename = input("What's your name?")
    with open(filename, 'w') as f_obj:
        json.dump(usename, f_obj)
    return usename


def greet_user():
    usename=get_stored_usename()
    if usename:
        print("Welecome back "+usename+'!')
    else:
        usename=get_new_usename()
        print("We will remenber your name")
greet_user()