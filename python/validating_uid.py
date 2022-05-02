for t in range(int(input())):
    st = input()
    if len(st) != 10:
        print('Invalid')
    else:
        for i in st:
            if st.count(i) > 1:
                print('Invalid')
                break
        if st.isalpha():
            print('Invalid')
        elif sum(c.isdigit() for c in st) < 3:
            print('Invalid')
        elif sum(1 for c in st if c.isupper())< 2:
            print('Invalid')
        else:
            print('Valid')


