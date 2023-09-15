s=input()
n=int(input())
l = len(s)
if s[:n] == s[:-n-1:-1]:
  print("Chuỗi vừa nhập là chuỗi giả Palindrome với", n)
else:
  print("Chuỗi vừa nhập KHÔNG phải là một chuỗi giả Palindrome với", n)
