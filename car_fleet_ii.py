'''
There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.
'''

The problem can be solved with a heap or a stack. Heap solution is probably easier to arrive at, given that it only requires us to make two observations about the input, but involves writing more code. Stack solution is elegant and fast, but is harder to come up with, since we have to make more observations about the input.

Heap solution
The intuition behind this solution is that earlier collisions have the potential to affect later collisions and not vice versa. Therefore we'd like to process collisions in the order they are happening. For this, we put each car that has a potential to collide with the next one in a heap and order it based on the expected collision time based on cars' positions and speed. A car that has collided is no longer interesting to us, since the previous car can now only collide with the car that follows it. To emulate this behavior we place cars in a linked list so we can easily remove the car after collision.

Complexity
Time: O(NlogN)
Space: O(N)

class Car:
    def __init__(self, pos, speed, idx, prev=None, next=None):
        self.pos = pos
        self.speed = speed
        self.idx = idx
        self.prev = prev
        self.next = next

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        colis_times = [-1] * len(cars)
        cars = [Car(pos, sp, i) for i, (pos, sp) in enumerate(cars)]
        for i in range(len(cars)-1): cars[i].next = cars[i+1]
        for i in range(1, len(cars)): cars[i].prev = cars[i-1]
        
        catchup_order = [((b.pos-a.pos)/(a.speed-b.speed), a.idx, a)
                        for i, (a, b) 
                        in enumerate(zip(cars, cars[1:])) if a.speed > b.speed]
        heapify(catchup_order)
        
        while catchup_order:
            catchup_time, idx, car = heappop(catchup_order)
            if colis_times[idx] > -1: continue # ith car has already caught up
            colis_times[idx] = catchup_time
            if not car.prev: continue # no car is following us
            car.prev.next, car.next.prev = car.next, car.prev
            if car.next.speed >= car.prev.speed: continue # the follower is too slow to catch up
            new_catchup_time = (car.next.pos-car.prev.pos)/(car.prev.speed-car.next.speed)
            heappush(catchup_order, (new_catchup_time, car.prev.idx, car.prev))
        
        return colis_times
      
Stack solution
Observations:

For every car we only care about the cars ahead, because those are the ones that we can collide with.
Among those ahead of us, some are faster and we will never catch up with those, so we can ignore them.
Some of the cars ahead that are slower than us will be in a collision before us, those we can also ignore because after they collide they are not any different to us that the car they collided with.
Anything we ignore can also be safely ignored by the cars that follow us, because they can only go as fast as us after colliding with us.
Based on aforementioned observations we produce a stack solution below. We iterate over the cars starting from the last one and process the cars in front of us, getting rid of them if they are no longer interesting.
Tip: for index i, ~i will give us the index with the same offset from the end of the array, e.g. for == 0, ~i == -1, etc.

Complexity
Time: O(N)
Space: O(N)

    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        colis_times = [-1] * len(cars)
        cars_in_front_stack = []
        for i, (position, speed) in enumerate(reversed(cars)):
            while cars_in_front_stack:
                front_car_pos, front_car_speed, front_car_collision = cars_in_front_stack[-1]
                if front_car_speed >= speed or \
                   (our_collision_with_front := (front_car_pos - position) / (speed - front_car_speed)) >= front_car_collision: 
                    cars_in_front_stack.pop()
                else: break
            
            if cars_in_front_stack:
                front_car_pos, front_car_speed, front_car_collision = cars_in_front_stack[-1]
                colis_times[~i] = (front_car_pos - position) / (speed - front_car_speed)
            cars_in_front_stack.append((position, speed, colis_times[~i] if colis_times[~i] != -1 else inf))
        
        return colis_times      
