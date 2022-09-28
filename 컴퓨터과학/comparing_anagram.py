def same(a,b):
    a_li = []
    b_li = []
    if len(a) != len(b):
        print("다릅니다.")
        return 0
    else:
        for i in range(0,len(a)):
            a_li.append(ord(a[i]))
            b_li.append(ord(b[i]))
    a_li.sort()
    b_li.sort()
    if a_li == b_li:
        print("같습니다.")
        return 0
    else:
        print("다릅니다.")
        return 0

a = 'abtjkef'
b = 'tabkefj'

same(a,b)