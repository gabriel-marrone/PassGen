import math
from .utils import roll_die_digit, make_camel_case

class DicewareGenerator:
    def __init__(self, lookup):
        self.lookup = lookup
        self.wordlist_size = len(lookup)
        self.entropy_per_word = math.log2(self.wordlist_size)

    def _roll_code(self):
        """ Generates a 5-digit code using the dice roll logic implemented in roll_die_digit """
        digits = [str(roll_die_digit()) for _ in range(5)]
        return "".join(digits)

    def generate_password(self, num_words=4):
        chosen_words = []

        for _ in range(num_words):
            while True:
                code = self._roll_code()
                if code in self.lookup:
                    chosen_words.append(self.lookup[code])
                    break
        
        password = make_camel_case(chosen_words)
        entropy = num_words * self.entropy_per_word
        return password, entropy