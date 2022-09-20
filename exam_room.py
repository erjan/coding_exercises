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

    def __init__(self, n: int):
        self.n = n
        self.lst = []

    def seat(self) -> int:
        if self.lst == []:
            self.lst.append(0)
            return 0
        else:
            index = 0 
            diff = self.lst[0]
            for i in range(1,len(self.lst)+1):
                if i == len(self.lst):
                    tmp = self.n - 1 - self.lst[i-1]
                else:
                    tmp = (self.lst[i] - self.lst[i-1])//2
                if  tmp > diff:
                    diff  = tmp
                    index = i
            #print(self.lst,diff,index)
            if index ==0: 
                self.lst.insert(0,0)
                return 0
            elif index == len(self.lst):
                self.lst.append(self.n-1)
                return self.n-1
            else:
                self.lst.insert(index,self.lst[index-1]+diff)
                return diff+self.lst[index-1]
    def leave(self, p: int) -> None:
        self.lst.remove(p)
