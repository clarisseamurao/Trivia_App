import random


class TriviaQuestion:
    def __init__(self, question, answer, choices=None):
        self.question = question
        self.answer = answer
        self.choices = choices or []

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "choices": self.choices,
        }

    def __str__(self):
        output = f"Q: {self.question}"
        if self.choices:
            options = "\n".join([f"- {c}" for c in self.choices])
            output += f"\n{options}"
        output += f"\nA: {self.answer}"
        return output


class TriviaManager:
    def __init__(self):
        self.questions = []

    def add_question(self, question: "TriviaQuestion"):
        self.questions.append(question)

    def get_random_question(self) -> "TriviaQuestion":
        return random.choice(self.questions)
