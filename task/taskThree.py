from basicText import basicText
import task.taskTwo as search_words
import re
import copy


class taskThree(basicText):
    def __init__(self, text):
        super().__init__(text)
        self.words = search_words.search_words(text)

    def sort_alphabetically(self):
        word = copy.deepcopy(self.words)
        word = list(set(word))
        word.sort()
        print('\n'.join(word))
        print('\n')

    def sort_list(self):
        words = [x for x in sorted(copy.deepcopy(self.words), key=lambda a: len(a))]

        def generator_words(words):
            for word in words:
                yield word

        def count_word(g):
            word = g.__next__()
            count = 1
            while True:
                try:
                    word_next = g.__next__()
                except StopIteration:
                    if word == word_next:
                        print('Слово: {}, Количество: {}\n'.format(word_next, count))
                    break
                finally:
                    if word == word_next:
                        count += 1
                    else:
                        print('Слово: {}, Количество: {}\n'.format(word, count))
                        count = 1
                        word = word_next

        def __reversed__(self):

        g = generator_words(words)
        count_word(g)
