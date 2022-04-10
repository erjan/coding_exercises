'''

In using for loops we sometimes encounter situations where we don't have to execute the loop completely, but have to jump out of the loop when certain conditions are met, so we use continue, break, return, etc.

continue is to continue the loop (execute the for loop from the beginning)
break is to jump out of the loop (end the loop)
return is to return the function value (all functions within the loop are not executed)
The words that Xiao Yi likes have the following characteristics.

Each letter of the word is a capital letter
Words do not have consecutive equal letters
For example: Xiao Yi does not like "ABBA" because there are two consecutive 'B's

You are given a word and you have to answer whether Xiao Yi will like this word or not?

Enter a description:

The input is a string of all uppercase letters, less than 100 in length

Output Description:

If Xiao Yi likes the word return "Likes", if not return "Dislikes"

Please write the relevant python code in solution.py to implement the above functionality, and we will import the module you wrote in main.py to check if your code implements the above functionality.
'''

def solution(var_str):
    # Iterate through the string

    for i in range(len(var_str)):
        if var_str[i] < 'A' and var_str[i] >'Z':
            return 'Dislikes'

    # Determine if the character is in A ~ Z. If not, return 'Dislikes'

    # Determine if this character is the last character
        if i != len(var_str)-1:
            if var_str[i] == var_str[i+1]:
                return 'Dislikes'
    # Determine if this character is equal to the next character, and if so, return 'Dislikes'
        else:
            continue
    # If not, continue the for loop
    return 'Likes'
    # If the loop does not return after execution, return 'Likes'
