a=int(input("xin mời nhập vào số a:"))
b=int(input("xin mời nhập vào số b:"))
if a>b:
    for i in range(1,a+1):
        if i%a==0 and i%b==0:
            print(i)
else:
    for i in range(1,b):
        if i%a==0 and i%b==0:
            print(i)