danh_sach_so = [int(x) for x in input("Nhập vào list số nguyên, cách nhau bởi dấu phẩy: ").split(',')]

if danh_sach_so:
    gia_tri_lon_nhat = max(danh_sach_so)
    print(f"Giá trị lớn nhất trong danh sách là: {gia_tri_lon_nhat}")
else:
    print("Danh sách không có phần tử.")
