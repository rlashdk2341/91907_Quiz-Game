from tkinter import *
from functools import partial


class Start:
    def __init__(self):
        background = "#D3D3D3"

        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg=background)
        self.start_frame.grid()

        # Books and Author Quiz Heading row 0
        self.books_label = Label(self.start_frame, text="Books and Author Quiz",
                                   font="Helvetica 26 bold", bg=background)
        self.books_label.grid(row=0)

        # Instructions for the game row 1
        self.instruction_label = Label(self.start_frame, text="How well do you know about authors and its books? \n\n"
                                                          "You'll be presented with authors from a list of 212.\n"
                                                          "You'll need to match the authors with their "
                                                          "books. \n\n "
                                                          "Please press Play button to play the game.",
                                   font="Arial 10", bg=background)
        self.instruction_label.grid(row=1)

        # to_game button frame row 2
        self.to_game_frame = Frame(self.start_frame, bg=background)
        self.to_game_frame.grid(row=2)

        # Button Font
        button_font = ("Arial 15 bold")

        self.play_button = Button(self.to_game_frame, text="Play", font=button_font, bg="#99CCFF",
                                  command=self.to_play, height=2, width=13, borderwidth=2)
        self.play_button.grid(row=0, column=1, padx=10, pady=5)

        # Help Button row 3
        self.help_button = Button(self.start_frame, text="Help", font="Helvetica 10 bold", height=2, width=10,
                                  borderwidth=3, command=self.help)
        self.help_button.grid(row=3, pady=5)

    def to_play (self):
        print("you chose play button")
        Game()



    def help(self):
        print("you chose help button")
        get_help = Help(self)
        get_help.help_text.configure(text="This quiz is about testing your knowledge for the \n"
                                          "naming famous books and authors. \n\n"
                                          "The name of the book will be given, \n"
                                          "and you will have to answer the corresponding author. \n\n"
                                          "This Quiz is a multiple choice quiz. \n\n"
                                          "I wish you best of luck and hope you enjoy this game.")

class Game:
    def __init__(self):

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Capital Label row 0
        self.books_label = Label(self.game_frame, text="Books",
                                   font="Helvetica 15 bold")
        self.books_label.grid(row=0)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box)
        self.top_answers_frame.grid(row=2)

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text="Top left",
                                             font="Helvetica 10 bold", padx=5, pady=5,
                                             command=lambda: self.reveal_answer(0))
        self.top_left_answer_button.grid(column=0, row=0)

        self.top_right_answer_button = Button(self.top_answers_frame, text="Top right",
                                              font="Helvetica 10 bold", padx=5, pady=5,
                                              command=lambda: self.reveal_answer(1))
        self.top_right_answer_button.grid(column=1, row=0)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text="Bottom left",
                                                font="Helvetica 10 bold", padx=5, pady=5,
                                                command=lambda: self.reveal_answer(2))
        self.bottom_left_answer_button.grid(column=0, row=1)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text="Bottom right",
                                                 font="Helvetica 10 bold", padx=5, pady=5,
                                                 command=lambda: self.reveal_answer(3))
        self.bottom_right_answer_button.grid(column=1, row=1)

    def reveal_answer(self, location):
        # TL = 0 TR =1 BL = 2 BR = 3
        print(location)

    def question_maker(self):
        print("hello world")

class Help:
    def __init__(self, partner):
        background = "#FFF4C3"

        # disable help button
        partner.help_button.config(state=DISABLED)

        self.help_box = Toplevel()
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Information",
                                 font=("Helvetica", "21", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",font="Arial",
                                width=45, bg=background, wrap=500)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="maroon",fg="white",
                                  font="Helvetica" "10" "bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    # Put help button back to normal
    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Books and Authors Quiz")
    something = Start()
    root.mainloop()
