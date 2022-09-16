'''
There is a supermarket that is frequented by many customers. The products sold at the supermarket are represented as two parallel integer arrays products and prices, where the ith product has an ID of products[i] and a price of prices[i].

When a customer is paying, their bill is represented as two parallel integer arrays product and amount, where the jth product they purchased has an ID of product[j], and amount[j] is how much of the product they bought. Their subtotal is calculated as the sum of each amount[j] * (price of the jth product).

The supermarket decided to have a sale. Every nth customer paying for their groceries will be given a percentage discount. The discount amount is given by discount, where they will be given discount percent off their subtotal. More formally, if their subtotal is bill, then they would actually pay bill * ((100 - discount) / 100).

Implement the Cashier class:

Cashier(int n, int discount, int[] products, int[] prices) Initializes the object with n, the discount, and the products and their prices.
double getBill(int[] product, int[] amount) Returns the final total of the bill with the discount applied (if any). Answers within 10-5 of the actual value will be accepted.
'''

class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n, self.i, self.d = n, 0, discount
        self.price = {product: price for product, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.i += 1
        s = sum(self.price[p] * a for p, a in zip(product, amount))
        return s if self.i % self.n else s * (1 - self.d / 100)
      
---------------------------------------------------------------------------------------------------------
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        
        self.n = n 
        self.discount = discount 
        self.price = { }
        self.customer = 0 
        
        for i in range(len(products))  : 
            self.price[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        
        self.customer += 1
        
        bill = 0 
        
        for i in range(len(product)) : 
            bill += amount[i] * self.price[product[i]]
        
        
        if self.customer == self.n : 
            bill = bill * (1 - self.discount / 100)
            self.customer = 0 
            
            
        return bill
