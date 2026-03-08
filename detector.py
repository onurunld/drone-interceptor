import math

class Radar:
    def __init__(self, x, y, detection_range):
        self.x = float(x)
        self.y = float(y)
        self.detection_range = detection_range

    def scan(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance <= self.detection_range:
            return "DETECTED"
        else:
            return "SAFE"


