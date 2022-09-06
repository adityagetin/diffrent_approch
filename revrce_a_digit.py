def rev():
    x=int(input())
    list=[int(y) for y in str(x)]
    rev=list[::-1]
    s = [str(i) for i in rev]
    res = int("".join(s))
    print(list)
    print(rev)
    print(res)
rev()
