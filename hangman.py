import random

class Word():
    def __init__(self,word):
        self.word = word
        self.word_info = []
        self.wrong_answers = 8
        self.guessed_letters = []
        for letter in word:
            letter_info = {}
            letter_info['letter'] = letter
            letter_info['guessed'] = False
            self.word_info.append(letter_info)

    def check_letter(self, letter):
        # update to allow for upper and lowercase guesses
        self.guessed_letters.append(letter)
        # add something if they repeat a letter
        if letter in self.word:
            # return 'yes!'
            for i in self.word_info:
                if letter == i['letter']:
                    i['guessed'] = True    
        else:
            self.wrong_answers -= 1
            # return 'Sorry, that\'s not in the word!'

    def print_word(self):
        for i in self.word_info:
            if i['guessed'] == True:
                print(i['letter'], end=' ')
            else:
                print('_', end=' ')
        print()

class Game():
    def __init__(self):
        self.current_word = None
        self.user_input = None
        self.game_over = False
        # if I were making this a 'real' game I'd do an api call for random words instead
        # stretch goal: words with spaces and non-letter characters (-, ', etc)
        self.word_bank = ['swing','liver','diamond','cower','dynamic','combination','tasty','conductor']
    
    def get_word(self):
        self.word_index = random.randint(0,len(self.word_bank)-1)
        self.current_word = self.word_bank[self.word_index]
        self.game_word = Word(self.current_word)

    def start_game(self):
        print('Welcome to Hangman! Press any key to start')
        self.user_input = input()
        self.get_word()
        self.game_word.print_word()
        self.game_play()

    def game_play(self):
        if self.game_over == False:
            print('Guess a letter', end=': ')
            self.user_input = input()
            self.game_word.check_letter(self.user_input)
            self.game_word.print_word()
            print('You have guessed', self.game_word.guessed_letters)
            print('You have', self.game_word.wrong_answers, 'wrong answers remaining')
            self.game_end()
            self.game_play()
        
    def game_end(self):
        # loss conditions
        if self.game_word.wrong_answers == 0:
            self.game_over = True
            print('Game Over! The word was', self.game_word.word)
        else :
            for i in self.game_word.word_info:
                if i['guessed'] == True:
                    next()
                else:
                    return

                    # self.game_over = True
                    # print('Congratulations! You win!')

                # if all(i['guessed']==True):
                #     self.game_over = True
                #     print('Congratulations! You win!')

        # win conditions
        # need to check that ['guessed'] on each letter is True/not False
        # what's the forEach function in python? lol

        # ability to restart



# test = Word('cabbage')
# print(test.word_info)
# print(test.check_letter('a'))
# print(test.check_letter('d'))
# test.print_word()
# print('wrong guesses remaining: ', test.wrong_answers)
# print('Letters guessed: ', set(test.guessed_letters))

test_game = Game()

test_game.start_game()
# print(test_game.current_word)
# print(test_game.game_word.word_info)

# print('Type something', end=": ")
