class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # (((((((((((
        # O(2^n), O(n)
        # backtracking approach

        self.longest_string = -1
        self.res = set()

        self.dfs(s, 0, [], 0, 0)

        return self.res

    def dfs(self, string, cur_idx, cur_res, l_count, r_count):
        if cur_idx >= len(string):
            if l_count == r_count:
                if len(cur_res) > self.longest_string:
                    self.longest_string = len(cur_res)

                    self.res = set()
                    self.res.add("".join(cur_res))
                elif len(cur_res) == self.longest_string:
                    self.res.add("".join(cur_res))
        
        else:
            cur_char = string[cur_idx]

            if cur_char == "(":
                cur_res.append(cur_char)
                # taking cur_char
                self.dfs(string, cur_idx + 1, cur_res, l_count + 1, r_count)

                # not taking cur_char
                cur_res.pop()
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)

            elif cur_char == ")":
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)

                # checking of l_count should be greater than r_count
                if l_count > r_count:
                    cur_res.append(cur_char)
                    # taking )
                    self.dfs(string, cur_idx + 1, cur_res, l_count, r_count + 1)

                    # not taking )
                    cur_res.pop()
            
            else: # this is for any character except "(" and ")"
                cur_res.append(cur_char)
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)
                cur_res.pop()


--------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.minDel = len(s) # 最小刪除數量，預設為字串長度(即可刪除的最大值)
        self.visited = set() # 已拜訪字串的集合(用來跳過重複搜索的字串)，也是不引發 TLE 的關鍵優化
        self.ans = set()     # 最終答案集合
        self.dfs(s, 0)
        # 若 ans 不為空則將其轉為 list 輸出，若為空則回傳 [""]
        return list(self.ans) if self.ans else [""]

    def dfs(self, S, count):
        # 放棄遞迴條件：字串為空、當前刪除數量 > 全域最小刪除數量、此字串已拜訪過(不需要重複拜訪)
        if (not S) or (count > self.minDel) or (S in self.visited):
            return

        self.visited.add(S) # 將此字串加入已拜訪集合
        
        # 若此字串為合法字串，進行處理並結束此次遞迴
        if self.isValid(S): 
            if count < self.minDel : # 若當前刪除數量 < 全域最小刪除數量
                self.minDel = count  # 則更新全域最小刪除數量
                self.ans = {S}       # 並重置 ans 集合
            elif count == self.minDel: # 若當前刪除數量 == 全域最小刪除數量
                self.ans.add(S)        # 則將新的字串加入 ans 集合
            return

        for i in range(len(S)):
            if S[i] in "()": # 若此字元為括號，則將其刪除，並進入下一層遞迴搜尋
                self.dfs(S[:i] + S[i+1:], count+1)

    def isValid(self, S):
        stack = list()
        for c in S:
            if c == "(":
                stack.append(0)
            elif c == ")":
                if stack: # 若有 ( 則消除
                    stack.pop()
                else: # 若無 ( 代表字串不合法
                    return False
        return stack == [] # 若堆疊為空代表為合法字串，反之不合法 
