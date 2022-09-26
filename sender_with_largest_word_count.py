'''
You have a chat log of n messages. You are given two string arrays messages and senders where messages[i] is a message sent by senders[i].

A message is list of words that are separated by a single space with no leading or trailing spaces. The word count of a sender is the total number of words sent by the sender. Note that a sender may send more than one message.

Return the sender with the largest word count. If there is more than one sender with the largest word count, return the one with the lexicographically largest name.

Note:

Uppercase letters come before lowercase letters in lexicographical order.
"Alice" and "alice" are distinct.

'''


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        
        d = defaultdict(list)
        words = list()

        for msg in messages:
            words.append(msg.count(' ') + 1)

        for s, w in zip(senders, words):
            d[s].append(w)

        for k, v in d.items():
            d[k] = sum(v)

        d = dict(d)

        maxi_v = sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][1]

        newd = dict()

        for k, v in d.items():
            if v == maxi_v:
                newd[k] = v

        newd = sorted(newd.items(), key=lambda x: (x[0]))
        newd = list(newd)[-1]
        res = newd[0]
        print(res)
        return res
      
---------------------------------------------------------------------------------------

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d={}
        l=[]
        for i in range(len(messages)):
            if senders[i] not in d:
                d[senders[i]]=len(messages[i].split())
            else:
                d[senders[i]]+=len(messages[i].split())
        x=max(d.values())
        for k,v in d.items():
            if v==x :
                l.append(k)
        if len(l)==1:
            return l[0]
        else:
            l=sorted(l)[::-1]      #Lexigograhical sorting of list
            return l[0]
