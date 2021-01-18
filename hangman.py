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
        if letter.lower() in self.guessed_letters:
            print('You already guessed that letter! Try again')
            return
        self.guessed_letters.append(letter.lower())
        if letter.lower() in self.word:
            for i in self.word_info:
                if letter.lower() == i['letter']:
                    i['guessed'] = True    
        else:
            self.wrong_answers -= 1
            print('Sorry, that\'s not in the word!')

    def print_word(self):
        for i in self.word_info:
            if i['guessed'] == True:
                print(i['letter'], end=' ')
            else:
                print('_', end=' ')
        print()
    
    def check_word(self):
        for i in self.word_info:
            if not i['guessed']:
                return False
        return True


class Game():
    def __init__(self):
        self.current_word = None
        self.user_input = None
        self.game_over = False
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
        if self.game_word.wrong_answers == 0:
            self.game_over = True
            print('Game Over! The word was', self.game_word.word)
        else :
            if self.game_word.check_word():
                self.game_over = True
                print('You win!')
            else: 
                return


# Stretch Goals:
    # ability to restart
    # stretch goal: words with spaces and non-letter characters (-, ', etc)
    # if making front-end piece: random words API
    

new_game = Game()
new_game.start_game()

