from basicText import basicText
from functools import reduce
import re


def average_in_list(lst):
    """Нахождения среднее значения"""
    if type(lst[0]) == int:
        return reduce(lambda x, y: x + y, lst) / len(lst)
    else:
        return reduce(lambda x, y: x + y, [x for x in map(len, lst)]) / len(lst)


def search_words(text):
    return [x for x in re.findall(r'[A-z\']+', text)]


class taskTwo(basicText):
    def __init__(self, text):
        super().__init__(text)
        self.amount_symbol = len(self.text) - self.text.count(' ')
        self.len_text = len(text)

    def solve_1(self):
        # amount = [0 if x.isalpha() else 1 for x in self.text if x.isalpha() or x.isdigit()]
        # amount_letters, amount_numeral = amount.count(0), amount.count(1)
        '''Вариант сверху красивый, но не оптимальный, т.к при очень большем тексте
        программа будет работать дольше, чам вариант ниже'''
        amount_letters, amount_numeral = 0, 0
        for symbol in self.text:
            if symbol.isdigit():
                amount_numeral += 1
            if symbol.isalpha():
                amount_letters += 1
        print(
            'Знаки: {}\nСимволов: {}; Процент: {:.2%}\nБукв: {}; Процент: {:.2%}\nЦифр: {}; Процент: {:.2%}%\n'.format(
                len(self.text), self.amount_symbol, self.amount_symbol / self.len_text, amount_letters,
                                                    amount_letters / self.len_text, amount_numeral,
                                                    amount_numeral / self.len_text))

    def solve_2(self):
        paragraph = self.text.split('\n')

        def __search_values(text=self.text):
            """Нахождения значений в тексте"""
            len_text = len(text)
            line = [text[(self.len_text + i) - len_text:i + 79] for i in
                    range(0, self.len_text, 79)]  # строка - это 79 символов
            offers = text.split('.') if '.' in text else '' + text.split('?') if '?' in text else '' + text.split(
                '!') if '!' in text else ''
            words = search_words(text)
            syllable = [x for x in re.findall(r'[aiouy]+e*|e(?!d$|ly).|[td]ed|le$', text)]
            word = [x for x in text if x.isalpha()]

            if text == self.text:
                return 'Абзацов: {0}\nСтроков: {1}\nПредложений: {2}\nСлов: {3}\nСлогов: {4}\n'.format(len(paragraph),
                                                                                                       len(line),
                                                                                                       len(offers),
                                                                                                       len(words),
                                                                                                       len(syllable))
            else:
                return [line, offers, words, syllable, word]

        def __output(func):
            """Вывод на консоль"""
            print('В полном тексте')
            print(__search_values(self.text))
            print('Среднее число значений в абзаце: ')
            func()

        @__output
        def __iterates_paragraph():
            """Поиск среднего значения в абзаце"""
            line, offers, words, syllable, word = [], [], [], [], []
            for paras in paragraph:
                average_list = __search_values(paras)
                line.append(average_list[0])
                offers.append(average_list[1])
                words.append(average_list[2])
                syllable.append(average_list[3])
                word.append(average_list[4])

            print('Строк: {}\nПредложений: {:.3}\nСлов: {:.3}\nСлогов: {:.3}\nБукв: {:.3}\n'.format(
                average_in_list(line), average_in_list(offers), average_in_list(words),
                average_in_list(syllable),
                average_in_list(word)))

    def solve_3(self):
        def __histogram(s=self.text.lower()):
            """Добавление текст в словарь из букв"""
            d = dict()
            for c in s:
                if c.isalpha():
                    if c not in d:
                        d[c] = 1
                    else:
                        d[c] += 1
            return d

        def __output(func):
            print('------Задания 3------\n')
            print('Частота букв в алфавите: ')
            __the_frequency_of_letters()
            print('Наиболее используемые и не используемые символы алфавита: \n')
            func()

        def __the_frequency_of_letters():
            """Частота букв в алфавите"""
            hist = __histogram()
            letters = len([x for x in self.text if x.isalpha()])
            for key in sorted(hist):
                print('{} => {:.2%}'.format(key, hist[key] / letters))
            print('\n')

        @__output
        def the_most_commonly_used_symbols():
            """Сортировка словаря"""
            hist = __histogram()
            sorted_values = sorted(hist.items(), key=lambda x: x[1], reverse=True)
            for i in sorted_values:
                print('{} => {}'.format(i[0], i[1]))
            print('\n')

    def solve_4(self):
        numbers = [x for x in re.findall(r'[0-9]+', self.text)]
        number = [1 for x in self.text if x.isdigit()]
        float_numbers = [x for x in re.findall(r'[-+]?\d+\..?\d*', self.text)]
        digit = average_in_list([len(x) for x in numbers])

        print(
            'Число появление чисел, цифр: {}, {}\nЧастота чисел и цифр: {:.2%}, {:.2%}\nСреднее число: \n'
            '   Разрядности: {}\nТип чисел: \n   Вещественные: {}\n   Целые: {}\n'.format(
                len(numbers) + len(float_numbers), len(number),
                (len(numbers) + len(float_numbers)) / self.amount_symbol,
                len(number) / self.amount_symbol, int(digit), len(float_numbers), len(numbers) - len(float_numbers)))
