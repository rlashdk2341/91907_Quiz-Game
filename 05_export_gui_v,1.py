from tkinter import *
from functools import partial
import random
import csv

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

    def to_play(self):
        print("you chose play button")
        Game()
        self.start_frame.destroy()

    def help(self):
        print("you chose help button")
        get_help = Help(self)
        get_help.help_text.configure(text="This quiz is about testing your knowledge for the \n"
                                          "naming famous books and authors. \n\n"
                                          "The name of the book will be given, \n"
                                          "and you will have to answer the corresponding author. \n\n"
                                          "This Quiz is a multiple choice quiz. \n\n"
                                          "I wish you best of luck and hope you enjoy this game.")


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

class Game:
    def __init__(self):

        # Import the csv file, name of csv file goes here...
        with open('movies-directors.csv', 'r') as f:
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # Inital Score
        self.score = 0

        # Amounts of games played
        self.played = 0

        question_ans = random.choice(my_list)
        yes = random.choice(my_list)
        no = random.choice(my_list)
        ok = random.choice(my_list)

        self.question = question_ans[1]
        self.answer = question_ans[0]
        incorrect1 = yes[0]
        incorrect2 = no[0]
        incorrect3 = ok[0]
        print(question_ans)

        button_list = [self.answer, incorrect1, incorrect2, incorrect3]
        random.shuffle(button_list)
        self.top_left = button_list[0]
        self.top_right = button_list[1]
        self.bottom_left = button_list[2]
        self.bottom_right = button_list[3]

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid(padx=10, pady=10)

        # Director Label row 0
        self.director_label = Label(self.game_frame, text=self.question,
                                    font="Helvetica 15 bold")
        self.director_label.grid(row=0)

        # Label showing correct or incorrect row 1
        self.answer_box = Label(self.game_frame, text="", font="Helvetica 11 italic", width=35, wrap=300)
        self.answer_box.grid(row=1)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box, width=50, height=50)
        self.top_answers_frame.grid(row=2, padx=5)

        # width, wrap, font height for buttons
        wt = 15
        ht = 2
        wr = 170
        ft = "Helvetica 15"

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text=self.top_left,
                                             font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr,
                                             command=lambda: self.reveal_answer(self.top_left))
        self.top_left_answer_button.grid(column=0, row=0, padx=5, pady=5)

        self.top_right_answer_button = Button(self.top_answers_frame, text=self.top_right,
                                              font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr,
                                              command=lambda: self.reveal_answer(self.top_right))
        self.top_right_answer_button.grid(column=1, row=0, padx=5, pady=5)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text=self.bottom_left,
                                                font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr,
                                                command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_left_answer_button.grid(column=0, row=1, padx=5, pady=5)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text=self.bottom_right,
                                                 font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr,
                                                 command=lambda: self.reveal_answer(self.bottom_right))
        self.bottom_right_answer_button.grid(column=1, row=1, padx=5, pady=5)

        # Label for the score and games played row 3
        self.score_label = Label(self.game_box, text="{} correct, {} rounds played".format(self.score, self.played))
        self.score_label.grid(row=3)

        # The Next button to proceed to the next round row 4
        self.next_button = Button(self.game_box, text="Next", command=lambda: self.to_next(my_list))
        self.next_button.grid(row=4)

        # Disable the next button initially,
        self.next_button.config(state=DISABLED)

    def reveal_answer(self, location):

        # Disable all the buttons
        self.top_left_answer_button.config(state=DISABLED)
        self.top_right_answer_button.config(state=DISABLED)
        self.bottom_left_answer_button.config(state=DISABLED)
        self.bottom_right_answer_button.config(state=DISABLED)

        # Enable the next_button
        self.next_button.config(state=NORMAL)

        # Increase total rounds played by 1
        self.played += 1

        # Check if button is correct.
        if location == self.answer:
            self.answer_box.config(text="Correct!", fg="green")
            self.score += 1

        else:
            self.answer_box.config(text="Incorrect, correct Movie was {}".format(self.answer), fg="red")

        # Update the score that the user has
        self.score_label.config(text="{} correct / {} rounds played".format(self.score, self.played))

    def to_next(self, list):
        if self.played == 10:
            End(self.score)
            self.game_box.destroy()

        self.top_left_answer_button.config(state=NORMAL)
        self.top_right_answer_button.config(state=NORMAL)
        self.bottom_left_answer_button.config(state=NORMAL)
        self.bottom_right_answer_button.config(state=NORMAL)
        self.next_button.config(state=DISABLED)
        self.answer_box.config(text="")

        question_ans = random.choice(list)
        yes = random.choice(list)
        no = random.choice(list)
        ok = random.choice(list)

        self.question = question_ans[1]
        self.answer = question_ans[0]
        incorrect1 = yes[0]
        incorrect2 = no[0]
        incorrect3 = ok[0]
        print(question_ans)

        self.director_label.config(text=self.question)

        button_list = [self.answer, incorrect1, incorrect2, incorrect3]
        random.shuffle(button_list)
        self.top_left = button_list[0]
        self.top_right = button_list[1]
        self.bottom_left = button_list[2]
        self.bottom_right = button_list[3]

        # Defining the randomized list to their corresponding buttons
        self.top_left_answer_button.config(text=self.top_left, command=lambda: self.reveal_answer(self.top_left))
        self.top_right_answer_button.config(text=self.top_right, command=lambda: self.reveal_answer(self.top_right))
        self.bottom_left_answer_button.config(text=self.bottom_left,
                                              command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_right_answer_button.config(text=self.bottom_right,
                                               command=lambda: self.reveal_answer(self.bottom_right))


class End:
    def __init__(self,score):

        # Background color is light yellow
        background = "#FFF4C3"

        # Accuracy percentage
        percentage= score/10

        # End Frame
        self.end_box = Toplevel()
        self.end_frame = Frame(self.end_box, bg=background)
        self.end_frame.grid(row=0)
        self.end_box.protocol('WM_DELETE_WINDOW', self.to_quit)


        # Heading row 0
        self.end_heading = Label(self.end_frame, text="Thanks for playing!", font= "Arial 19 bold", bg=background)
        self.end_heading.grid(row=0, padx=10)

        # Game statistics row 1
        self.end_stats = Label(self.end_frame, text="You have got \n {} \n correct out of \n 10 \n\n"
                                                    "You have got {:.2f}%" .format(score,percentage),
                               bg=background, font="Helvetica 10")
        self.end_stats.grid(row=1)

        # Button grid row 2
        self.end_buttons = Frame(self.end_frame, bg=background)
        self.end_buttons.grid(row=2)

        # Export button row 0 column 0
        self.end_export_button = Button(self.end_buttons, text="Export", font="Helvetica 10 bold",
                                        command=lambda:to_export, width=8, bg="#A6FF56", height=2)
        self.end_export_button.grid(row=0, column=0,padx=6,pady=5)

        # Retry Button row 0 column 1
        self.end_retry_button = Button(self.end_buttons, text="Play Again", font="Helvetica 10 bold",
                                       command=self.to_start, width=8, bg="#569FFF", height=2)
        self.end_retry_button.grid(row=0, column=1, padx=6,pady=5)

        # Quit button row 0 column 2
        self.end_quit_button = Button(self.end_buttons, text="Quit", font="Helvetica 10 bold",
                                      command=root.quit, width=8, bg="#FF5656", height=2)
        self.end_quit_button.grid(row=0, column=2, padx=6,pady=5)

    def to_start(self):
        Start()
        self.end_box.destroy()

    def to_quit(self):
        root.quit()

class converter:
    def __init__(self):
        # Formatting variables... This color is light orange
        background_color = "#FFE6CC"

        self.all_calc_list = []

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.converter_frame, text="Information",
                                     font=("Arial", "8", "bold"),
                                     bg=background_color,
                                     padx=10, pady=10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):
        # This color is Lightish Yellow
        background = "#EBFF6B"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press 'x' cross at the top, closes history and 'releases' history button.
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation history",
                                 font=("Arial", "15", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent calculations ",

                                  justify=LEFT, width=40, bg=background, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # history Output goes here... (Row 2)

        # Generate string from list of calcualtions...

        history_string = ""
        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[lens(calc_history) - item - 1] + "\n"


        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here are your most recent calculations ")

        # Export /Dismiss Buttons Frame (row 3)

        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)


class Export:
    def __init__(self, partner, calc_history):
        print(calc_history)

        # This color is Lightish Yellow
        background = "#EBFF6B"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press 'x' cross at the top, closes export and 'releases' export button.
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font=("Arial", "15", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text= "If the filename you entered already exists,"
                                                          "it will be overwritten.", justify=LEFT, bg=background,
                                 fg='red', font="Arial 10 italic",
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

    def save_history(self, partner, calc_history):

        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = " (no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.save_error_label.config(text="Invalid filename - {}".format(problem))

            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            filename = filename + ".txt"

            f = open(filename, "w+")

            for item in calc_history:
                f.write(item + "\n")

            f.close()

            self.close_export(partner)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = converter()
    root.mainloop()
