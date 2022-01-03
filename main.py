# From file import Class
import data
from data import choose_category, table
from question_model import Question
from quiz_brain import QuizBrain

print(f"{table} \n")
category = int(input("Which Category do you like to start with?: "))


question_bank = []
for question in choose_category[category]:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


print(f"Category {choose_category[category][0]['category']}")
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print(f"""No more questions left.. 
You have completed the quiz!!
Your final score was: {quiz.score}/{quiz.question_number}""")

