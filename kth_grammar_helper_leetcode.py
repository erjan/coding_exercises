def f(n: int, k: int) -> int:
    s = [["0"]]

    if n == 0:
        return s[0][0]

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

        s.append(cur_row)

    print("answer is ")
    print(s[k - 1][0])
    return s[k-1][0]


f(2, 2)
