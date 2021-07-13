a=3
n=0
i=1

if a%2!=0:
    while n!=a:
        if i%2!=0:
            print(i,end=' ')
            n+=1
            i+=1
        else:
            i+=1
else:
    while n!=(a-1):
        if i%2!=0:
            print(i,end=' ')
            n+=1
            i+=1
        else:
            i+=1
