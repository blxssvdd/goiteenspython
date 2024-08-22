class Employee:
    def __init__(self, name: str, salary: float):
        self._name = name  
        self.__salary = salary  

    def display_info(self):
        print(f"Співробітник {self._name}")

    def _calculate_bonus(self):  
        return self.__salary * 0.1

    def __apply_raise(self):  
        self.__salary *= 1.05

    def show_salary(self):
        print(f"Зарплата: {self.__salary}")

    def give_raise(self):
        self.__apply_raise() 


class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department  

    def display_info(self):
        super().display_info()
        print(f"Відділ: {self.department}")

    def calculate_bonus(self):
        bonus = self._calculate_bonus()  
        return bonus * 2  

class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language  

    def display_info(self):
        super().display_info()
        print(f"Мова програмування: {self.programming_language}")

    def calculate_bonus(self):
        return self._calculate_bonus()  


employees = [
    Manager("Аліна", 80000, "Sales"),
    Developer("Михайло", 60000, "Python"),
    Developer("Ярослав", 65000, "JavaScript"),
]

for emp in employees:
    emp.display_info()
    print(f"Премія: {emp.calculate_bonus()}")
    emp.show_salary()
    emp.give_raise()
    emp.show_salary()
    print()
