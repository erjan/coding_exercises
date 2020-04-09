#Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

def f(s,t):
    s1, s2 = [],[]

    for i in range(len(s)):
        if s[i] == '#':
            if s1:
                s1.pop()
        else:
            s1.append(s[i])

    for i in range(len(t)):
        if t[i] == '#':
            if s2:
                s2.pop()
        else:
            s2.append(t[i])

    if s1 == s2:
        return True
    else:
        return False
