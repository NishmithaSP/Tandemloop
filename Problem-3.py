rows=3
for i in range(1,rows+1):
    if i%2!=0:
        for j in range(i,-1,-1):
            print(j+1,end=' ')
    else:
        for j in range(i+1):
            print(j+1,end=' ')
    print()
for i in range(rows-1,-1,-1):
    if i%2!=0:
        for j in range(i,-1,-1):
            print(j+1,end=' ')
    else:
        for j in range(i+1):
            print(j+1,end=' ')
    print()
