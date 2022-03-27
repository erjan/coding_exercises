'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
'''

#BASIC IDEA: calculate the distance on the go once we find 2 matching words

def shortest_distance(self, words: List[str], word1: str, word2: str) -> int:
    # Write your code here
    dist = float('inf')
    ind = [None, None]
    for i in range(len(words)):

        if words[i] == word1:
            ind[0] = i
        elif words[i] == word2:
            ind[1] = i
        if ind[0] != None and ind[1] != None:
            dist = min(dist, abs(ind[0]- ind[1]) )
    return dist
  
  
#output with prints...


def f(words, word1, word2):

    dis = sys.maxsize
    ind = [None, None]
    if len(words) == 0:
        return dis
    for i in range(len(words)):
        print('-----------------------------')
        print()
        if words[i] == word1:
            print('word1', word1, ' found at ', i)
            ind[0] = i
        elif words[i] == word2:
            print('word2', word2, ' found at ', i)
            ind[1] = i
        print(ind)

        if ind[0] != None and ind[1] != None:
            print('found 2 words')
            dis = min(dis, abs(ind[0] - ind[1]))
            print('calc distance...')
            print(ind[0], ind[1], 'the distance', dis)

    print(ind)

    return dis
