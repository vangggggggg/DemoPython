n = int(input())
arr = []
b = []


for i in range(n):
    #Nhập trên 1 hàng cách nhau 1 space được hiểu là 1 list 
    action = input().split()
    if action[0] == 'insert':
        #thêm vào vị trí ví dụ insert 3 1 là thêm vào số 3 vào vị trí 1
        arr.insert(int(action[1]),int(action[2]))
    elif action[0] == 'print':
        c = arr.copy()
        b.append(c)
    elif action[0] == 'remove':
        # Xóa lần xuất hiện đầu tiên của số nguyên 
        arr.remove(int(action[1]))
    elif action[0] == 'append':
        #Chèn số nguyên e vào cuối danh sách.
        arr.append(int(action[1]))
    elif action[0] == 'sort':
        #sắp xếp list 
        arr.sort
    elif action[0] == 'pop':
        # Lấy ra phần tử cuối cùng từ danh sách.
        arr.pop()
    elif action[0] == 'reverse':
        #đảo ngược mảng 
        arr.reverse
    else :
        pass
for i in  range(len(b)):
    print(b[i])