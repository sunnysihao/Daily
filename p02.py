while True:
    try:
        s = input()
        dic = {}
        res = ''
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        Min = min(dic.values())
        for c in s:
            if dic[c] != Min:
                res += c
        print(res)
    except:
        break
