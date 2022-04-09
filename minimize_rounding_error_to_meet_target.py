'''
Given an array of prices [p1,p2...,pn] and a target, round 
each price pi to Roundi(pi) so that the rounded array [Round1(p1),Round2(p2)...,Roundn(pn)] sums to the given target. Each 
operation Roundi(pi) could be either Floor(pi) or Ceil(pi).

Return the string "-1" if the rounded array is impossible to 
sum to target. Otherwise, return the smallest rounding error, which is 
defined as Σ |Roundi(pi) - (pi)| for i from 1 to n, as a string with three places after the decimal.

'''

def minimizeError(self, prices: List[str], target: int) -> str:
        
        float_prices = [float(price) for price in prices]
        
        # 1. Compute the min rounded sum:
        rounded_sum = 0
        rounding_error = 0
        for price in float_prices:
            rounded_price = floor(price)
            
            rounded_sum += rounded_price
            rounding_error += price - rounded_price
        if rounded_sum >= target: # STOP
            return '%.3f' % rounding_error if rounded_sum == target else '-1'
        
        elif rounded_sum + len(prices) < target:
            return '-1'
        
        # 2. Replace 1 floor by ceil at a time until we reach target: choose the price with the min rounding error
        float_prices.sort(key=lambda price: ceil(price) - price) # ... Sort prices by ceil error to get the min rounding error
        for price in float_prices:
            rounded_sum += ceil(price) - floor(price) # +1 or +0
            rounding_error += (ceil(price) - price) - (price - floor(price)) # Replace the floor rounding by the ceil rounding
            
            if rounded_sum >= target:
                break
        
        return '%.3f' % rounding_error if rounded_sum == target else '-1'
