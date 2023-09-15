# a, b, c = map(float, input().split())
a=float(input())
b=float(input())
c=float(input())

# if a + b > c and b + c  > a and c + a > b and a > 0 and b > 0  and c > 0:
#     if a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a:
#       print('Right triangle !')
#     elif a == b and b == c:
#       print('Equilateral triangle !')
#     elif a == b or b == c or c == a :
#       print('Isosceles triangle !') 
#     elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:
#       print('Obtuse triangle !')
#     else:
#       print('Acute triangle !')
# else :
#   print('Not a Triangle !')
d = a + b > c and b + c  > a and c + a > b and a > 0 and b > 0  and c > 0
print('Triangle is ' + str(d))