a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))

print(f"Ước chung của {a} và {b} là:", end=" ")
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(i, end=" ")
