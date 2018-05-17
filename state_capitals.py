"""State Captials Game."""
from random import shuffle

state_dict = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver"
}


class StateCapitalsGame():
    """Not even sure waht to put here."""

    def __init__(self, dictionary):
        """So you say you need a comment."""
        self.dict_states = {}
        self.stats = {'Correct': 0, 'Incorrect': 0}
        self.shuffle_states(dictionary)
        self.instructions()
        self.play_game()
        self.play_again()

    def instructions(self):
        """So you say you need a comment."""
        print('Welcome to the State Capitals Game.')
        print('Below you will be asked the capital of a state.')
        print('Please type in the capital and enter.')
        

    def shuffle_states(self, state_dictionary):
        """So you say you need a comment."""
        keys = list(state_dictionary.keys())
        shuffle(keys)
        for key in keys:
            self.dict_states.update({key: state_dictionary[key]})

    def play_game(self):
        """So you say you need a comment."""
        for key, value in self.dict_states.items():
            question = ('What is the capital of {}? ').format(key)
            answer = input(question)
            self.process_answer(answer, value)

    def process_answer(self, input, capital):
        """So you say you need a comment."""
        if(input == capital):
            print('Yay, you are CORRECT!')
            self.stats['Correct'] += 1
            print(("You currenty have {} right and {} wrong.").format(self.stats['Correct'], self.stats['Incorrect']))
        else:
            print('Sorry, you are incorrect.')
            self.stats['Incorrect'] += 1
            print(("You currenty have {} right and {} wrong.").format(self.stats['Correct'], self.stats['Incorrect']))

    def play_again(self):
        """So you say you need a comment."""
        play_again = input("Would you like to play again? Type y for yes and n for no. ")
        if (play_again == 'y'):
            StateCapitalsGame(state_dict)
        else:
            print(("Thanks for playing. You got {} right and {} wrong.").format(self.stats['Correct'], self.stats['Incorrect']))


    def __str__(self):
        """So you say you need a comment."""
        return ("You got {} right and {} wrong.").format(self.stats['Correct'], self.stats['Incorrect'])


game1 = StateCapitalsGame(state_dict)
