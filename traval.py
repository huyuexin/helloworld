#travel
position = True
#标记结束  大写的
travel={}
while position:
    name=input("\n what's your name?")
    visiter=input("\n where's favorite want to travel?")
    travel[name] = visiter
    positioner=input("anyone go on? yes or no?")
    if positioner=='no':
        position=False
print("\n---Poll Results")
for name,visiter in travel.items():
    print(name+" want to travel to "+visiter+".")

