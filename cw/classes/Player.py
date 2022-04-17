class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def count_used_words(self):
        """получение количество слов (возвращает int)"""
        return len(self.used_words)

    def add_words(self, word):
        """добавление слова в использованные слова"""
        self.used_words.append(word)

    def check_use(self, word):
        if word.lower() in self.used_words:
            return True
        else:
            return False
        # return word in self.used_words
