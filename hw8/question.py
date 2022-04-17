class Question:

    def __init__(self, text, diff, correct_answer):
        self.text = text
        self.diff = diff
        self.correct_answer = correct_answer

        self.is_asked = False
        self.user_answer = None
        self.points = 0

        self.max_diff = 5

    def __repr__(self):
        return f"Вопрос сложность {self.diff}/{self.max_diff} {self.text} {self.correct_answer}"

    def get_points(self):
        return self.diff * 10

    def is_correct(self):
        if self.correct_answer == self.user_answer:
            return True
        return False

    def build_question(self):
        return f"Вопрос: {self.text}\nСложность {self.diff}/{self.max_diff}"

    def build_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.get_points()} баллов\n"
        return f"Ответ неверный, верный ответ {self.correct_answer}\n"
