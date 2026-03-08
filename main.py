from drone import Drone
from detector import Radar
from logger import Logger
import random

def run():
    radar = Radar(40, 50, 25)
    logger = Logger("logs.txt")

    drones = []
    for i in range(5):
        drone = Drone(random.uniform(0,100), random.uniform(0, 100),
    random.uniform(10,50), random.uniform(50,200))
        drones.append(drone)

    for drone in drones:
        print(f"Drone: ({drone.x:.1f}, {drone.y:.1f}) | Distance: {((drone.x-radar.x)**2 + (drone.y-radar.y)**2)**0.5:.1f}")
        result = radar.scan(drone.x, drone.y)
        print(f"Result: {result}")
        if result == "DETECTED":
            logger.log(drone.x, drone.y, "DETECTED")
            drone.move_toward(radar.x, radar.y)
            logger.log(drone.x, drone.y, "TARGET ELIMINATED")
        else:
            logger.log(drone.x, drone.y, "SAFE")

if __name__ == "__main__":
    run()
