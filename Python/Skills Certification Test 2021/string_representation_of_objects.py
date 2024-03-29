class Car:
    def __init__(self, speed, unit):
        self.speed = speed
        self.unit = unit

    def __str__(self):
        return f"Car with the maximum speed of {self.speed} {self.unit}"

class Boat:
    def __init__(self, speed):
        self.speed = speed

    def __str__(self):
        return f"Boat with the maximum speed of {self.speed} knots"

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        sen = input().split()
        type, speed = sen[0], sen[1:]
        if type == "car":
            car = Car(speed[0], speed[1])
            print(car.__str__())
        else:
            boat = Boat(speed[0])
            print(boat.__str__())
