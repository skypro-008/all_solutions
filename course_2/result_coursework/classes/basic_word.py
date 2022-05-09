class BasicWord:
    """Этот класс содержит в себе все необходимое для работы со словом."""

    def __init__(self, initial_word, word_species):
        self.initial_word = initial_word
        self.word_species = word_species

    def check_word(self, ent_word):
        if ent_word in self.word_species:
            return True
        return False

    def count_species(self):
        return len(self.word_species)

