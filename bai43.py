chuoi = input("Nhập vào chuỗi: ")

lol = ''.join(char if ('a' <= char.lower() <= 'z' or char == ' ') else ' ' for char in chuoi)

cac_tu = lol.split()
so_tu = len(cac_tu)

print(f"Số từ trong chuỗi là: {so_tu}")
