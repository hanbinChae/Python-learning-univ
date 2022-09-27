n=1
answer = 0

def addy(n,answer):
    answer+=n
    n += 1
    if n>100:
        return answer
    else:
        return addy(n,answer)

print(addy(n,answer))