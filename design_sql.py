'''
You are given n tables represented with two arrays names and columns, where names[i] is the name of the ith table and columns[i] is the number of columns of the ith table.

You should be able to perform the following operations:

Insert a row in a specific table. Each row you insert has an id. The id is assigned using an auto-increment method where the id of the first inserted row is 1, and the id of each other row inserted into the same table is the id of the last inserted row (even if it was deleted) plus one.
Delete a row from a specific table. Note that deleting a row does not affect the id of the next inserted row.
Select a specific cell from any table and return its value.
Implement the SQL class:

SQL(String[] names, int[] columns) Creates the n tables.
void insertRow(String name, String[] row) Adds a row to the table name. It is guaranteed that the table will exist, and the size of the array row is equal to the number of columns in the table.
void deleteRow(String name, int rowId) Removes the row rowId from the table name. It is guaranteed that the table and row will exist.
String selectCell(String name, int rowId, int columnId) Returns the value of the cell in the row rowId and the column columnId from the table name.
 
 '''


from collections import defaultdict

class Table:    
    DELETED = "deleted"
    def __init__(self, name, column_count) -> None:
        self.name = name
        self.column_count = column_count
        self.rows = []
    
    def add_row(self, row: List[str]):
        if len(row) != self.column_count:
            raise Exception('invalid rows')
        self.rows.append(row)
    
    def delete_row(self, row_id: int):
        self.rows[row_id-1].append(Table.DELETED)
    
    def get_cell(self, row_id: int, column: int) -> str:
        if self.rows[row_id-1][-1] == Table.DELETED:
            raise Exception('invalid row id')
        return self.rows[row_id-1][column-1]        

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.db = defaultdict(Table)
        for name, column in zip(names, columns):
            self.db[name] = Table(name, column)

    def insertRow(self, name: str, row: List[str]) -> None:
        self.db[name].add_row(row)
        
    def deleteRow(self, name: str, rowId: int) -> None:
         self.db[name].delete_row(rowId)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.db[name].get_cell(rowId, columnId)
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)

----------------------------------------------------------------------------------------------------
class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {name: {"nextId": 1} for name in names}

    def insertRow(self, name: str, row: List[str]) -> None:
        """ Insert row into table. Raise KeyError if table does not exist. """
        table = self.tables[name]
        rowId = table["nextId"]
        table[rowId] = row
        table["nextId"] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        """ Idempotently delete a table row by ID. Raise KeyError if table does not exist. """
        self.tables[name].pop(rowId, None)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        """ Return cell in table. Raise KeyError if table, row, or column does not exist. """
        return self.tables[name][rowId][columnId-1]  
      
--------------------------------------------------------------------------------------------------------------------
Since the rows to be inserted have the correct size already, we don't really need to worry about the number of columns in a table. We will simply append new rows to the current table, so we don't really need to keep track of the id of the rows either.

Note columns are also 1-indexed.

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {name: [] for name in names}

    def insertRow(self, name: str, row: List[str]) -> None:
        self.tables[name].append(row)

    def deleteRow(self, name: str, rowId: int) -> None:
        self.tables[name][rowId - 1] = None # we could simpy `pass` this, but this releases the memory that was allocated for the deleted row

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId - 1][columnId - 1]
---------------------------------------------------------------------------------------------------------------------------
In an interview setting, the interviewer may ask questions like:

Is this the most space effecient?
What happens if we insert, select, or delete a row in a non-existing table?
What happens if we select or delete a non existing row?
What happens if we insert too many or too few columns?
For the last question, I would store the columnCount for each table. During insert, if the count does not match, I would raise a ValueError with a useful message. I would do this for too few columns because if we're given 3 columns and we expect 9, do we assume they should be inserted as the first 3? Should we add an offset=0 parameter to account for this? We would still need the columnCount to ensure we don't go out of bounds.

class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {name: {"nextId": 1} for name in names}

    def insertRow(self, name: str, row: List[str]) -> None:
        """ Insert row into table. Raise KeyError if table does not exist. """
        table = self.tables[name]
        rowId = table["nextId"]
        table[rowId] = row
        table["nextId"] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        """ Idempotently delete a table row by ID. Raise KeyError if table does not exist. """
        self.tables[name].pop(rowId, None)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        """ Return cell in table. Raise KeyError if table, row, or column does not exist. """
        return self.tables[name][rowId][columnId-1]  
