import json

from question import Question


def load_questions():
    questions = []
    with open("quest.json", "r", encoding="utf-8") as file:
        questions_raw = json.load(file)
    for question_raw in questions_raw:
        q = question_raw.get("q")
        d = int(question_raw.get("d"))
        a = question_raw.get("a")
        new_question = Question(q, d, a)
        questions.append(new_question)

    return questions


def build_stats(questions):
    correct_answer_count = 0
    questions_points = 0
    for question in questions:
        if question.is_correct():
            correct_answer_count += 1
            questions_points += question.points

    print("Вот и всё!")
    print(f"Отвечено {correct_answer_count} вопроса из {len(questions)}")
    print(f"Набрано баллов: {questions_points}")
