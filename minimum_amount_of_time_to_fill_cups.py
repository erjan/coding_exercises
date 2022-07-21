'''
You have a water dispenser that can dispense 
cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount
of length 3 where amount[0], amount[1], and amount[2] denote the 
number of cold, warm, and hot water cups you need to fill respectively. Return the minimum 
number of seconds needed to fill up all the cups.
'''

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        res = 0
        amount.sort(reverse=True)        
        while amount[0] >0:
            
            amount[0] -=1
            amount[1] -=1
            res+=1
            
            amount = sorted(amount, reverse=True)
        
        return res
            
            
        


-------------------------------------------------------------------------------
#heap another sol-n

class Solution {
public:
    int fillCups(vector<int>& amount) {
        priority_queue<int> q;
        for(auto i:amount)
            q.push(i);
        
        int ans = 0;
        while(q.top()!=0){
            int a = q.top();
            q.pop();
            int b = q.top();
            q.pop();
            if(a>0 and b>0){
                q.push(--a);
                q.push(--b);
                ans++;
            }else{
                q.push(--a);
                q.push(b);
                ans++;
            }
        }
        
        return ans;
    }
};

#heap solution
 int fillCups(vector<int>& amount) {
        priority_queue<int> pq;   //  max heap
        
        for(auto amt: amount)
            pq.push(amt);
        
        
        int count=0;
        while(!pq.empty())
        {
            if(pq.top()==0) break;   // if all bottles are filled
            if(pq.size()==1)         // if only one bottle is left , fill it in one by one time, so add the needed time to count
            {
               count+= pq.top();
               break;
            }
            int hot= pq.top();    // maxm cap
            pq.pop();
            int warm = pq.top();  // 2nd max cap
            pq.pop();
            
            
            count++;         //pourred both max n 2nd max , so increse counter
            if(hot>1) pq.push(--hot);     // if left amt is less then 0 , then we have alreday filled that cup
            if(warm>1)pq.push(--warm);    // so wont add to the queue
         
                
            
                
        }
        return count;
    }




#brain teaser solution
def fillCups(self, amount: List[int]) -> int:
        return max(int(math.ceil(sum(amount)/2)),max(amount))
