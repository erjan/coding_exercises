'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
'''


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def digit_log(log):

            log = log.split(' ')
            log = log[1:]
            l = list(filter(lambda x: x.isdigit(), log))
            if len(l) == len(log):
                return True
            return False

        letter_logs = list()
        digit_logs = list()

        for i in range(len(logs)):
            log = logs[i]

            if not digit_log(log):
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        for i in range(len(letter_logs)):
            letter_logs[i] = letter_logs[i].split()

        letter_logs.sort(key=lambda x: x[0])
        letter_logs.sort(key=lambda x: x[1:])

        total = list()
        for i in range(len(letter_logs)):
            letter_logs[i] = " ".join(letter_logs[i])

        total = letter_logs
        total.extend(digit_logs)
        return total
