from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q_data in question_data :
    question_bank.append(Question(q_data['question'],q_data['correct_answer']))


quiz = QuizBrain(question_bank)

final_statement = ''
while quiz.still_has_questions():
    final_statement = quiz.next_question()



print('You have completed the quiz')
print(f"Your final Score is {quiz.score}/{quiz.question_number}")
