                                #Python OOPs Questions

# 1.  What is Object-Oriented Programming (OOP)?
# Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods to manipulate that data. It emphasizes concepts such as encapsulation, inheritance, polymorphism, and abstraction to create modular and reusable code.

# 2.What is a class in OOP?
# A class in OOP is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.

# 3.What is an object in OOP?
# An object is a concrete instance of a class. It is created based on the class definition and contains specific values for the attributes defined in the class.

# 4.What is the difference between abstraction and encapsulation?
# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object. Encapsulation, on the other hand, is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit (class) and restricting access to some of the object's components.

#5.What are dunder methods in Python?
# Dunder methods, or "double underscore" methods, are special methods in Python that have double underscores at the beginning and end of their names (e.g., __init__, __str__). They are used to define the behavior of objects for built-in operations, such as initialization, string representation, and arithmetic operations.

# 6.Explain the concept of inheritance in OOP?
# Inheritance is a fundamental concept in OOP that allows a class (called the child or subclass) to inheritproreties and behavious of class.

# 7.What is polymorphism in OOP?
# Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same name.

# 8.How is encapsulation achieved in Python?
# Encapsulation can be achieved by making variables private, public, and protected by using underscores before the variable name.

# 9.What is a constructor in Python?
# A constructor is a special method in Python that is automatically called when an object of a class is created.

# 10.What are class and static methods in Python?
# Class methods are methods that are bound to the class and not the instance of the class. They can access and modify class state that applies across all instances of the class. Static methods, on the other hand, do not have access to the instance or class state. They are utility functions that belong to the class's namespace but do not operate on class or instance data.

# 11.What is method overloading in Python?
# Method overloading is a feature that allows a class to have multiple methods with the same name but different parameters. Python does not support method overloading by default, but it can be achieved using default arguments or variable-length arguments.

# 12.What is method overriding in OOP?
# Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already defined in its superclass.

# 13.What is a property decorator in Python?
# The property decorator in Python is used to define a method as a property, allowing you to access it like an attribute while still using getter and setter methods.

# 14.Why is polymorphism important in OOP?
# Polymorphism is important in OOP because it allows for flexibility and the ability to extend code without modifying existing structures. It enables a single interface to represent different underlying forms (data types).

# 15.What is an abstract class in Python?
# An abstract class in Python is a class that cannot be instantiated and is typically used as a base class. It can contain abstract methods that must be implemented by any subclass.

# 16.What are the advantages of OOP?
# Advantages of OOP include code reusability, modularity, easier maintenance.

# 17.What is multiple inheritance in Python?
# Multiple inheritance is a feature in Python where a class can inherit attributes and methods from more than one parent class. This allows for a more complex and flexible class hierarchy.

# 18.What is the difference between a class variable and an instance variable?
# A class variable is shared among all instances of a class, while an instance variable is unique to each instance of the class.

# 19.Explain the purpose of ‘’__str__’ and ‘__repr__’ ‘ methods in Python?
# The __str__ method is used to define a human-readable string representation of an object, while the __repr__ method is used to define an unambiguous string representation of an object that can be used to recreate the object.

# 20.What is the significance of the ‘super()’ function in Python?
# The super() function in Python is used to call a method from a parent class. It is particularly useful in the context of inheritance, allowing you to access inherited methods that have been overridden in a subclass.

# 21.What is the significance of the __del__ method in Python?
# The __del__ method in Python is a destructor method that is called when an object is about to be destroyed. It is used to perform cleanup activities, such as closing files or releasing resources.

# 22.What is the difference between @staticmethod and @classmethod in Python?
# @staticmethod is used to define a method that does not operate on an instance or class, while @classmethod is used to define a method that operates on the class itself and can access class variables.

# 23.How does polymorphism work in Python with inheritance?
# Polymorphism in Python allows methods to be defined in a base class and overridden in derived classes. This enables a single interface to represent different underlying forms (data types).

# 24.What is method chaining in Python OOP?
# Method chaining is a technique where multiple method calls are made on the same object in a single statement. This is achieved by having each method return the object itself (usually via self).

# 25.What is the purpose of the __call__ method in Python?
# The __call__ method in Python allows an instance of a class to be called as a function. This can be useful for creating objects that behave like functions or for implementing callable objects.



                                                # PRACTICAL QUESTIONS
#1 Create a parent class Animal with a method speak() that prints a generic message. Create a child class Dog that overrides the speak() method to print "Bark!".
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Bark!")
obj = Dog()
obj.speak()

# 2. Write a program to create an abstract class Shape with a method area(). Derive classes Circle and Rectangle from it and implement the area() method in both.
import abc
class shape:
    @abc.abstractmethod
    def area(self):
        pass
class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
obj = Circle(5)
print(obj.area())

# 3.Implement a multi-level inheritance scenario where a class Vehicle has an attribute type. Derive a class Car and further derive a class ElectricCar that adds a battery attribute.
class Vehicle:
    def __init__(self , type):
        self.type = type
class Car(Vehicle):
    def __init__(self,type,model):
        self.type = type
        self.model = model
class ElectricCar(Car):
    def __init__(self,type,model,battery):
        self.type = type
        self.model = model
        self.battery = battery
obj = ElectricCar("Vehicle","Car","5000mAh")
print(obj.type)
print(obj.model)
print(obj.battery)

# 4. Demonstrate polymorphism by creating a base class Bird with a method fly(). Create two derived classes Sparrow and Penguin that override the fly() method.
class Bird:
    def fly(self):
        print("Base class bird is flying")
class Sparrow(Bird):
    def fly(self):
        print("sparrow is flying")
class Penguin(Bird):
    def fly(self):
        print("penguin is flying")
obj = Penguin()
print(obj.fly())

#5. Write a program to demonstrate encapsulation by creating a class BankAccount with private attributes balance and methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Low balance. Withdrawal failed.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.__balance -= amount
            print(f"Withdraw: {amount}")
    def check_balance(self):
        print(f"Current Balance: {self.__balance}")

obj = BankAccount(1000)
print(obj.deposit(5000))
print(obj.check_balance())

# 6. Demonstrate runtime polymorphism using a method play() in a base class Instrument. Derive classes Guitar and Piano that implement their own version of play().

class Instrument:
    def play(self):
        print("play the instrument which you like")
class Guitar(Instrument):
    def play(self):
        print("let play the guitar")
class Piano(Instrument):
    def play(self):
        print("let's play piano")
def perform_play(instrument):
    instrument.play()
guitar = Guitar()
print(perform_play(guitar))


# 7. Create a class MathOperations with a class method add_numbers() to add two numbers and a static method subtract_numbers() to subtract two numbers.

class MathOperations:
    @classmethod
    def add_numbers(cls, a, b):
        return a + b
    @staticmethod
    def subtract_numbers(a, b):
        return a - b

# 8. Implement a class Person with a class method to count the total number of persons created.

class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod
    def get_person_count(cls):
        return cls.count

# 9. Write a class Fraction with attributes numerator and denominator. Override the str method to display the fraction as "numerator/denominator".

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
obj = Fraction(3,4)
print(obj)

#  10. Demonstrate operator overloading by creating a class Vector and overriding the add method to add two vectors.

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x + other.x , self.y + other.y)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
v1 = Vector(2,3)
v2 = Vector(4,5)
v3 = v1 + v2
print(v3)


# 11. Create a class Person with attributes name and age. Add a method greet() that prints "Hello, my name is {name} and I am {age} years old."
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
obj = Person("Harshit", 23)
obj.greet()


# 12. Implement a class Student with attributes name and grades. Create a method average_grade() to compute the average of the grades.
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
obj = Student("Harshit", [85, 90, 78, 92])
print(obj.average_grade())


# 13. Create a class Rectangle with methods set_dimensions() to set the dimensions and area() to calculate the area.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def set_dimension(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
obj = Rectangle(5, 10)
print(obj.area())
obj.set_dimension(7, 12)
print(obj.area())

#  14. Create a class Employee with a method calculate_salary() that computes the salary based on hours worked and hourly rate. Create a derived class Manager that adds a bonus to the salary.
class Employee:
    def __init__(self, salary, work_hours, horly_rate):
        self.salary = salary
        self.work_hours = work_hours
        self.horly_rate = horly_rate
    def calculate_salary(self):
        return (self.work_hours * self.horly_rate)
class Manager(Employee):
        def add_bonus(self, bonus):
            return self.calculate_salary() + bonus

obj = Manager(0, 160, 50)
print(obj.add_bonus(5000))

# 15. Create a class Product with attributes name, price, and quantity. Implement a method total_price() that calculates the total price of the product.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price*self.quantity
obj = Product("Laptop", 50000, 2)
print(obj.total_price())


# 16. 16. Create a class Animal with an abstract method sound(). Create two derived classes Cow and Sheep that implement the sound() method.

import abc
class Animal:
    @abc.abstractmethod
    def sound(self):
        pass
class Cow(Animal):
    def sound(self):
        print(" cow is shouting")
class Sheep(Animal):
    def sound(self):
        print("sheep is shouting")
obj = Sheep()
print(obj.sound())



# 17. Create a class Book with attributes title, author, and year_published. Add a method get_book_info() that returns a formatted string with the book's details.

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    def get_book_info(self):
        return f"{self.title} by {self.author}, published in {self.year_published}"
obj = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(obj.get_book_info())

#  18. Create a class House with attributes address and price. Create a derived class Mansion that adds an attribute number_of_rooms.

class House:
    def __init__ (self, address, price):
        self.address = address
        self.price = price
class Mansion(House):
    def __init__(self,address, price, number_of_rooms):
        super().__init__(address, price)
        self.number_of_rooms = number_of_rooms
obj = Mansion("123 Mansion St", 1000000, 5)
print(obj.address)
print(obj.price)
print(obj.number_of_rooms)