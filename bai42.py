A = int(input("Nhập vào số nguyên A: "))

e, a = 1, 1

while e + a <= A:
    l = e + a
    e, a = a, l

print(f"Số Fibonacci lớn nhất không vượt quá {A} là {a}.")
