n = int(input("Nhập vào một số tự nhiên: "))
for i in range(2, n):
    if n % i == 0:
        print("Số {0} không phải số nguyên tố".format(n))
        break
else:
    print("Số {0} là số nguyên tố".format(n))