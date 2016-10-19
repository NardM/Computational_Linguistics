from basicText import basicText
import task.taskTwo as search_words
from task.taskTwo import taskTwo
import re
import copy


class taskThree(taskTwo):
    def __init__(self, text):
        super().__init__(text)
        self.words = search_words.search_words(text)

    def sort_alphabetically(self):
        # word = list(set(copy.deepcopy(self.words)))
        # word.sort()
        self.solve_3()
        # print('\n'.join(word))
        print('\n')

    def sort_list(self):
        words = copy.deepcopy(self.words)
        words.sort()

        def generator_words(words):
            for word in words:
                yield word

        def count_word(g):
            word = g.__next__()
            count = 1
            dict_words = dict()
            while True:
                try:
                    word_next = g.__next__()
                except StopIteration:
                    if word == word_next:
                        dict_words.update({word_next, count})
                        # print('Слово: {}, Количество: {}\n'.format(word_next, count))
                    break
                finally:
                    if word == word_next:
                        count += 1
                    else:
                        dict_words.update({word, count})
                        # print('Слово: {}, Количество: {}\n'.format(word, count))
                        count = 1
                        word = word_next

            return dict_words

        g = generator_words(words)
        dict_words = count_word(g)
        print(dict_words)

    def sort_alphabetically_reversed(self):
        words = [x[::-1] for x in re.findall(r'[A-z\']+', self.text)]
        word = list(set(words))
        word.sort()
        print('\n'.join(word))
        print('\n')
