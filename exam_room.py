'''
There is an exam room with n seats in a single row labeled from 0 to n - 1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number 0.

Design a class that simulates the mentioned exam room.

Implement the ExamRoom class:

ExamRoom(int n) Initializes the object of the exam room with the number of the seats n.
int seat() Returns the label of the seat at which the next student will set.
void leave(int p) Indicates that the student sitting at seat p will leave the room. It is guaranteed that there will be a student sitting at seat p.
 
 '''
class ExamRoom:
    def __init__(self, N: int):
        self.occupied = []
        self.N = N

    def seat(self) -> int:
        if not self.occupied: 
            self.occupied.append(0)
            return 0
        left, right = -self.occupied[0], self.occupied[0]
        maximum = (right - left) // 2
        for start, end in zip(self.occupied, self.occupied[1:] + [2 * self.N - 2 - self.occupied[-1]]):
            if (end - start) // 2 > maximum:
                left, right = start, end
                maximum = (right - left) // 2
        bisect.insort(self.occupied, left + maximum)
        return left + maximum
            
    def leave(self, p: int) -> None:
        self.occupied.remove(p)
