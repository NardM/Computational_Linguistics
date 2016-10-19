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


def search_letters(text):
    return [x for x in text if x.isalpha()]


def search_number(text):
    return [1 for x in text if x.isdigit()]


class taskTwo(basicText):
    def __init__(self, text):
        super().__init__(text)
        self.amount_symbol = len(self.text) - self.text.count(' ')
        self.len_text = len(text)

    def solve_1(self):
        amount_letters, amount_numeral = len(search_letters(self.text)), len(search_number(self.text))
        print('------Задания 1------\n')
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
            word = search_letters(text)

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
            print('------Задания 2------\n')
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
        # def __histogram(s=self.text.lower()):
        def __histogram(s=search_words(self.text.lower())):
            """Добавление текст в словарь из букв"""
            d = dict()
            for c in s:
                if c.isalpha():
                    if c not in d:
                        d[c] = 1
                    else:
                        d[c] += 1
            return d

        def __the_frequency_of_letters():
            """Частота букв в алфавите"""
            hist = __histogram()
            letters = len(search_letters(self.text))
            return_list = []
            for key in sorted(hist):
                return_list.append('{} => {:.2%}'.format(key, hist[key] / letters))
            return return_list

        def the_most_commonly_used_symbols():
            """Сортировка словаря"""
            hist = __histogram()
            sorted_values = sorted(hist.items(), key=lambda x: x[1], reverse=True)
            return_list = []
            for i in sorted_values:
                return_list.append('{} => {}'.format(i[0], i[1]))
            return return_list

        print('------Задания 3------\n')
        print('Частота букв в алфавите: ')
        print('\n'.join(__the_frequency_of_letters()))
        print('Наиболее используемые и не используемые символы алфавита: \n')
        print('\n'.join(the_most_commonly_used_symbols()))

    def solve_4(self):
        numbers = [x for x in re.findall(r'[0-9]+', self.text)]
        number = search_number(self.text)
        float_numbers = [x for x in re.findall(r'[-+]?\d+\..?\d*', self.text)]
        digit = average_in_list([len(x) for x in numbers])

        print('------Задания 4------\n')
        print(
            'Число появление чисел, цифр: {}, {}\nЧастота чисел и цифр: {:.2%}, {:.2%}\nСреднее число: \n'
            '   Разрядности: {}\nТип чисел: \n   Вещественные: {}\n   Целые: {}\n'.format(
                len(numbers) + len(float_numbers), len(number),
                (len(numbers) + len(float_numbers)) / self.amount_symbol,
                len(number) / self.amount_symbol, int(digit), len(float_numbers), len(numbers) - len(float_numbers)))
