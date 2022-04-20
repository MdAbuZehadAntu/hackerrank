if __name__=="__main__":
    n = int(input())
    es = set(map(int,input().split()))
    n = int(input())
    fs = set(map(int,input().split()))
    print(len(es.symmetric_difference(fs)))