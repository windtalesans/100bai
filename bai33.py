a = int(input("Nhập vào số nguyên dương a: "))

if a < 2:
    print(f"{a} không phải là số nguyên tố.")
else:
    la_so_nguyen_to = 1
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            la_so_nguyen_to = 0
            break

    if la_so_nguyen_to:
        print(f"{a} là số nguyên tố.")
    else:
        print(f"{a} không phải là số nguyên tố.")
