class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.double = []

    def book(self, start: int, end: int) -> bool:
        # check if overlaps with double
        i = 0
        while i < len(self.double):
            if end <= self.double[i][0]:
                break
            elif start >= self.double[i][1]:
                i += 1
            else:
                return False

        # book the event
        i = 0
        while i < len(self.events):
            if start <= self.events[i][0]:
                self.events.insert(i, (start, end))
                break
            else:
                i += 1
        else:
            self.events.append((start, end))

        # find new doubles
        j = 0
        lst_doubles = []
        while j < len(self.events):
            if (j != i and start < self.events[j][1] and
                    self.events[j][0] < end):
                lst_doubles.append((max(self.events[j][0], start),
                                    min(self.events[j][1], end)))
            elif end <= self.events[j][0]:
                break
            j += 1

        # update doubles
        for s, e in lst_doubles:
            i = 0
            while i < len(self.double):
                if e <= self.double[i][0]:
                    self.double.insert(i, (s, e))
                    break
                elif s >= self.double[i][1]:
                    i += 1
                else:
                    # we should not reach this point
                    return False
            else:
                self.double.append((s, e))
        return True
      
-------------------------------------------------------------------------------------------------
class MyCalendarTwo:
    
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))  # --- NOTE [1]
        self.calendar.append((start, end))
        return True
