from item import Item
from phone import Phone


item1 = Item("MyItem", 750)

item1.apply_increment(0.2)
print(item1.price)