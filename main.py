class Vehicle:
    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price

    def __gt__(self, other):
        return self.speed > other.speed


v1 = Vehicle("Name1", 1000, 10000)
v2 = Vehicle("Name2", 110, 9000)

result = sorted([v1, v2], key=lambda x: x.speed)
