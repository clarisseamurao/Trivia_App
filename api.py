from flask import Flask, jsonify
from trivia import TriviaQuestion, TriviaManager

app = Flask(__name__)

manager = TriviaManager()

# Seed some trivia questions
manager.add_question(TriviaQuestion(
    "What is the capital of France?",
    "Paris",
    ["Paris", "Berlin", "Rome", "Madrid"],
))
manager.add_question(TriviaQuestion(
    "Who painted the Mona Lisa?",
    "Leonardo da Vinci",
    ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
))
manager.add_question(TriviaQuestion(
    "Which planet is known as the Red Planet?",
    "Mars",
    ["Venus", "Jupiter", "Mars", "Saturn"],
))
manager.add_question(TriviaQuestion(
    "In which year did the first human land on the Moon?",
    "1969",
    ["1965", "1969", "1972", "1959"],
))
manager.add_question(TriviaQuestion(
    "What is the chemical symbol for Gold?",
    "Au",
    ["Ag", "Au", "Gd", "Go"],
))
manager.add_question(TriviaQuestion(
    "Which language is used to style web pages?",
    "CSS",
    ["HTML", "CSS", "Python", "SQL"],
))
manager.add_question(TriviaQuestion(
    "Who wrote the novel 1984?",
    "George Orwell",
    ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.R.R. Tolkien"],
))
manager.add_question(TriviaQuestion(
    "What is the largest ocean on Earth?",
    "Pacific Ocean",
    ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
))


@app.get("/trivia")
def get_trivia():
    q = manager.get_random_question()
    return jsonify(q.to_dict())


if __name__ == "__main__":
    app.run(port=5000)
