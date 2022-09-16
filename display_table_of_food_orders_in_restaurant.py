'''
Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.
'''

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        allDishes=set()
        myFood={}
        
        for name,tableNo,dish in orders:
            if dish not in allDishes:
                allDishes.add(dish)
                
            if (tableNo) in myFood:
                if dish in myFood[(tableNo)]:
                    myFood[(tableNo)][dish]=myFood[(tableNo)][dish]+1
                else:
                    myFood[(tableNo)][dish]=1
            else:
                myFood[(tableNo)]={dish:1}
        print(myFood)
        allDishes=sorted(allDishes)
        allFood=["Table"] +[d for d in allDishes ]
        res=[]
        res.append(allFood)
        
        for table in sorted(myFood, key=int): #int to sort tables ascendingly 
            t=[]
            t.append((table))
            for i in range(1,len(allFood)):
                currDish=allFood[i]
                if currDish in myFood[(table)]:
                    t.append(str(myFood[(table)][currDish]))
                else:
                    t.append('0')
            res.append(t)
        return res
      
------------------------------------------------------

def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dict_ = defaultdict(lambda: defaultdict(int)) # nested dictionary of [table][item] storing counts
        items = sorted(set(item for name,table,item in orders)) # unique items sorted lexicographically
        tables = sorted(set(table for name,table,item in orders), key=int) # unique table numbers sorted
        
        # build dictionary
        for name,table,item in orders:
            dict_[table][item] += 1
        
        # build result table row/column headers
        res = [['Table']+items]
        for table in tables:
            res.append([table])
            
        # append each value to result table based on row/column headers
        for i in range(1, len(res)):
            for j in range(1, len(res[0])):
                table, item = res[i][0], res[0][j]
                count = str(dict_[table][item])
                res[i].append(count)
        
        return res
      
---------------------------------------------------------

def displayTable(self, orders):
        map_={}
        res=[]
        arr=[]
        set_=set()
        for i in range(0, len(orders)):
            if int(orders[i][1]) not in map_:
                map_[int(orders[i][1])]=[orders[i][2]]
            else:
                map_[int(orders[i][1])].append(orders[i][2])
        map_=sorted(map_.items(), key=lambda x:x[0])
        for i in range(0, len(orders)):
            set_.add(orders[i][2])
        set_=list(set_)
        set_.sort()
        set_.insert(0,"Table")
        res.append(set_)
        # print(res)
        for i in map_:
            arr.append(str(i[0]))
            for j in set_[1:]:
                arr.append(str(i[1].count(j)))
            res.append(arr)
            arr=[]
        # print(res)
        return res
