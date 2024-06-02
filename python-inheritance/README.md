# Python inheritance
In this project we are expected to learn about inheritance.


### What is a superclass, baseclass or parentclass
A superclass, baseclass or parentclass are the classes that encapsulates the common attributes and methods that will be inherited by their childs. Basically, is the class being inherited from. Any class can be a parent class.
#### For example, a class named `Person`, with `first name` and `last name` properties and a `printname` method.
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    x = Person("John", "Doe")
    x.printname()
```

The output will be:
```
John Doe
```

### What is a subclass
A subclass is the 'child class', the class that inherits from another class their attributes and methods. Sends the parent class as a parameter when creating the child class.

#### For example, a class `Student` that inherits the properties and methods of `Person`.
```
    class Student(Person)
    pass
```

Now, the class `Student` has the same properties and methods that the class `Person` has

### How to list all attributes and methods of a class or instance
To list the attributes (methods, properties and others) of a class or instance we need to use the built-in function `dir()`