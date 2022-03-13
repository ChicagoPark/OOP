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
        self.__name = name      # by adding __ in front of variable, we can prevent it to be changed strongly.
                                # but we can edit __variable inside of the class by using function
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute (We can set function name with variable name)
    def name(self):
        return self.__name

    # name.setter Decorator = Write-Could-Be setting
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise Exception("The price is out of range")
        self.__price = value


    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        #self.price = self.price * Item.pay_rate
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price*increment_value

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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        Wd have {self.name} {self.quantity} times.
        Regards, JimShapedCoding
        """
    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()