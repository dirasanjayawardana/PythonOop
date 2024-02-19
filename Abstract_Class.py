# abstract class --> class yang tidak bisa dibuat object secara langsung, hanya bisa di turunkan ke childnya, hanya seperti membuat kerangka
# membuat abstract class dengan menggunakan kata kunci --> ABC (Abstract Base Class)
from abc import ABC, abstractmethod

class Person(ABC):
    def setProfile(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
    
    @abstractmethod
    def getProfile(self):
        pass # pass hanya sebagai penutup dari blok funtion
    
# cara inheritance class
class Student(Person):
    def __init__(self):
        super().__init__()
    
    def getProfile(self):
        return{
            "firs-name" : self.firstName,
            "last-name" : self.lastName,
            "email" : self.email
        }

# membuat object dari child class
student1 = Student()
student1.setProfile("dira", "sanjaya", "dira@gmail.com")
print(student1.getProfile())

# menggunakan largs (list arguments) dengan * --> argument atau parameter properti yang dimasukkan boleh berupa list apa saja
class Animal:
    animal = []
    
    def setAnimal(self, *largs):
        self.animal.extend(largs)
    
    def getAnimal(self):
        for item in self.animal:
            print(item)

animal1 = Animal()
animal1.setAnimal("kucing", "anjing", "ayam", "bebek")
animal1.getAnimal()

# menggunakan kwargs (keyword arguments) dengan ** --> argument atau parameter properti yang dimasukkan boleh berupa dictionary apa saja
class Employee:
    employee = []
    
    def setEmployee(self, **kwargs):
        self.employee.append(kwargs)
    
    def getEmployee(self):
        for item in self.employee:
            print(item)

employee1 = Employee()
employee1.setEmployee(name="dira", email="dira@mail.com", employee="jakarta")
employee1.getEmployee()
