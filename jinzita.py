def fibonacci(n):
    terms=[0,1]
    i=2
    while i <= n:
        terms.append(terms[i-1]+terms[i-2])
        i=i+1
    return terms[n]

for i in range(0,10):
    print(fibonacci(i))
