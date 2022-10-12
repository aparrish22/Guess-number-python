''' goal, implement GUI and Data Visualization '''

from random import Random
from settings import Settings

class GuessNumber:
    ''' Simple abstract class of guessing a number '''
    
    def __init__(self):
        
        self.settings = Settings()
        
        self.target_number = 0
        self.guesses = 0
        self.found = False
        self.max_num = self.settings.easy_mode() # default
        
        
    def choose_difficulty(self):
        error = False
        
        while not error:
            try:
                difficulty = input('Type one of the following to choose a difficulty'
                            'level!:\n'
                            '\'easy\'\n'
                            '\'medium\'\n'
                            '\'hard\'\n'
                            '\'custom\'\n')
                error = True # won't be reached until difficulty is valid
            except ValueError:
                print(f'{difficulty} is not a valid choice.')
        
        match difficulty:
            case 'easy':
                self.max_num = self.settings.easy_mode()
            case 'medium':
                self.max_num = self.settings.medium_mode()
            case 'hard':
                self.max_num = self.settings.hard_mode()
            case 'custom':
                try:
                    maximum = int(input('Input a max number range: '))
                    self.max_num = self.settings.custom_mode(maximum)
                except ValueError:
                    print('Please type an interger number')
            case _:
                print('Invalid input.')
                
        
    def run_guess_number(num):
        pass
    
    def record_data(self,guesses):
        ''' Record data in json to later visualize the input data '''
        pass

class GuessNumberUser(GuessNumber):
    ''' Purely guessing the number as a user. '''

    def __init__(self):
        super().__init__()
        
        self.choose_difficulty()
        
        # Setting an easy setting for the user to guess the number
        # can implement settings into this
        self.target_number = Random.randint(self=Random(),a=1,b=self.max_num)
        
    def choose_difficulty(self):
        return super().choose_difficulty()
        
    def run_guess_number(self):
        print('Welcome to Guessing the Number App!')
        print(f'The range is from 1 to {self.max_num}!: ')
        
        target = int(self.target_number)
        
        
        
        # print(f"(Debug: This is target num: {target})")
        # while it's not found, go find it. 
        # when it IS found, break.
        while not self.found:
            try:
                guess = int(input('Enter your guess: '))
                if guess == target:
                    print('success')
                    self.found = True
                elif guess < target:
                    print('too low')
                elif guess > target:
                    print('too high')
            except ValueError:
                print("Your guess is not a valid number!")


            
            

class GuessNumberComputer(GuessNumber):
    ''' Guessing the number with a computer, after giving user input '''
    
    def __init__(self):
        super().__init__()
        
        self.choose_difficulty()
        
        # Setting an easy setting for the computer to guess the number
        # can implement settings into this
        self.end = self.max_num
        self.target_number = Random.randint(self=Random(),a=1,b=self.end)

    def choose_difficulty(self):
        return super().choose_difficulty()

    def run_guess_number(self):
        print('Alrighty computer. Welcome to Guessing the Number App!')
        print(f'The range is from 1 to {self.max_num}!: ')
        
        target = int(self.target_number)
         
        print(f"(Note for us - this is target num: {target})")
        # while it's not found, go find it. 
        # when it IS found, break.
        while not self.found:
            guess = self._binary_search_guess(target)
            if guess == target:
                print(f'The computer found the number! It was {target}!')
                self.found = True
            else:
                print("The computer failed! :(.")
            ''' returns int number guess '''

    def _binary_search_guess(self, target):
        start = 1
        end = self.end
        mid = end // 2
        found = self.found

        while not found:
            if mid == target:
                return mid
            elif mid < target:
                print('Too low!')
                start = mid
                mid = round((start + end) / 2)
            elif mid > target:
                end = mid
                mid = round(end / 2)
                print('Too high!')
        
        return 0

if __name__ == '__main__':
    # gnu = GuessNumberUser()
    # gnu.run_guess_number()
    gnc = GuessNumberComputer()
    gnc.run_guess_number()