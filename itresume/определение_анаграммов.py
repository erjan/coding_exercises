'''
Даны два слова: word1 и word2. Написать функцию anagram для определения, являются ли эти слова анаграммами.

Примечание: Анаграммами называются слова, которые состоят из одного и того же набора букв (и имеют одинаковую длину).
'''

class Answer:
    def anagram(self, word1, word2):
        word1 = list(word1)
        word2 = list(word2)
        
        word1.sort()
        word2.sort()
        
        return word1 == word2
