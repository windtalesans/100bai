numbers = []

while True:
    num = int(input("Nhập một số nguyên: "))
    
    if num == -1:
        break
    
    numbers.append(num)

if not numbers:
    print("Dãy số rỗng.")
else:
    max_num = max(numbers)
    min_num = min(numbers)

    print(f"Số lớn nhất là: {max_num}")
    print(f"Số nhỏ nhất là: {min_num}")
