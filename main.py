from question_model import Question
#from data import question_data
from quiz_brain import QuizBrain
from travia import question_data

bank_question = []

for question in question_data["results"]:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    bank_question.append(new_question)

quiz = QuizBrain(bank_question)
while quiz.still_has_question():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

