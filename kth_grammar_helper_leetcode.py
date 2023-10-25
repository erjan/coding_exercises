
https://leetcode.com/problems/k-th-symbol-in-grammar/description/

this code is for the above leetcode exercise - generating bunch of lines into list of lists

def f(n: int, k: int) -> int:
    s = [["0"]]

    if n == 0:
        return s[0]


    for i in range(1, n):
        print("--------------------------------------------")
        print("prev row:")
        print(s[-1])

        prev_row = s[-1]
        cur_row = []

        for el in prev_row:
            print("cur element in row:" + str(el))
            cur = ""
            for x in el:
                if x == "0":
                    cur += "01"
                elif x == "1":
                    cur += "10"

            cur_row.append(cur)

        print()
        print("adding this row")
        print(cur_row)
        s.append(cur_row)

    print()
    print()
    print(s)


f(5, 2)
