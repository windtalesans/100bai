def tim_so_nho_nhat_trong_doan(L, a, b):
    if a >= b or b >= len(L) or a < 0:
        print("Yêu cầu không hợp lệ.")
        return

    so_nho_nhat = min(L[a:b+1])
    print(f"Số nhỏ nhất trong đoạn từ vị trí {a} đến vị trí {b}: {so_nho_nhat}")

L = [int(x) for x in input("Nhập vào list số nguyên: ").split()]

a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b (a < b): "))

tim_so_nho_nhat_trong_doan(L, a, b)