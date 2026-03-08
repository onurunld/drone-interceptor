import math

class Drone:
    def __init__(self, x, y, speed, fuel):
        self.x = float(x)
        self.y = float(y)
        self.speed = speed
        self.fuel = fuel

    def distance_to(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        distance = math.sqrt(dx**2 + dy**2)
        return float(distance)

    def move_toward(self, tx, ty) -> float:
        dx = tx - self.x
        dy = ty - self.y
        distance = math.sqrt(dx**2 + dy**2)


        if distance < 0.001:
            print("Already at target")
            return 0.0
        else:
            step = min(distance, self.speed, self.fuel)
            ux = dx / distance
            uy = dy / distance
            self.x += ux * step
            self.y += uy * step
            self.fuel -= step
            return step


    def __str__(self):
        return f"{self.x} - {self.y} - {self.speed} - {self.fuel}"

    def __repr__(self):
        return f"Drone(position x='{self.x}', position y='{self.y}', speed='{self.speed}', fuel='{self.fuel}')"



