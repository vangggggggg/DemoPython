def giaiThua(n):
	giaithua = 1
	for i in range(1, n+1, 1):
		giaithua *= i
	return giaithua

x = int(input('x= '))
e_mu=0
for i in range(30):
   e_mu+=x**i/giaiThua(i)
res=e_mu/(1+e_mu)
print("Sigmoid_Logistic({0})= {1}".format(x,res))