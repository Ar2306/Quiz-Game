from question_model import Quesiton
from data import question_data
from quiz_brain import Quiz_brain

question_bank=[]
for i in question_data:
    question_text=i["text"]
    question_answer=i["answer"]
    new_question=Quesiton(question_text,question_answer)
    question_bank.append(new_question)


quiz=Quiz_brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("you've completed the quiz")
print(f"your final score is :{quiz.score}/{quiz.question_number}")    