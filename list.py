l=[]
n=int(input('enter how many list items : '))
if n<=0:
    print('Enter a valid number')
else:
    for i in range(1,n+1):
        print('enter no ', i , ': ')
        x=int(input())
        l.append(x)
    print(l)
    for i in l:
        if i>0:
            print(i)
    
    
