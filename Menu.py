import mat_create as u
import determ as i
import FFF as r
import classK as s

while True:
    print("1. Создать матрицу m x n\n2.Вычислить Определитель матрицы\n3.Вычислить значение ряда\n4.Задание на класс")
    print("Введите Q, чтобы завершить\n")
    k= input()
    if k == "Q":
        break
    elif k== "1":
        p=[]
        u.put_m(p)
    elif k=="2":
        print("\nвведине квадратную матрицу")
        mat =[]
        u.put_m(mat)
        print('Опредилитель равен {0}\n'.format(i.opred(mat, 1)))
    elif k=="3":
        r.ryad()
    
    elif k=="4":
        s.try_c()

    else:
        print("\nНеверное значение\n")

