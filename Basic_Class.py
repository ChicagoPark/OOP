class Item:
    pay_rate = 0.8 # it doesn't need self since we have one pay_rate for BOSS class (Can be use for class level and instance level)
    all = []       # very convenient to manage all the instance from one BOSS class
    def __init__(self, name: str, price=0, quantity=0):
        # self is mandatory since class get the instance by itself as the first argument(think self=instance)
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"quantity {price} is not greater than zero"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        #self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

    def __repr__(self): # responsible for representing the object(instance)
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)
item2 = Item("Computer", 1000, 5)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


print(Item.all)
'''
for instance in Item.all:
    print(instance.name)
'''
