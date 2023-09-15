a = float(input())
b = float(input())
c = float(input())
d = b*b - 4*a*c
if d > 0:
    print('The equation has two real solution!')
elif d == 0:
    print('The equation has one real solution!')
else :
    print('The equation has no solution!')