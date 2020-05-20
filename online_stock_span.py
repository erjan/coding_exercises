#Write a class StockSpanner which collects daily price quotes for 
#some stock, and returns the span of that stock's price for the current day.

#The span of the stock's price today is 
#defined as the maximum number of consecutive days (starting from today and going backwards) for
#which the price of the stock was less than or equal to today's price.

class StockSpanner {
    stack<pair<int,int>> s; //1st is index and 2nd is value
    int index;
public:
    StockSpanner() {
        ios::sync_with_stdio(false);
        cin.tie(0);
        index = -1;
    }
    
    int next(int price) {
        index +=1;
        
        while(!s.empty() && s.top().second<=price)    //Find the previous greater element
            s.pop();
        //If there is no previous greater element
        if(s.empty())
        {   s.push({index,price});      return index+1;   }
        
        int result = s.top().first;
        s.push({index,price});
        return index-result;        
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
