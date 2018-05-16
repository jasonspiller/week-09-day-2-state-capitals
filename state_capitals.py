"""State Captials Game."""

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
        self.dictionary = dictionary

    def __str__(self):
        """So you say you need a comment."""
        return ("Our dict is {} long.").format(len(self.dictionary))


game1 = StateCapitalsGame(state_dict)

print(game1)
