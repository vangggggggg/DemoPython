text = input("Nhập vào văn bản muốn mã hóa: ") #Nhận đoạn văn bản rõ
k = int(input("Nhập vào khóa dịch chuyển: ")) # Nhận khóa nhập vào từ bàn phím, ép kiểu về số nguyên
result = '' #Khởi tạo một chuỗi ký tự rỗng để cộng dồn kết quả mã hóa
print("Plain Text : " + text)
print("Shift pattern : " + str(k))

for i in range(len(text)):
    char = text[i]
    if "A"<=char<="Z": #Mã chữ HOA
        result = result + chr((ord(char) + k-65) % 26 + 65) # Nối ký tự bản mã vào kết quả
    elif 97<=ord(char)<=122: #Mã chữ thường
        result = result + chr((ord(char) + k - 97) % 26 + 97)
    else:
        result = result + char
print(result)