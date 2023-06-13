def prostota(n):
    i = 1
    while n%(n-i) != 0:
        i += 1
    if n-i != 1:
        print('no')
    else:
        print('yes')
    print(n-i)

prostota(127)