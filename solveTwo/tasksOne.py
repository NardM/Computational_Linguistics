from basicText import basicText
from solveTwo import tasksTwo


class taskOne(basicText):
    def __init__(self, text, len_text):
        #basicText.__init__(text,len_text)
        basicText.__init__(text, len_text)
        self.amount_symbol = self.solve_1()[0]
        self.amount_numeral = self.solve_1()[1]


    def __str__(self):
        return 'Person %s, %s' % (self.amount_numeral,self.amount_symbol)

    def solve_1(self):
        # amount = [0 if x.isalpha()_t else 1 for x in self.text if x.isalpha() or x.isdigit()]
        # amount_letters, amount_numeral = amount.count(0), amount.count(1)
        amount_letters, amount_numeral = 0, 0
        for symbol in self.text:
            if symbol.isdigit():
                amount_numeral += 1
            if symbol.isalpha():
                amount_letters += 1

        amount_symbol = len(self.text) - self.text.count(' ')

        return amount_symbol,amount_numeral