 '''
 
 In this problem we will provide a list list_1 and we have written the delete_list_element function in solution.py for you. The list_1 of this function represents our initial list and the function will eventually return a list of elements that you need to delete from the 4th to the 7th element and return.

Write the relevant Python code in solution.py to return the list after the elements have been removed.

'''
 
 
 #my ugly solution
 
 def del_list_element(list_1:list) -> list:

    new_list = list_1[:3]
    new_list.extend(list_1[6:])
    return new_list
    
  
  
#another solution  
 def del_list_element(list_1:list) -> list:

 if len(list_1) < 7:
        return(list_1)
    else:
        list_1[3:6] = []
        return list_1
