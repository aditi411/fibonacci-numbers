n=int(input('enter the number of fibonacci numbers you want : '))
a=int(input('enter the first number : '))
b=int(input('enter the second number : '))
i=3
while i<=n:
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1
