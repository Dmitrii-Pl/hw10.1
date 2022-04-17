class BasicWord:

    def __init__(self, original_word, sub_words):

        self.original_word = original_word
        self.sub_words = sub_words

    def correct_answer(self, ent_word):
        """ проверку введенного слова в списке допустимых подслов(вернет bool),"""
        if ent_word.lower() in self.sub_words:
            return True
        else:
            return False

    def count_sub_words(self):
        """- подсчет количества подслов(вернет int)."""
        return len(self.sub_words)
