# Python: Classes and objects
In this project we are expected to learn about Object-Oriented Programming

## First things first: What do we need to know to do this?
### What is OOP
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects and data, rather than actions and logic. In OOP, objects are instances of classes, and classes define the properties (attributes) and behaviors (methods) of objects. OOP promotes modularity, reusability, and extensibility in software development.
### “first-class everything”
"First-class everything" is a principle in programming languages that treats all entities (such as functions, variables, and data structures) as first-class citizens, meaning they can be passed as arguments, returned from functions, and assigned to variables.
### What is a class
A class in Python is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that all objects of that class will have.
### What is an object and an instance
An object is a concrete instance of a class. It is created using the class constructor and has its own unique set of attribute values.
### What is the difference between a class and an object or instance
The difference between a class and an object or instance is that a class is a blueprint or template for creating objects, while an object is a concrete instance of a class.
### What is an attribute
An attribute is a piece of data associated with a particular object. Attributes represent the state of an object and can be accessed using dot notation.
### What are and how to use public, protected and private attributes
Attributes can be public, protected, or private:
- Public attributes: Accessible from outside the class.
- Protected attributes: Accessible within the class and its subclasses.
- Private attributes: Accessible only within the class.
For example:
```
class School:
    def __init__(self):
        self.students = []     # Public attribute
        self._teachers = []    # Protected attribute
        self.__courses = []    # Private attribute

""" Creating an object of the School class """
school = School()

""" Accessing public attribute """
print("Students:", school.students)    # Output: []

""" Accessing protected attribute (only accessible within the class) """
print("Teachers:", school._teachers)   # Output: []

# Attempting to access private attribute directly
# This will raise an AttributeError
# print(school.__courses)
```
### What is self
The self keyword in Python is a reference to the current instance of the class. It is used to access instance variables and methods within the class.
### What is a method
A method is a function defined inside a class that operates on the attributes of an object.
### What is the special `__init__` method and how to use it
The special `__init__` method (constructor) is called automatically when an object of the class is created. It is used to initialize the attributes of the object.
### What is Data Abstraction, Data Encapsulation, and Information Hiding
- *Data Abstraction*: The process of hiding the implementation details and showing only the essential features of an object.
- *Data Encapsulation*: The bundling of data (attributes) and methods that operate on that data into a single unit (class).
- *Information Hiding*: The practice of restricting access to certain parts of an object, hiding the details of its implementation.
### What is a property
A property is a special kind of attribute that automatically calls getter and setter methods when accessed or assigned to. It allows for controlled access to object attributes.
### What is the difference between an attribute and a property in Python
The difference between an attribute and a property in Python is that an attribute is a piece of data associated with an object, while a property is a special kind of attribute that allows for controlled access to object attributes using getter and setter methods.
### What is the Pythonic way to write getters and setters in Python
The Pythonic way to write getters and setters in Python is to use property decorators. (@property)
### How to dynamically create arbitrary new attributes for existing instances of a class
To dynamically create arbitrary new attributes for existing instances of a class, we can simply assign values to new attribute names using dot notation.
### How to bind attributes to object and classes
Attributes can be bound to objects or classes using dot notation or by using the `setattr()` function.
### What is the `__dict__` of a class and/or instance of a class and what does it contain
The `__dict__` attribute of a class or instance of a class is a dictionary that contains the attributes of the class or instance, along with their values.
### How does Python find the attributes of an object or class
Python finds the attributes of an object or class by searching the object's dictionary (__dict__) first, then its class hierarchy.
### How to use the `getattr` function
The `getattr()` function is used to get the value of an attribute of an object or class. It takes the object or class and the attribute name as arguments. If the attribute does not exist, it returns a default value or raises an AttributeError.
