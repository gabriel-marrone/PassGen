class WordlistLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.lookup = {} # maps "12345" -> "apple"

    def load(self):
        """ Loads wordlist into a dictionary """
        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    code, word = parts
                    self.lookup[code] = word

        if not self.lookup:
            raise ValueError("Wordlist is empty or invalid")

        return self.lookup