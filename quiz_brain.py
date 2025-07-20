class QuizBrain:

    def __init__(self, quiz_list):
        self.question_number = 0
        self.question_list = quiz_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You have completed the quiz.")
            print(f"Your final score was: {self.score}/{self.question_number}.")
            return False

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower() :
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")


    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_answer, question.answer)


