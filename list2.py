squares=[]
for values in range(1,11):
    square = values ** 2
    squares.append(square)
print(squares)

squares=[]
for values in range(1,31,3):
    squares.append(values)
print(squares)
print(squares[0:3])
print(squares[2:5])
print(squares[2:])
print(squares[-3:])


