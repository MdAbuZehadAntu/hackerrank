def floyd_triangle(n):
    c = 1
    for i in range(1 , n + 1):
        for j in range(1 , i + 1):
            print(c , end=" ")
            c += 1
        print()


floyd_triangle(5)
