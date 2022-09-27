'''
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.
'''

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj=defaultdict(list)
        ind=defaultdict(int)
        
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                adj[ingredients[i][j]].append(recipes[i])
                ind[recipes[i]]+=1
        ans=[]
        q=deque()
        for i in range(len(supplies)):
            q.append(supplies[i])
        while q:
            node=q.popleft()
            for i in adj[node]:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)
                    ans.append(i)
        return ans
