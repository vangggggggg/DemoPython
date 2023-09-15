n = int(input())
_list=[]
for i in range(n):
    action = input().split()
    if action[0] == 'insert':
        _list.insert(int(action[1]),int(action[2]))
    elif action[0] == 'print':
        print(_list)
    elif action[0] == 'remove':
        _list.remove(int(action[1]))
    elif action[0] == 'append':
        _list.append(int(action[1]))
    elif action[0] == 'sort':
        _list.sort()
    elif action[0] == 'pop':
        _list.pop()
    elif action[0] == 'reverse':
        _list.reverse()
