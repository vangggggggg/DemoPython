from binascii import b2a_base64


def fib(n):
    a, b = 1, 1
    for i in range(n):
        a, b= b, a + b
    print(a)

fib(4)