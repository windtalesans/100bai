chuoi = input("Nhập vào chuỗi: ")
tong_ky_tu_so = sum(int(ky_tu) for ky_tu in chuoi if ky_tu.isdigit())
print(f"Tổng của các ký tự số trong chuỗi là: {tong_ky_tu_so}")