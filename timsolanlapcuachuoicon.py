
a = input()
b = input()
# count = 0
# # for i in range(0,len(a)):
# #     if b in a:
# #         count += 1

# print(a.count(b))
def count_substring(string,sub_string):
    l=len(sub_string)
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string ):   
            count+=1
    return count  
print(count_substring(a,b))