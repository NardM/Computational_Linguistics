from basicText import basicText
import re
import copy


class taskThree(basicText):
    def __init__(self, text):
        super().__init__(text)
        self.words = [x for x in re.findall(r'[A-z\']+', self.text)]

    def sort_alphabetically(self):
        word = copy.deepcopy(self.words)
        # word = list(copy(self.words))
        word = list(set(word))
        word.sort()

        # print(words)
        # print('\n'.join(word))
        print('\n')

    def sort_list(self):
        word = copy.deepcopy(self.words)
        words = [x for x in sorted(word, key=lambda a: len(a))]

        # print(words)

        def s(wordd):
            for i in wordd:
                yield i

        a = 0

        def test(wordd):

            i = s(wordd)
            if next(i) == i:
                print(1)
            else:
                print(i, 1)
                a = 0

        test(word)
