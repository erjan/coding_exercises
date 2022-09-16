'''
There is an ATM machine that stores banknotes of 5 denominations: 20, 50, 100, 200, and 500 dollars. Initially the ATM is empty. The user can use the machine to deposit or withdraw any amount of money.

When withdrawing, the machine prioritizes using banknotes of larger values.

For example, if you want to withdraw $300 and there are 2 $50 banknotes, 1 $100 banknote, and 1 $200 banknote, then the machine will use the $100 and $200 banknotes.
However, if you try to withdraw $600 and there are 3 $200 banknotes and 1 $500 banknote, then the withdraw request will be rejected because the machine will first try to use the $500 banknote and then be unable to use banknotes to complete the remaining $100. Note that the machine is not allowed to use the $200 banknotes instead of the $500 banknote.
Implement the ATM class:

ATM() Initializes the ATM object.
void deposit(int[] banknotesCount) Deposits new banknotes in the order $20, $50, $100, $200, and $500.
int[] withdraw(int amount) Returns an array of length 5 of the number of banknotes that will be handed to the user in the order $20, $50, $100, $200, and $500, and update the number of banknotes in the ATM after withdrawing. Returns [-1] if it is not possible (do not withdraw any banknotes in this case).
'''

class ATM:
    def __init__(self):
        self.cash = [0] * 5
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotes_count: List[int]) -> None:
        for i, n in enumerate(banknotes_count):
            self.cash[i] += n

    def withdraw(self, amount: int) -> List[int]:
        res = []
        for val, n in zip(self.values[::-1], self.cash[::-1]):
            need = min(n, amount // val)
            res = [need] + res
            amount -= (need * val)
        if amount == 0:
            self.deposit([-x for x in res])
            return res
        else:
            return [-1]
          
----------------------------------------------------------
class ATM:

    def __init__(self):
        self.count = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        self.count = [a + b for a, b in zip(self.count, banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        count = [0, 0, 0, 0, 0]
        trans = [20, 50, 100, 200, 500]

        for i in range(len(self.count) - 1, -1, -1):
            total = min(self.count[i], amount // trans[i])
            amount -= total * trans[i]
            count[i] += total

        if amount != 0:
            return [-1]

        self.deposit(list(map(lambda v: -v, count)))
        return count
