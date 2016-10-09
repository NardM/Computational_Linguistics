import re
from functools import reduce


class Work_2:
    def __init__(self, text):
        self.__text = text
        self.__len_text = len(text)

    def solve_1(self):
        # amount = [0 if x.isalpha() else 1 for x in self.text if x.isalpha() or x.isdigit()]
        # amount_letters, amount_numeral = amount.count(0), amount.count(1)
        amount_letters, amount_numeral = 0, 0
        for symbol in self.__text:
            if symbol.isdigit():
                amount_numeral += 1
            if symbol.isalpha():
                amount_letters += 1

        amount_symbol = len(self.__text) - self.__text.count(' ')

        print(
            'Знаки: {}\nСимволов: {}; Процент: {:.2%}\nБукв: {}; Процент: {:.2%}\nЦифр: {}; Процент: {:.2%}%\n'.format(
                len(self.__text), amount_symbol, amount_symbol / self.__len_text, amount_letters,
                                                 amount_letters / self.__len_text, amount_numeral,
                                                 amount_numeral / self.__len_text))

    def solve_2(self):
        paragraph = self.__text.split('\n')

        def __average_in_list(lst):
            if type(lst[0]) == int:
                return reduce(lambda x, y: x + y, lst) / len(lst)
            else:
                return reduce(lambda x, y: x + y, [x for x in map(len, lst)]) / len(lst)

        def __search_values(text=self.__text):
            len_text = len(text)
            line = [text[(self.__len_text + i) - len_text:i + 79] for i in
                    range(0, self.__len_text, 79)]  # строка - это 79 символов
            offers = text.split('.') + text.split('?') + text.split('!')
            words = [x for x in re.findall(r'[A-z\']+', text)]
            syllable = [x for x in re.findall(r'[aiouy]+e*|e(?!d$|ly).|[td]ed|le$', text)]
            word = [x for x in text if x.isalpha()]

            if text == self.__text:
                return 'Абзацов: {0}\nСтроков: {1}\nПредложений: {2}\nСлов: {3}\nСлогов: {4}\n'.format(len(paragraph),
                                                                                                       len(line),
                                                                                                       len(offers),
                                                                                                       len(words),
                                                                                                       len(syllable))
            else:
                return [line, offers, words, syllable, word]

        def __output(func):
            print('В полном тексте')
            print(__search_values(self.__text))
            print('Среднее число значений в абзаце: ')
            func()

        @__output
        def __iterates_paragraph():
            line, offers, words, syllable, word = [], [], [], [], []
            for paras in paragraph:
                average_list = __search_values(paras)
                line.append(average_list[0])
                offers.append(average_list[1])
                words.append(average_list[2])
                syllable.append(average_list[3])
                word.append(average_list[4])

            print('Строк: {}\nПредложений: {}\nСлов: {}\nСлогов: {}\nБукв: {}\n'.format(
                __average_in_list(line), __average_in_list(offers), __average_in_list(words), __average_in_list(syllable),
                __average_in_list(word)))

    def solve_3(self):
        def __histogram(s=self.__text.lower()):
            d = dict()
            for c in s:
                if c.isalpha():
                    if c not in d:
                        d[c] = 1
                    else:
                        d[c] += 1
            return d

        def __the_frequency_of_letters(func):
            hist = __histogram()
            letters = len([x for x in self.__text if x.isalpha()])
            print('Частота букв в алфавите: ')
            for key in sorted(hist):
                print('{} => {:.2%}'.format(key, hist[key] / letters))
            func()

        @__the_frequency_of_letters
        def the_most_commonly_used_symbols():
            hist = __histogram()
            l = lambda x: x[1]
            print(sorted(hist.items(), key=l, reverse=True))

    def solve_4(self):
        def avarage_in_list(lst):
            return reduce(lambda x, y: x + y, lst) / len(lst)

        number = [1 for x in self.__text if x.isdigit()]
        numbers = [x for x in re.findall(r'[0-9]+', self.__text)]
        digit = [2 if x.count('.') > 0 else 1 for x in self.__text if x.isdigit()]
        print('Среднее число: \nРазрядности: {}\nТип чисел: {}\n'.format(avarage_in_list(numbers),
                                                                                 avarage_in_list(digit)))


text = '''Though it was winter Vadim Petrovich, the agronomist of the farm, had a busy day last Tuesday.
He began his morning with the radio, he listened to the news. At half past seven he got up, washed, did his morning
exercises at an open window, dressed and had breakfast.
Vadim Petrovich likes mornings, because he can see his family, and he can have a talk with his wife and children.
At a quarter to nine Vadim Petrovich left home. It was a cold winter day. There was a lot of snow on the ground.
The sky wasn't blue, and the sun didn't shine at all. There weren't any people in the street.
Vadim Petrovich went to the farm. It is not far from his house, so he walks there. The road was white with snow and he
couldn't walk fast. When he came to the farm, some people wanted to see and talk to him. His working day began.
At 1 o'clock he went home to have dinner. He had dinner with his wife and little daughter who does not go to school.
He ate his dinner, rested a little, and went back to the farm. Vadim Petrovich had to talk to some people,
to write some letters, and to do some other work. At 5 o'clock he had an important meeting.
And only at 8 o'clock he came home.'''
test = Work_2(text)
#test.solve_1()
#test.solve_2()
#test.solve_3()
test.solve_4()
