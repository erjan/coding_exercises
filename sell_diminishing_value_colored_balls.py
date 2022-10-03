'''
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.
'''


def maxProfit(self, inventory: List[int], orders: int) -> int:

    ctr = collections.Counter(inventory)
    ls = sorted([-k for k in ctr.keys()] + [0])

    maxEarn = 0
    ordersRemaining = True
    while orders and ls and ordersRemaining:
        curV = -heapq.heappop(ls)
        nxV = -ls[0]
        height = curV - nxV
        divM = 0
        width = ctr[curV]
        if (width * height) > orders:
            ordersRemaining = False
            height, divM = map(int, divmod(orders, width))
        maxEarn = (
            maxEarn
            + (width * ((height * curV) - ((height * (height - 1)) // 2)))
            + (divM * (curV - height))
        )
        maxEarn = int(maxEarn % ((10 ** 9) + 7))
        orders = orders - (height * width) - divM
        if ordersRemaining:
            del ctr[curV]
            ctr[nxV] = ctr[nxV] + width
            orders = orders - (width * height)
    return int(maxEarn % (1e9 + 7))
