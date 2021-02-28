class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        num_items = 0
        for item in items:
               
            type_i = item[0]
            color_i = item[1]
            name_i = item[2]
            print(type_i, color_i, name_i)
            rule1 = (ruleKey == "type" and ruleValue == type_i)
            rule2 = (ruleKey == "color" and ruleValue == color_i)
            rule3 = (ruleKey == "name" and ruleValue == name_i)
            if rule1:
                num_items+=1
            elif rule2:
                num_items+=1
            elif rule3:
                num_items+=1
        return num_items

                
        

items = [["phone","blue","pixel"],["computer","silver","lenovo"],
         ["phone","gold","iphone"]]

ruleKey = "color"
ruleValue = "silver"

'''
#this problem is about knowing how to iterate!!!!
nested for loop on this one gives me error - dont go one level deeper , it will start iterating over letters in each word!!
e.g. phone, blue, pixel:
    for i in item:
        i[0] - p
        i[1] - h
        i[2] - o
        instead of actual items! nested loop on item produces letters!!
'''        
