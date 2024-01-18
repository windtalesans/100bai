n = int(input("Nhập vào số nguyên dương n: "))

so_luong_chu_so_chan = 0
so_luong_chu_so_le = 0

while n > 0:
    chu_so = n % 10
    if chu_so % 2 == 0:
        so_luong_chu_so_chan += 1
    else:
        so_luong_chu_so_le += 1
    n //= 10

print(f"{n} có {so_luong_chu_so_chan} chữ số chẵn và {so_luong_chu_so_le} chữ số lẻ.")
