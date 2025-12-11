import importlib.resources

class WordlistLoader:
    def __init__(self, filepath=None):
        """ If filepath is = to none, loads the default wordlist found in /src/passgen/wordlists """
        self.filepath = filepath
        self.lookup = {} # maps "12345" -> "apple"

    def load(self):
        """ Loads wordlist into a dictionary """
        if self.filepath:
            self._load_from_path(self.filepath)
        else:
            self._load_default()

        if not self.lookup:
            raise ValueError("Wordlist is empty or invalid")

        return self.lookup

    def _load_from_path(self, path):
        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    code, word = parts
                    self.lookup[code] = word

    def _load_default(self):
        """ Loads the packaged default list: /src/passgen/wordlists """

        with importlib.resources.open_text("passgen.wordlists", "eff_large_wordlist.txt") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    code, word = parts
                    self.lookup[code] = word