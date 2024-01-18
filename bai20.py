# Nhập vào tháng và năm từ người dùng
thang = int(input("Nhập vào tháng (1-12): "))
nam = int(input("Nhập vào năm: "))

if thang < 1 or thang > 12:
    print("Tháng không hợp lệ.")
else:
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        so_ngay = 31
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        so_ngay = 30
    else:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            so_ngay = 29
        else:
            so_ngay = 28

    print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")
