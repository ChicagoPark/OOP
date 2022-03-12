# Python_OOP
Object-Oriented Programming

## 1. Basic Class

[1] self: the scale of generated instance by BOSS class

[2] assert: Use it to suggest the condition for input parameters (Good to prevent the error at the beginning)

[3] _ _ repr _ _: Represent and assign unique name for the object
```python
def __repr__(self):
  return f"Item('{self.name}', {self.price}, {self.quantity})"
```
`result`
```bash
# When we generate 5 objects
[Item('Phone', 100, 5), Item('Computer', 1000, 5), Item('Cable', 10, 5), Item('Mouse', 50, 5), Item('Keyboard', 75, 5)]
```


```python
  def __init__(self, name: str, price=0, quantity=0):
      # Run validations to the received arguments
      assert price >= 0, f"Price {price} is not greater than zero"
      assert quantity >= 0, f"quantity {price} is not greater than zero"
```
print(CLASS._ _ dict _ _): Show all the attribute

## 2. CSV
Install the Plugin named "CSV"

classmethod: send the class as first argument
staticmethod: send the value as first argument

### When to use class methods and when to use static methods?
```python
class Item:
  @staticmethod
  def is_integer(num): # staticmethod function could be same with the function outside of the class. But it looks natural to include inside of the class.
    '''
    This should do something that has a relationship
    with the class, but not something that must be unique
    per instance!
    '''
  @classmethod
  def instantiate_from_something(cls):
    '''
    This should also do something that has a relationship
    with the class, but usually, those are used to manipulate
    different structures of data to instantiate objects, like
    we have done with CSV.
    '''
```
