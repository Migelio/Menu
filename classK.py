def try_c():
 class Person:
     per_count = 0
    
     def __init__(self, name, salary, area):
         self.name = name
         self.salary = salary
         self.area = area
         Person.per_count += 1

     def print_count(self):
         print('Всего сотрудников: %d' % Person.per_count)
        
     def print_employee(self):
         print('Имя: {}. Зарплата: {}. Район: {}'.format(self.name, self.salary, self.area))
 class Docter:
     doc_count = 0
     
     def __init__(self, name, salary, area):
         self.name = name
         self.salary = salary
         self.area = area
         Docter.doc_count += 1

     def print_count(self):
         print('Всего сотрудников: %d' % Docter.doc_count)

     def print_employee(self):
         print('Имя: {}. Зарплата: {}. Район: {}'.format(self.name, self.salary, self.area))
 class Programmer:
     pro_count = 0

     def __init__(self, name, salary, area):
         self.name = name
         self.salary = salary
         self.area = area
         Programmer.pro_count += 1

     def print_count(self):
         print('Всего сотрудников: %d' % Programmer.pro_count)

     def print_employee(self):
         print('Имя: {}. Зарплата: {}. Район: {}'.format(self.name, self.salary, self.area))

 per1 = Person("Андрей", 45500, "Сокол")
 per2 = Person("Мария", 70440, "Перово")
 per1.print_employee()
 per2.print_employee()
 doc1 = Docter("Петр", 200000, "Прудная")
 doc2 = Docter("Анна", 30000, "Лужники")
 doc1.print_employee()
 doc2.print_employee()
 pro1 = Programmer("Николай", 38000, "Котельники")
 pro2 = Programmer("София", 67400, "Новогиреево")
 pro1.print_employee()
 pro2.print_employee()
 print("Всего учителей: %d" % Person.per_count)
 print("Всего врачей: %d" % Docter.doc_count)
 print("Всего программистов: %d\n" % Programmer.pro_count)
