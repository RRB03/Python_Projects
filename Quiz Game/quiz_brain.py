class QuizBrain:
    def __init__(self, q_list):
        self.ques_number = 0
        self.ques_list = q_list
        self.score = 0

    def ques_left(self):
        return self.ques_number < len(self.ques_list)

    def next_q(self):
        ques = self.ques_list[self.ques_number]
        self.ques_number += 1
        u_ans = input(f"Q.{self.ques_number}: {ques.text} (True / False)")
        self.check_ans(u_ans,ques.answer)

    def check_ans(self, u_ans, correct_ans):
        if u_ans.lower() == correct_ans.lower():
            print("Your answer is right")
            self.score+=1
        else:
            print("Your answer is wrong")
        print(f"Correct answer is {correct_ans}")
        print(f"Your score is: {self.score}/{self.ques_number}\n")
