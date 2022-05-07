class Test:
    def __init__(self, name, salary):
        self.v1 = name
        self.v2 = salary
val = Test('John', 50000)
print(val.__str__())
print(val.__repr__())