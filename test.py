word = [1, 1, 1, 1, 2, 3, 3, 4, 5, 5, 6, 4, 3, 5, 6, 6]

'''def s():
    for i in word:
        yield i
        test()
'''


def reader():
    """A generator that fakes a read from a file, socket, etc."""
    for i in range(4):
        yield '<< %s' % i


def reader_wrapper(g):
    # Manually iterate over data produced by reader
    for v in g:
        yield v


wrap = reader_wrapper(reader())
for i in wrap:
    # print(i)
    pass


def ss():
    for i in word:
        yield i


def sss(g):
    number = next(g)
    if number == next(number)():
        print("Yes")
    else:
        print("No")

s=sss(ss())

for w in s:
    print(w)