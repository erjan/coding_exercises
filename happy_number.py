class Solution:
    
    def isHappy(self, n):
        def helper(self,n, seen_numbers):
            #print('-----%d' % n)
            str_n = str(n)
            total = 0
            for i in range(len(str_n)):
                temp = int(str_n[i])**2
                print(temp , end = ' ')
                total += temp
            print()
            print(total)

            
            if total!= 1:
                if total in seen_numbers:
                    print('cycle found, no happy number!')
                    return False
                else:
                    seen_numbers.append(total)
                    return helper(self,total, seen_numbers)
            else:
                print('happy number!')
                return True
            
        return helper(self,n,[])
        
d =Solution()
res = d.isHappy(19)    
print(res)
