from item import Item

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

