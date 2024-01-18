chuoi = input("Nhập vào chuỗi: ")

tong_con_so = 0

so_tam = ''
for ky_tu in chuoi:
    if ky_tu.isdigit():
        so_tam += ky_tu
    elif so_tam:
        tong_con_so += int(so_tam)
        so_tam = ''

if so_tam:
    tong_con_so += int(so_tam)

print(f"Tổng của các con số trong chuỗi là: {tong_con_so}")