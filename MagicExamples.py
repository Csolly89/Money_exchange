# example magic method..
class Car:
    [...]

    def __str__(self):
        return f"make: {self.make}, model: {self.model}"
myCar = Car("Hyundai","Sonata")
print(myCar) #make: Hyundai, model: Sonata



class Car:
    [...]

    def __eq__(self,other): # ==
        if self.make == other.make and self.model == other.model:
            return True
        else:
            return False

    def __ne__(self,other): # !=
        if self == other:
            return False
        else:
            return True

car1 = Car("Hyundai","Sonata")
car2 = Car("Hyundai","Sonata")
car3 = Car("Honda","Accord")
print(car1 == car2) #True (self is car1, other is car2)
print(car1 == car3) #False (self is car1, other is car3)
print(car2 != car3) #True (self is car2, other is car3)

class Car:
    [...]

    def __str__(self):
        return f"make: {self.make}, model: {self.model}"

    def __repr__(self):
        return f"make: {self.make}, model: {self.model}"
