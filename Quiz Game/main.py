from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(0,len(question_data)):
    question = Question(question_data[i]["text"],question_data[i]["answer"])
    question_bank.append(question)

start_quiz = QuizBrain(question_bank)
while start_quiz.ques_left():
    start_quiz.next_q()
print(f"Quiz got completed.\n"
      f"Your final score is {start_quiz.score}/{start_quiz.ques_number}")