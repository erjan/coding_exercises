class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
            cur = current
            cor = correct
            
            cur = cur.split(':')

            print(cur)

            cur_h = int(cur[0])
            cur_m = int(cur[1])

            cur_total_m = cur_h*60 + cur_m

            cor = cor.split(':')
            cor_h = int(cor[0])
            cor_m = int(cor[1])

            cor_total_m = cor_h*60 + cor_m

            diff = abs(cur_total_m - cor_total_m)

            print(diff)

            count = 0

            full, remainder = divmod(diff, 60)
            count += full
            diff = remainder

            full, remainder = divmod(diff, 15)
            count += full

            diff = remainder
            full, remainder = divmod(diff, 5)
            count += full

            diff = remainder
            count += remainder

            print(diff)
            print('count', count)
            return count
          
          
#another

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time = 60 * int(current[0:2]) + int(current[3:5]) # Current time in minutes
        target_time = 60 * int(correct[0:2]) + int(correct[3:5]) # Current time in minutes
        diff = target_time - current_time # Difference b/w current and target times in minutes
        count = 0 # Required number of operations
        for i in [60, 15, 5, 1]:
            count += diff // i # add number of operations needed with i to count
            diff %= i # Diff becomes modulo of diff with i
        return count
      
      
#another

def convertTime(self, current: str, correct: str) -> int:
        if current==correct:
            return 0
        h=int(correct[:2])-int(current[:2])
        m=int(correct[3:])-int(current[3:])
        dit=h*60+m
        count=0
        if dit>=60:
            count+=dit//60
            dit=dit%60
        if dit>=15:
            count+=dit//15
            dit=dit%15   
        if dit>=5:
            count+=dit//5
            dit=dit%5    
        if dit>=1:
            count+=dit//1
            dit=dit%1    
        return count
