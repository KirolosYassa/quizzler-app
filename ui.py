from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 12, "normal")

class QuizClass:

    def __init__(self):
        self.window = Tk()
        self.window.title("Trivia Quizzer")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score = 0", fg="white", font=SCORE_FONT, bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(150, 125, text="dalfk alfklfads fk", width=250, font=FONT, fill=THEME_COLOR, anchor="center")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        right_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        true_button = Button(image=right_img, command=self.check_true, borderwidth=0, highlightthickness=0)
        false_button = Button(image=false_img, command=self.check_true, borderwidth=0, highlightthickness=0)

        true_button.grid(row= 2, column= 0)
        false_button.grid(row= 2, column= 1)

        self.window.mainloop()


    def check_true(self):
        pass