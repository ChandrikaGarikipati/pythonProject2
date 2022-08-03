def fibbbonocci(num):
    n1=0
    n2=1
    n3=0
    for i in range(num):
        print(n3);
        n1=n2;
        n2=n3;
        n3=n1+n2;
num=int(input('enter fibanocci'))
fibbbonocci(num)
