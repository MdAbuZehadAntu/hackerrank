if __name__ == '__main__':
    arr = [2,3,6,6,5]
    max = float('-inf')
    min = max

    for i in set(arr):
        if i > max:
            min = max
            max = i
        elif min < i:
            min = i
    print(min)