# Object-Oriented Programming (OOP) in Python

## Why is Python called an OOP Language?
In Python, **everything is an object** – including data structures, data types, and functions.  
This makes Python a fully object-oriented language.

---

## Advantages of OOP
- You can create your own data types  
- Code reusability  
- Easier debugging  
- Easy collaboration in teams  

---

## End-to-End Project (Chatbook Class)

### Key OOP Concepts

- **Function vs Method**  
  - Function call → `print(function_name)`  
  - Method call → `object_name.method_name()`

- **Magic Methods / Dunder Methods**  
  Special methods with double underscores, for example:  
  - `__init__()` – Constructor  
  - `__str__()` – String representation  

- **`self`**  
  Represents the current object.  
  Example:  
  ```python
  object_name = ClassName()
  # Here, object_name represents 'self'

- **Creating Attributes Outside the Class**
  - Attributes can be dynamically added to objects after creation.     

- - **Encapsulation**
  - Making attributes private using double underscores:
  ```python
  - self.__name

- - **Getter & Setter Methods**
  - Used to access and modify hidden attributes:
  ```python
  def set_name(self, val):
    self.__name = val

  def get_name(self):
    return self.__name



- - **Static Methods**
  - Methods that do not require access to instance (self) or class variables.
    Defined using @staticmethod.
```python
__user_id = 1 #Static Variable (Before constructor)
def __init__(self):
        self.id = Chatbook.__user_id   #only class can acess static variable ie no self.__user_id
        Chatbook.__user_id += 1  #o/p --> 1,2,3  before static variable 1,1,1

@staticmethod     #as discussed earlier self cant access the ststaic variable
    def set_id(val):  #hence no self is passed i.e def set_id(self,val):  
        Chatbook.__user_id = val

    @staticmethod     #same rule used for setter
    def get_id():
        return Chatbook.__user_id

    







