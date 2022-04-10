
'''

Please complete the code in solution.py to realize the function 
of reverse_k_group. The reverse_k_group function has two parameters: the string str_in and the 
positive integer k. Given a string, reverse each of k characters, and finally returns the updated string.
If the last remaining strings are less than k, keep the last 
remaining strings in the original order

'''

def reverse_k_group(str_in, k) -> str:
    """
    :param str_in: The first input list
    :param k: Reverse every k strings
    :return: The str_in after reverse
    """
    s = str_in
    q,r = divmod(len(s),k)

    full = s[:q*k]
    rem = s[-r:]
    full = list(full)

    for i in range(0,len(full),k):
    
        full[i:i+k] = full[i:i+k][::-1]
    
    full = "".join(full)

    if r != 0:
        full = full + rem

    #print(full)
    return full
  
  
  --------------------------
  def reverse_k_group(str_in, k) -> str:
    """
    :param str_in: The first input list
    :param k: Reverse every k strings
    :return: The str_in after reverse
    """
    times = len(str_in) // k
    remain = len(str_in) % k
    result = ''
    for i in range(1, times+1):
        for j in range(i*k-1, (i-1)*k-1, -1):
            result += str_in[j]
    if remain > 0:
        result += str_in[-remain:] 
    return result

