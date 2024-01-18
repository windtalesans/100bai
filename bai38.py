n = int(input("Nhập vào số nguyên dương n: "))

so_luong_chu_so = 0
while n > 0:
    n //= 10
    so_luong_chu_so += 1

print(f"{n} có {so_luong_chu_so} chữ số.")
