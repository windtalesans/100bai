import re
s1 = input("xin mời nhập vào chuối:")
m1 = re.findall(r'\d', s1)  
m1 = [int(x) for x in m1]
print(sum(m1))

