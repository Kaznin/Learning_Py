class People:
    '''Базовый класс людей'''

    def __init__(self, age = 0, name = 'Adam'):
        self.age = age
        self.name = name
        self.gender = 'male'

class Employee(People):
    '''Базовый класс '''
    emp_count = 0 #атрибут класса

    def __init__(self, name, salary = 0):
        super().__init__(name=name)
        self.salary = salary #атрибут экземпляра класса
        Employee.emp_count += 1

Ivan = People(18)
print(Ivan.gender, Ivan.age, Ivan.name)
Maria = Employee('Мария', 1500)
Maria.gender = 'female'
print(Maria.gender, Maria.age, Maria.name)
Ivan.name = 'Адам'
print(Ivan.gender, Ivan.age, Ivan.name)