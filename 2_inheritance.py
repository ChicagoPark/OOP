import csv

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

    #decorator (Access to the function through Class)
    @classmethod
    def instantiate_from_csv(cls):
        # read the file
        with open('items.csv', 'r') as f:
            # read as dictionary
            reader = csv.DictReader(f)
            items = list(reader)
        # initiate from the inside of the class
        for item in items:
            Item(
                name=item.get('name'),
                price=int(item['price']), # same thing with the above and the below lines
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self): # responsible for representing the object(instance)
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

# inheritance
class Phone(Item):
    # super function is for inheritance, and we can add what we want to add.
    def __init__(self, name: str, price=0, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__( # with __init__ we can call __init__ function in Item class
                          # by listing the names, we can assign covering that process to parent class
            name, price, quantity
        )
        assert broken_phones >= 0, f"quantity {broken_phones} is not greater than zero"
        # Assign to self object
        self.broken_phones = broken_phones


#Item.instantiate_from_csv()
#print(Item.is_integer(7.0))

phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)
print(phone2.calculate_total_price())

print(Item.all)
print(Phone.all)
