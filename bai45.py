chuoi_so = input("Nhập vào 3 số nguyên: ")

danh_sach_so = [int(so) for so in chuoi_so.split(',')]

if len(danh_sach_so) == 3:
    tong = sum(danh_sach_so)
    print(f"Tổng của 3 số nguyên là: {tong}")
else:
    print("Vui lòng nhập đúng định dạng (3 số nguyên, cách nhau bởi dấu phẩy).")
