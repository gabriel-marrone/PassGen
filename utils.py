import secrets

def roll_die():
    """ Simulates a dice roll using secrets for cryptographed randomness """
    return secrets.randbelow(6) + 1

def roll_die_digit():
    """ Rolls roll_die 4 times and uses the last roll """
    result = None
    for _ in range(4):
        result = roll_die()
    return result

def make_camel_case(words):
    """ Converts list of words to camel case """
    return "".join(word.capitalize() for word in words)