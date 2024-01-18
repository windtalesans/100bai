n = int(input("Nhập vào số nguyên dương n: "))
k = 0
while 2 ** k <= n:
    if 2 ** k == n:
        print(f"{n} là số dạng 2^k với k = {k}.")
        break
    k += 1
else:
    print(f"{n} không phải là số dạng 2^k.")
