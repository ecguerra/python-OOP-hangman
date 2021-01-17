import random

class Word():
    def __init__(self,word):
        self.word = word
        self.word_info = []
        for letter in word:
            letter_info = {}
            letter_info['letter'] = letter
            letter_info['guessed'] = False
            self.word_info.append(letter_info)

    def check_letter(self, letter):
        if letter in self.word:
            # return 'yes!'
            for i in self.word_info:
                # print(i['letter'])
                if letter == i['letter']:
                    # print('Yes!', i['letter'])
                    i['guessed'] = True
        else:
            return 'no!'

    def print_word(self):
        for i in self.word_info:
            if i['guessed'] == True:
                print(i['letter'])
            else:
                print('_')

class Game():
    def __init__(self):
        self.wrong_answers = 8
        self.guessed_letters = {}
        self.current_word = None
        # if I were making this a 'real' game I'd do an api call for random words instead
        self.word_bank = ['swing','liver','diamond','cower','dynamic','combination','tasty','conductor']
    
    def get_word(self):
        self.word_index = random.randint(0,len(self.word_bank))
        self.current_word = self.word_bank[self.word_index]
        self.game_word = Word(self.current_word)

    def start_game(self):
        self.wrong_answers = 8
        self.guessed_letters = {}
        self.get_word()
        self.game_word.print_word()

    def game_end(self):
        # win conditions
        # loss conditions
        # ability to restart
        pass

# test = Word('cabbage')
# print(test.word_info)
# print(test.check_letter('a'))
# print(test.check_letter('d'))
# test.print_word()

test_game = Game()

test_game.start_game()
# print(test_game.current_word)
# print(test_game.game_word.word_info)
