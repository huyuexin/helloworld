def make_piz(size,*toppings):
    print("\n making a "+str(size)+"piz with flowing:")
    for topping in toppings:
        print(" -"+topping)
make_piz(16,'naiyou')
make_piz(12,'X','z','A')