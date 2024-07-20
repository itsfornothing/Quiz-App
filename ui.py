from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg="#375362", padx=20, pady=20)

        self.score = Label(text=f"score: 0", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some Question texts",
                                                     fill="#375362",
                                                     width=280,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, bd=0,command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_button_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, bd=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of question.")

    def true_pressed(self):
        if self.quiz.still_has_questions():
            self.give_feed_back(self.quiz.check_answer("true"))
            self.score.config(text=f"score: {self.quiz.score}")

    def false_pressed(self):
        if self.quiz.still_has_questions():
            self.give_feed_back(self.quiz.check_answer("false"))
            self.score.config(text=f"score: {self.quiz.score}")

    def give_feed_back(self,user_answer):
        if user_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)