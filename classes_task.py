
import datetime

class Employee:
    
    def __init__ (self, name, age, salary, employment_date):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_date = employment_date
        
    def get_working_years(self):
         now = datetime.datetime.now()
         return now.year - int(self.employment_date)
     
class Manager(Employee):
    
    def __init__ (self, name, age, salary, employment_date, bonus_percentage):
        super().__init__(name, age, salary, employment_date)
        self.bonus_percentage = bonus_percentage
        
    
    def get_bonus(self):
         return float(self.bonus_percentage) * float(self.salary)
     
employees = []
managers = []

options = ["show employees", "show managers", "add an employee", "add a manager", "exit"]

print("    Welcome to HR Pro 2019:")

while(True):
    print("    Choose an action to do:")
    counter = 1
    for option in options:
        print(counter , ".", option)
        counter += 1
    print()
    option = input("what would you like to do? ")
    
    if not option.isdigit():
        print("Invalid option!\n")
        continue
    
    option = int(option)
    if option < 1 or option > 5:
        print("Invalid option!\n")
        continue
    
    if option == 5:
        break
    print("-----------------")
    
    if option == 1:
        if len(employees) == 0:
            print("No employess yet!")
        else:
            print("Employees")
            for employee in employees:
                print("name:", employee.name, ", age:", employee.age, ", salary:", employee.salary, ", working years: ", employee.get_working_years())
            print("-----------------\n")
            continue
        
    if option == 2:
        if len(managers) == 0:
            print("No managers yet!")
        else:
            print("Managers")
            for manager in managers:
                print("name:", manager.name, ", age:", manager.age, ", salary:", manager.salary, ", working years:", manager.get_working_years(), ", bonus:", manager.get_bonus())
            print("-----------------\n")
            continue
        
    if option == 3:
        name = input("name: ")
        age = input("age: ")
        salary = input("salary: ")
        employement_year = input("employement year: ")
        
        employees.append(Employee(name, age, salary, employement_year))
        print("Employee added succesfully!\n")
        
    if option == 4:
        name = input("name: ")
        age = input("age: ")
        salary = input("salary: ")
        employement_year = input("employement year: ")
        bonus_percentage = input("bonus percentage: ")
        
        managers.append(Manager(name, age, salary, employement_year, bonus_percentage))
        print("Manager added succesfully!\n")
        
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    