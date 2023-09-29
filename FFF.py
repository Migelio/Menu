def ryad():
 import math

 def fun(n):
	 return (n**n)/((3**n)*math.factorial(n))

 n = 1
 pred = 0
 eps = 0.001
 suma = 0
 sled = fun(n)
 suma += sled
 n+=1
 while True:
	 pred = sled
	 sled = fun(n)
	 n+=1
	 suma+=sled
	 if abs(pred-sled)>eps:
		 break

 print("Cумма Ряда  = {0}\n".format(suma))

