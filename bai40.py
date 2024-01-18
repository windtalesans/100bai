n = int(input("Nhập vào số nguyên dương n: "))

tong_chu_so = 0

while n > 0:
    chu_so = n % 10
    tong_chu_so += chu_so
    n //= 10

print(f"Tổng các chữ số của {n} là {tong_chu_so}.")

