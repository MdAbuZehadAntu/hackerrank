def fizzBuzz(n):
    for i in range(0,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
