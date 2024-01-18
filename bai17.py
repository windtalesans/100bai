a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))

so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)
so_trung_gian = (a + b + c) - so_lon_nhat - so_nho_nhat

print("Các số theo thứ tự tăng dần là:", so_nho_nhat, so_trung_gian, so_lon_nhat)
