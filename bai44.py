chuoi = input("Nhập vào chuỗi: ")

cac_tu = chuoi.split()

if cac_tu:
    tu_dau_tien = cac_tu[0]
    print(f"Từ đầu tiên trong chuỗi là: {tu_dau_tien}")
else:
    print("Chuỗi không có từ.")
