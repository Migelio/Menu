def put_m(a):
 m = int(input('Количество строк, m : '))
 n = int(input('Количество столбцов, n : '))
 for i in range(0,m):
   b = []
   print("{0} Строка".format(i+1))
   for j in range(0,n):

     b.append(int(input("{0} Столбец: " .format(j+1))))
   a.append(b)
 print("\n{0}\n".format(a))
 return a
