a = float(input("Nhập vào hệ số a: "))
b = float(input("Nhập vào hệ số b: "))

if a != 0:
    x = -b / a
    print("Nghiệm của phương trình là x =", x)
else:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
