# Python_OOP
Object-Oriented Programming

[Definition]
assert: Use it to suggest the condition for input parameters
```python
  def __init__(self, name: str, price=0, quantity=0):
      # Run validations to the received arguments
      assert price >= 0
      assert quantity >= 0
```
