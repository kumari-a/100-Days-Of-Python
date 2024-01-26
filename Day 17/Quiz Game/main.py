from data import question_data
import random


class Game:
    def __init__(self):
        self.score=0
        self.question=set()
        for _ in range(5):
            self.choose_question()
        print(f"Thank you for playing. Your final score is {self.score}.")

    def choose_question(self):
        question_ = random.choice(question_data)
        que = question_["text"]
        while que in self.question:
            question_ = random.choice(question_data)
            que = question_["text"]
        ans=question_["answer"]
        self.question.add(que)
        answer= input(f"{que} true/false : ").lower()
        if ans==answer:
            self.score+=1
            print(f"Your answer is correct. Your score is {self.score}.")
        else:
            print(f"Your answer is wrong, Your score is {self.score}.")


play = Game()



