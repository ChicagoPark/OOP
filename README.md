# Python_OOP
Object-Oriented Programming

[Definition]

[1] self: the scale of generated instance by BOSS class

[2] assert: Use it to suggest the condition for input parameters (Good to prevent the error at the beginning)

[3] __repr__: Represent and assign unique name for the object
```python
def __repr__(self):
  return f"Item('{self.name}', {self.price}, {self.quantity})"
```
result
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
print(CLASS.__dict__): Show all the attribute
