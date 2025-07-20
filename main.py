from question_model import Question
from data import question_data, trivia_data
from quiz_brain import QuizBrain


question_bank = []

for item in trivia_data['results']:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
