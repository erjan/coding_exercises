'''
You have a keypad with 9 buttons, numbered from 1 to 9, each mapped to lowercase English letters. You can choose which characters each button is matched to as long as:

All 26 lowercase English letters are mapped to.
Each character is mapped to by exactly 1 button.
Each button maps to at most 3 characters.
To type the first character matched to a button, you press the button once. To type the second character, you press the button twice, and so on.

Given a string s, return the minimum number of keypresses needed to type s using your keypad.

Note that the characters mapped to by each button, and the order they are mapped in cannot be changed.
'''


'''
Explanation
Idea: Always make the letters with higher frequency to be easier accessible.
Say there are 3 letters on one button (left - mid - right). Left is the easiest to access, mid is the second, right is the hardest.
Steps:
Sort letter with frequency reversely, then assign each with following orders
1-left, 2-left, 3-left, ... 9-left | 9 in total (easiest to access)
1-mid, 2-mid, 3-mid, ... 9-mid | 9 in total
1-right, 2-right, 3-right, ... 8-right | 8 in total, since at most 26 letters (hardest to access)
Intuitive
'''


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = collections.Counter(s)
        ans = cnt = 0
        for i, freq in enumerate(sorted(c.values(), reverse=True)):  # sort reversely
            if i % 9 == 0:
                cnt += 1
            ans += cnt * freq                                        # add `num_of_time_to_press_the_key * frequency` to result
        return ans

