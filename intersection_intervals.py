'''
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.
'''


def intersect_or_not(i1, i2):
    s1 = i1[0]
    s2 = i2[0]
    e1 = i1[1]
    e2 = i2[1]
    intersect = False
    if s1 <= e2 and e1 >= s2:
        intersect = True
    return intersect

def get_interval(i1,i2):
    if intersect_or_not(i1, i2):
        s1 = i1[0]
        s2 = i2[0]
        e1 = i1[1]
        e2 = i2[1]
        result = [max(s1, s2), min(e1,e2)]
        return result
    

def main(a,b):
    a_ptr = 0
    b_ptr = 0
    final_list= list()
    while a_ptr < len(a) and b_ptr < len(b):
        
        interval1 = a[a_ptr]
        interval2 = b[b_ptr]
        if intersect_or_not(interval1, interval2):
            final_list.append(get_interval(interval1, interval2))
        #decide what pointer to increase:
        if interval1[1] > interval2[1]:
            b_ptr+=1
        else:
            a_ptr+=1
            
    print(final_list)
    return final_list


A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

main(A,B)
            
