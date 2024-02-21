class Currency:
    currencies =  {'CHF': 0.930023, #swiss franc 
                    'CAD': 1.264553, #canadian dollar
                    'GBP': 0.737414, #british pound
                    'JPY': 111.019919, #japanese yen
                    'EUR': 0.862361, #euro
                    'USD': 1.0} #us dollar
    
    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
        An Currency object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    # repr and str are basically the same thing
    def __repr__(self):
        return f"{round(self.value,2)} {self.unit}"
    
    def __str__(self):
        return f"{round(self.value,2)} {self.unit}"
    
    # main functions of add and subtraction first
    def __add__(self,other):
        #Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.
        if type(other) == int or type(other) == float:
            x = (other * Currency.currencies[self.unit])
        else:
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
        return Currency(x + self.value, self.unit)
    
    def __sub__(self,other):
        if type(other) == int or type(other) == float:
            x = (other * Currency.currencies[self.unit])
        else:
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]) 
        return Currency(self.value - x, self.unit)
    
    # the __iadd__ and __isub__ are inplace productions of the orginal methods but modifies the original object (the one on the left side of the operator)
    # to store the result of the addition or subtraction without creating a new object
    def __iadd__(self, other):
        return Currency.__add__(self,other)

    def __isub__(self, other):
        return Currency.__sub__(self,other)
    
    # _radd_ and _rsub_ are reversed methods that will reverse the operation.. if u call x.__rsub__(y) you'll actually get y-x
    # its more of a foolproof double check incase the original x-y returns a NotImplemented value indicating the data types are incompatible.
    def __radd__(self, other):
        res = self + other
        if self.unit != "USD":
            res.changeTo("USD")
        return res

    def __rsub__(self, other):
        res = other - self.value
        res = Currency(res,self.unit)
        if self.unit != "USD":
            res.changeTo("USD")
        return res

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 

# Expected outcome
# 40.65 EUR
# 47.14 USD
# 26.02 EUR
# 30.17 USD
# 20.84 EUR
# 10.03 USD
