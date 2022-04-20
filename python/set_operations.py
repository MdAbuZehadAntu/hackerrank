# The first line contains the number of elements in set .
# The second line contains the space separated list of elements in set .
# The third line contains integer , the number of other sets.
# The next  lines are divided into  parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.
#
#  len(set(A))
#  len(otherSets)
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    for _ in range(m*2):
        inp = list(map(str, input().split()))
        op = inp[0]
        l = int(inp[1])
        print(op, l)

        otherSet = set(map(int, input().split()))

        if op == 'intersection_update':
            A.intersection_update(otherSet)
        elif op == 'update':
            A.update(otherSet)
        elif op == 'symmetric_difference_update':
            A.symmetric_difference_update(otherSet)
        elif op == 'difference_update':
            A.difference_update(otherSet)
    print(sum(A))


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# intersection_update 10