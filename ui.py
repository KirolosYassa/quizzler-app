from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 12, "normal")

class QuizClass:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        
        self.window.title("Trivia Quizzer")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score = 0", fg="white", font=SCORE_FONT, bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text="Questions are appeared here.",
            anchor="center",
            font=FONT,
            fill=THEME_COLOR,
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.show_question()

        right_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=right_img, command=self.check_true, borderwidth=0, highlightthickness=0)
        self.false_button = Button(image=false_img, command=self.check_false, borderwidth=0, highlightthickness=0)

        self.true_button.grid(row= 2, column= 0)
        self.false_button.grid(row= 2, column= 1)

        self.window.mainloop()


    def show_question(self):
        # self.true_button.config(state="normal")
        # self.false_button.config(state="normal")

        self.canvas.config(self.canvas, bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(self.canvas, bg="white")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the questions.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self, answer=True):
        self.give_feedback(self.quiz.check_answer(str(answer)))
        

    def check_false(self, answer=False):
        self.give_feedback(is_right=self.quiz.check_answer(str(answer)))
    
    
    def give_feedback(self, is_right):
        # self.true_button.config(state="disabled")
        # self.false_button.config(state="disabled")

        if is_right:
            self.score.config(self.score, text="Score = " + str(self.quiz.score + 1))
            self.canvas.config(self.canvas, bg="green")
        else:
            self.score.config(self.score, text="Score = " + str(self.quiz.score))
            self.canvas.config(self.canvas, bg="red")
        self.window.after(1000, self.show_question)
