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
        # need to print the underscores vs the letters, depending on what has been guessed
        pass

class Game():
    def __init__(self):
        self.wrong_answers = 8
        self.guessed_letters = {}
        self.current_word = None
    
    def start_game(self):
        self.wrong_answers = 8
        self.guessed_letters = []
        self.current_word = None

    def get_word(self):
        # something here to set the current word
        pass

    def game_end(self):
        # win conditions
        # loss conditions
        # ability to restart
        pass

test = Word('cabbage')
print(test.word_info)
print(test.check_letter('a'))
print(test.word_info)
print(test.check_letter('d'))