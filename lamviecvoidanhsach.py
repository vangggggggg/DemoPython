# import random

# def action(mlist ,i):
#     if i == 1:
#         mlist.insert(random.randint(0,9),random.randint(0,9))
#     elif i ==2:
#         random_index = random.randint(0,len(mlist)-1)
#         mlist.remove(mlist[random_index])
#     elif i == 3:
#         mlist.append(random.randint(0,9))
#     elif i == 4:
#         mlist.sort()
#     elif i == 5:
#         mlist.pop()
#     elif i == 6 :
#         mlist.reverse()
#     elif i == 7:
#         print(mlist)

# n = int(input('N: '))
# mlist = [0]

# for j in range(n-1):
#     i = random.randint(0,6)
#     action(mlist ,i)
# action(mlist,7)






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
        arr.sort()
    elif action[0] == 'pop':
        # Lấy ra phần tử cuối cùng từ danh sách.
        arr.pop()
    elif action[0] == 'reverse':
        #đảo ngược mảng 
        arr.reverse()
    else :
        pass
for i in  range(len(b)):
    print(b[i])
    