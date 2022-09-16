'''
You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].

Execute all the valid transactions. A transaction is valid if:

The given account number(s) are between 1 and n, and
The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
Implement the Bank class:

Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
boolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.
boolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.
boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.
'''

class Bank:

    def __init__(self, bal: List[int]):
        self.store = bal  # storage list


    def transfer(self, a1: int, a2: int, money: int) -> bool:
        try:
            # checking if both accounts exist. and if the transaction would be valid
            if self.store[a1 - 1] >= money and self.store[a2 - 1] >= 0:
                # performing the transaction
                self.store[a1 - 1] -= money
                self.store[a2 - 1] += money
                return True
            else:
                # retrning false on invalid transaction
                return False
        except:
            # returning false when accounts don't exist
            return False


    def deposit(self, ac: int, mn: int) -> bool:
        try:
            # if account exists performing transaction
            self.store[ac - 1] += mn
            return True
        except:
            # returning false when account doesn't exist
            return False


    def withdraw(self, ac: int, mn: int) -> bool:
        try:
            # checking if transaction is valid
            if self.store[ac - 1] >= mn:
                # performing the transaction
                self.store[ac - 1] -= mn
                return True
            else:
                # returning false in case on invalid transaction
                return False
        except:
            # returning false when account doesn't exist
            return False
          
-----------------------------------------------------------------------

class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance
        self.noOfAccounts = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.noOfAccounts and 1 <= account2 <= self.noOfAccounts:
            if money <= self.accounts[account1 - 1]:
                self.accounts[account1 - 1] -= money
                self.accounts[account2 - 1] += money
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.noOfAccounts:
            self.accounts[account - 1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.noOfAccounts and self.accounts[account - 1] >= money:
            self.accounts[account - 1] -= money
            return True
        else:
            return False
