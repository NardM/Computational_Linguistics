from basicText import basicText
import task.taskTwo as search_words
from task.taskTwo import taskTwo
import re
import copy


class taskThree(taskTwo):
    def __init__(self, text):
        super().__init__(text)
        self.words = search_words.search_words(text)
        self.letters_abc = 'abcdefghijklmnopqrstuvwxyz'
        self.letters_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.words_all =  [x for x in sorted(copy.deepcopy(self.words), key=lambda a: len(a))]

    def __add__(self, other): #+
        pass

    def __sub__(self, other):
        pass

    def __rpow__(self, other): # a**=b
        pass

    def sort_alphabetically(self):
        word = list(set(copy.deepcopy(self.words)))
        word.sort()
        print('\n'.join(word))
        self.solve_3()
        #print('\n'.join([x for x in sorted(copy.deepcopy(self.words), key=lambda a: len(a))]))
        # print('\n'.join(word))
        print('\n')

    def sort_list(self):
        words = copy.deepcopy(self.words)
        words.sort()

        def generator_words(words):
            for word in words: # 5 4 4 4 3
                yield word

        def count_word(generator_words):
            word = g.__next__() # 5
            count = 1
            dict_words = dict()
            while True:
                try:
                    word_next = g.__next__() # 4
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
                        word = word_next #4

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

    def appearance_of_the_letters_to_the_position(self):
        for letter in self.letters_abc:
            position = 0
            for i in range(30):
                position=i
                count_letter = 0
                for word in self.words:
                    if i<len(word):
                        if word[i].lower()==letter:
                            count_letter+=1

                print('Буква: {}, Позиция: {}, Количесвто {}'.format(letter, position, count_letter))






    def compatibility_letters(self):
        for a in self.letters_ABC:
            for b in self.letters_abc:
                print('Сочетание: {} встречается: {}'.format(a+b, self.text.count(a+b)+self.text.count(b+a)))



