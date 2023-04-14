from tkinter import *
from settings import BACKGROUND_COLOR, FG_COLOR, FONT, SIZE_TEXT, TRUE_BUTTON_IMAGE, FALSE_BUTTON_IMAGE, \
    RED_COLOR, GREEN_COLOR
from question_bank import Questions


class QuizzWindow(Tk, Questions):

    def __init__(self, data_list_questions: list):
        super().__init__()

        """Initializes the window inheriting from the tkinter.Tk() class 
        and the function from the Questions class."""

        # Values
        self.list_questions = data_list_questions
        self.total_questions = len(self.list_questions)
        self.total_questions_answered = 0
        self.question, self.answer = self.next_question(self.list_questions)

        # config
        self.config(background=BACKGROUND_COLOR, pady=20, padx=20)
        self.title("Quizzlet")
        self.resizable(False, False)

        # score
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", background=BACKGROUND_COLOR,
                                 fg=FG_COLOR, font=(FONT, SIZE_TEXT, "normal"), padx=40, pady=40)
        self.score_label.grid(row=0, column=1)

        # rectangle card
        self.canvas = Canvas(width=350, height=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.text = self.canvas.create_text(160, 150, text=f"{self.question}", width=250, font=(FONT, 25, "italic"),
                                            fill=BACKGROUND_COLOR)

        # right button & wrong button
        self.right_image_button = PhotoImage(file=TRUE_BUTTON_IMAGE)
        self.wrong_image_button = PhotoImage(file=FALSE_BUTTON_IMAGE)
        self.right_button = Button(image=self.right_image_button, background=BACKGROUND_COLOR, highlightthickness=0,
                                   highlightbackground=BACKGROUND_COLOR, command=self.right_button_pressed)
        self.right_button.grid(row=2, column=0, pady=40, padx=40)

        self.wrong_button = Button(image=self.wrong_image_button, background=BACKGROUND_COLOR, highlightthickness=0,
                                   highlightbackground=BACKGROUND_COLOR, command=self.wrong_button_pressed)
        self.wrong_button.grid(row=2, column=1, pady=40, padx=40)
        self.mainloop()

    def __str__(self):
        return "Quizzler Window Program."

    def add_score(self):
        """If user gets right the answer, add a point to the score."""
        self.score += 1

    def right_button_pressed(self):
        """Command for the right button."""
        if self.total_questions_answered == self.total_questions:
            self.stop_quizzler()
        else:
            if self.answer == "True":
                self.add_score()
                self.green_canvas()
            else:
                self.red_canvas()
            self.score_label.config(text=f"Score: {self.score}")
            self.total_questions_answered += 1
            self.after(1000, self.change_question)

    def wrong_button_pressed(self):
        """Command for the wrong button."""
        if self.total_questions_answered == self.total_questions:
            self.stop_quizzler()
        else:
            if self.answer == "False":
                self.add_score()
                self.green_canvas()
            else:
                self.red_canvas()
            self.score_label.config(text=f"Score: {self.score}")
            self.total_questions_answered += 1
            self.after(1000, self.change_question)

    def results(self):
        """Gives the user the final results."""
        self.canvas.itemconfig(self.text, text=f"Final Score: {self.score}")
        self.score_label.config(fg=BACKGROUND_COLOR)
        self.right_button.config(state=DISABLED)
        self.wrong_button.config(state=DISABLED)

    def change_question(self):
        """Retrieves the next question."""
        self.remove_question()
        self.canvas.config(bg="white")
        self.question, self.answer = self.next_question(self.list_questions)
        self.canvas.itemconfig(self.text, text=f"{self.question}")

    def stop_quizzler(self):
        """Once the user completes all the questions, stop."""
        self.right_button.config(state=DISABLED)
        self.wrong_button.config(state=DISABLED)
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.text, text=f"Result: {self.score}/{self.total_questions}")

    def green_canvas(self):
        """Changes the canvas color to green."""
        self.canvas.config(bg=GREEN_COLOR)

    def red_canvas(self):
        """Changes the canvas color to red."""
        self.canvas.config(bg=RED_COLOR)

    def remove_question(self):
        """Deletes from the list the index that contains the same value for the question key."""
        try:
            for i in range(len(self.list_questions)):
                if self.list_questions[i]["question"] == self.question:
                    del self.list_questions[i]
        except IndexError:
            pass

