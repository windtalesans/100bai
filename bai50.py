mat_khau = input("Nhập vào một chuỗi mật khẩu: ")

co_dau_cach_biet = False
co_in_hoa = False
co_so = False
co_in_thuong = False
do_dai_hop_le = False

for ky_tu in mat_khau:
    if ky_tu.isalpha():
        if ky_tu.isupper():
            co_in_hoa = True
        elif ky_tu.islower():
            co_in_thuong = True
    elif ky_tu.isdigit():
        co_so = True
    elif ky_tu in "!@#$%^&*()_-+=<>?":
        co_dau_cach_biet = True

if 6 <= len(mat_khau) <= 20:
    do_dai_hop_le = True

if co_dau_cach_biet and co_in_hoa and co_so and co_in_thuong and do_dai_hop_le:
    print("Chuỗi mật khẩu mạnh.")
else:
    print("Chuỗi mật khẩu không đạt yêu cầu mạnh.")
