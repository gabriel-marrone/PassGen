import random

class UsernameGenerator:
    def __init__(self, lookup):
        self.lookup = lookup

    def _roll_word(self):
        roll = "".join(str(random.randint(1, 6)) for _ in range(5))
        return self.lookup.get(roll, "Word")

    def _to_leet(self, word):
        table = {
            "a": "4", "e": "3", "i": "1", "o": "0",
            "s": "5", "t": "7", "g": "9"
        }
        return "".join(table.get(c.lower(), c) for c in word)

    def generate(self, words=2, add_number=True, style="random"):
        # Add all styles here
        available_styles = [
            "camel",
            "pascal",
            "lower",
            "kebab",
            "plain",
            "upper",
            "upper_plain",
            "leet",
        ]

        if style == "random":
            style = random.choice(available_styles)

        picked = [self._roll_word() for _ in range(words)]

        # --- STYLE FORMATTING ---
        if style == "camel":
            username = picked[0].lower() + "".join(w.capitalize() for w in picked[1:])

        elif style == "pascal":
            username = "".join(w.capitalize() for w in picked)

        elif style == "lower":
            username = "_".join(w.lower() for w in picked)

        elif style == "kebab":
            username = "-".join(w.lower() for w in picked)

        elif style == "upper":
            username = "_".join(w.upper() for w in picked)

        elif style == "upper_plain":
            username = "".join(w.upper() for w in picked)


        elif style == "leet":
            username = "".join(self._to_leet(w) for w in picked)

        elif style == "plain":
            username = "".join(picked)

        else:
            # Unknown style fallback
            username = "".join(picked)

        if add_number:
            username += str(random.randint(0, 999))

        return username
