a=int(input("xin mời nhập vào số a:"))
s=0
for i in range(1,a+1):
    if a%i==0:
        s=s+1
print(s)