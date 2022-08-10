'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.
'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a
      
--------------------------
def getSum(a, b):
	if b == 0: return a
	return getSum(a ^ b, (a & b) << 1)

---------------------------------------------------
class Solution:
    def getSum(self, a: int, b: int) -> int:
        ## RC ##
        ## APPROACH : BITWISE OPERATIONS ##
        ## LOGIC ##
        #   1. For any two numbers, if their binary representations are completely opposite, then XOR operation will directly produce sum of numbers ( in this case carry is 0 )
        #   2. what if the numbers binary representation is not completely opposite, XOR will only have part of the sum and remaining will be carry, which can be produced by and operation followed by left shift operation.
        #   3. For Example 18, 13 => 10010, 01101 => XOR => 11101 => 31 (ans found), and operation => carry => 0
        #   4. For Example 7, 5
        #   1 1 1                   1 1 1
        #   1 0 1                   1 0 1
        #   -----                   -----
        #   0 1 0   => XOR => 2     1 0 1  => carry => after left shift => 1 0 1 0
        #   2                                                              10
        # now we have to find sum of 2, 10 i.e a is replace with XOR result and b is replaced wth carry result
        # similarly repeating this process till carry is 0
        #   steps will be 7|5 => 2|10 => 8|4  => 12|0
        
		## TIME COMPLEXITY : O(1) ##
		## SPACE COMPLEXITY : O(1) ##
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff # (python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit )
        while(b & mask > 0):
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a

---------------------------------------------------------------------
There's lot of answers here, but none of them shows how they arrived at the answer, here's my simple try to explain.

Eg: Let's try this with our hand 3 + 2 = 5 , the carry will be with in the brackets i.e "()"

3 => 011 
2=>  010
     ____
     1(1)01
Here we will forward the carry at the second bit to get the result.
So which bitwise operator can do this ? A simple observation says that XOR can do that,but it just falls short in dealing with the carry properly, but correctly adds when there is no need to deal with carry.
For Eg:

1   =>  001 
2   =>  010 
1^2 =>  011 (2+1 = 3) 
So now when we have carry, to deal with, we can see the result as :

3  => 011 
2  => 010 
3^2=> 001  
Here we can see XOR just fell short with the carry generated at the second bit.
So how can we find the carry ? The carry is generated when both the bits are set, i.e (1,1) will generate carry but (0,1 or 1,0 or 0,0) won't generate a carry, so which bitwise operator can do that ? AND gate ofcourse.

To find the carry we can do

3    =>  011 
2    =>  010 
3&2  =>  010
now we need to add it to the previous value we generated i.e ( 3 ^ 2), but the carry should be added to the left bit of the one which genereated it.
so we left shift it by one so that it gets added at the right spot.

Hence (3&2)<<1 => 100
so we can now do

3 ^2        =>  001 
(3&2)<<1    =>  100 

Now xor them, which will give 101(5) , we can continue this until the carry becomes zero.

A Java program which implements the above logic :

class Solution {
    public int getSum(int a, int b) {
      int c; 
      while(b !=0 ) {
        c = (a&b);
        a = a ^ b;
        b = (c)<<1;
      }
      return a;
        
    }
}
