
'''

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 
 
 '''


from collections import defaultdict

""" 
https://www.notion.so/paulonteri/Hashtables-Hashsets-220d9f0e409044c58ec6c2b0e7fe0ab5#cf22995975274881a28b544b0fce4716
"""

class Solution(object):
    def invalidTransactions(self, transactions):
        """ 
        - Record all transactions done at a particular time. Recording the person and the location. Example:
            `['alice,20,800,mtv','bob,50,1200,mtv','bob,20,100,beijing']` :\n
            ` 
            {   
            20: {'alice': {'mtv'}, 'bob': {'beijing'}}, 
            50: {'bob': {'mtv'}}
            } 
            ` \n
            `{time: {person: {location}, person2: {location1, location2}}, time: {person: {location}}}`
        - For each transaction, check if the amount is invalid - and add it to the invalid transactions if so.
        - For each transaction, go through invalid times (+-60), check if a transaction by the same person happened
            in a different city - and add it to the invalid transactions if so.
        """
        invalid = []

        # Record all transactions done at a particular time
        #   including the person and the location.
        transaction_time = defaultdict(dict)
        for transaction in transactions:
            name, str_time, amount, city = transaction.split(",")
            time = int(str_time)

            if name not in transaction_time[time]:
                transaction_time[time][name] = {city, }
            else:
                transaction_time[time][name].add(city)

        for transaction in transactions:
            name, str_time, amount, city = transaction.split(",")
            time = int(str_time)

            # # check amount
            if int(amount) > 1000:
                invalid.append(transaction)
                continue

            # # check if person did transaction within 60 minutes in a different city
            for inv_time in range(time-60, time+61):
                if inv_time not in transaction_time:
                    continue
                if name not in transaction_time[inv_time]:
                    continue

                trans_by_name_at_time = transaction_time[inv_time][name]

                # check if transactions were done in a different city
                if city not in trans_by_name_at_time or len(trans_by_name_at_time) > 1:
                    invalid.append(transaction)
                    break

        return invalid
       
--------------------------------------

from collections import defaultdict

""" 
https://www.notion.so/paulonteri/Hashtables-Hashsets-220d9f0e409044c58ec6c2b0e7fe0ab5#cf22995975274881a28b544b0fce4716
"""

class Solution(object):
    def invalidTransactions(self, transactions):
        
        invalid = []
        tr_time = defaultdict(dict)

        for tr in transactions:

            tr = tr.split(',')

            name = (tr[0])
            time = (int(tr[1]))
            amount = (int(tr[2]))
            city = (tr[3])

            if name not in tr_time[time]:
                tr_time[time][name] = {city,}
            else:
                tr_time[time][name].add(city)

        for t in transactions:
            name, time , amount,city =t.split(',')
            time = int(time)
            if int(amount)>1000:
                invalid.append(t)
                continue

            for q in range(time-60, time+61):
                if q not in tr_time:
                    continue
                if name not in tr_time[q]:
                    continue

                t_by_time = tr_time[q][name]
                if city not in t_by_time or len(t_by_time)>1:
                    invalid.append(t)
                    break
        return invalid
---------------------------------------------------------
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
        r = {}
                
        inv = []        
        for i in transactions:
            split = i.decode("utf-8").split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            if time not in r:
                r[time] = {
                    name: [city]
                }
            else:
                if name not in r[time]:
                    r[time][name]=[city]
                else:
                    r[time][name].append(city)
                    
        
        for i in transactions:
            split = i.decode("utf-8").split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            
            if amount > 1000:
                inv.append(i)
                continue
            
            for j in range(time-60, time+61):
                if j not in r:
                    continue
                if name not in r[j]:
                    continue
                if len(r[j][name]) > 1 or (r[j][name][0] != city):
                    inv.append(i)
                    break
                                        
        return inv   
