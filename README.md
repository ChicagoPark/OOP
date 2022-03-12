# Python_OOP
Object-Oriented Programming

[Definition]

self: the scale of generated instance by BOSS class

assert: Use it to suggest the condition for input parameters (Good to prevent the error at the beginning)
```python
  def __init__(self, name: str, price=0, quantity=0):
      # Run validations to the received arguments
      assert price >= 0, f"Price {price} is not greater than zero"
      assert quantity >= 0, f"quantity {price} is not greater than zero"
```
print(CLASS.__dict__): Show all the attribute
