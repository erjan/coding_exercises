'''

Given a list of products goods, this list stores a 
number of product tuples, each with two elements, representing
the product name and the product price. Please sort the entire list 
of items by price, and if the prices are the same sort by the item name in canonical order, then return 
the item name with the most expensive price.

'''

def get_goods(goods: list) -> str:
    # Please write your code here



    goods.sort(key=lambda x: [x[1], x[0]])
    return goods[-1][0]
