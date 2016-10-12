word = ['a','a','b']

'''def s():
    for i in word:
        yield i
        test()
'''


def generator(word):
    for i in word:
        yield i


a = 0


def sss(g):
    number = g.__next__()
    a = 1
    while True:
        try:
            number2 = g.__next__()
        except StopIteration:
            if number==number2:
                print(number2,a)
            break
        finally:
            if number == number2:
                a += 1
            else:
                print(number, a)
                a = 1
                number = number2


g = generator(word)
sss(g)
