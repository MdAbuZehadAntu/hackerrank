def multiplication_table(n):
    for i in range(1 , 11):
        print(f'{n} X {i} = {n * i}')
    print()


N = [2 , 5 , 7 , 8 , 9 , 10]
for item in N:
    multiplication_table(item)
