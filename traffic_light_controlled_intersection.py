'''
Design a deadlock-free traffic light controlled system at this intersection.

Implement the function void carArrived(carId, roadId, direction, turnGreen, crossCar) where:

carId is the id of the car that arrived.
roadId is the id of the road that the car travels on.
direction is the direction of the car.
turnGreen is a function you can call to turn the traffic light to green on the current road.
crossCar is a function you can call to let the current car cross the intersection.
Your answer is considered correct if it avoids cars deadlock in the intersection. Turning the light green on a road when it was already green is considered a wrong answer.
'''


import threading

class TrafficLight:
    def __init__(self):
        self.lock = threading.Lock()
        self.roadIdGreen = 1

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        
        self.lock.acquire()
        
        if roadId != self.roadIdGreen:
            self.roadIdGreen = roadId
            turnGreen()

        crossCar()            
            
        self.lock.release()
