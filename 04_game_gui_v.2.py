from tkinter import *
import csv
import random


class Start:
    def __init__(self):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Country Capital Quiz Heading row 0
        self.capital_label = Label (self.start_frame, text="Movies and Directors Quiz",
                                    font= "Helvetica 20 bold")
        self.capital_label.grid(row=0)

        # to_game button row 1
        self.play_button = Button(text="Play", command= self.to_game)
        self.play_button.grid(row=1)

    def to_game(self):
        Game()

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
        no= random.choice(my_list)
        ok = random.choice(my_list)

        self.question = question_ans[1]
        self.answer = question_ans[0]
        incorrect1 = yes[0]
        incorrect2 = no[0]
        incorrect3 = ok[0]
        print(question_ans)

        button_list = [self.answer, incorrect1, incorrect2, incorrect3]
        random.shuffle(button_list)
        self.top_left=button_list[0]
        self.top_right=button_list[1]
        self.bottom_left=button_list[2]
        self.bottom_right=button_list[3]

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid(padx=10, pady=10)

        # Capital Label row 0
        self.capital_label = Label(self.game_frame, text=self.question,
                                   font="Helvetica 15 bold")
        self.capital_label.grid(row=0)

        # Label showing correct or incorrect row 1
        self.answer_box = Label(self.game_frame, text="", font="Helvetica 14 italic", width=35, wrap=300)
        self.answer_box.grid(row=1)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box, width=50, height=50)
        self.top_answers_frame.grid(row=2, padx=5)

        # width, wrap, font height for buttons
        wt=15
        ht=2
        wr=170
        ft="Helvetica 15"

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text=self.top_left,
                                             font=ft, padx=5, pady=5,width=wt,height=ht,wrap=wr,
                                             command=lambda: self.reveal_answer(self.top_left))
        self.top_left_answer_button.grid(column=0, row=0,padx=5,pady=5)

        self.top_right_answer_button = Button(self.top_answers_frame, text=self.top_right,
                                             font=ft, padx=5,pady=5,width=wt,height=ht,wrap=wr,
                                             command=lambda: self.reveal_answer(self.top_right))
        self.top_right_answer_button.grid(column=1, row=0,padx=5,pady=5)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text=self.bottom_left,
                                             font=ft, padx=5, pady=5,width=wt,height=ht,wrap=wr,
                                             command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_left_answer_button.grid(column=0, row=1,padx=5,pady=5)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text=self.bottom_right,
                                              font=ft, padx=5, pady=5,width=wt,height=ht,wrap=wr,
                                              command=lambda: self.reveal_answer(self.bottom_right))
        self.bottom_right_answer_button.grid(column=1, row=1,padx=5,pady=5)

        # Label for the score and games played row 3
        self.score_label = Label(self.game_box, text="{} correct, {} rounds played".format(self.score,self.played))
        self.score_label.grid(row=3)

        # The Next button to proceed to the next round row 4
        self.next_button = Button(self.game_box, text="Next", command=lambda:self.to_next(my_list))
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

    def to_next(self,list):

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

        self.capital_label.config(text=self.question)

        # Defining the randomized list to their corresponding buttons
        self.top_left_answer_button.config(text=self.top_left, command=lambda: self.reveal_answer(self.top_left))
        self.top_right_answer_button.config(text=self.top_right, command=lambda: self.reveal_answer(self.top_right))
        self.bottom_left_answer_button.config(text=self.bottom_left, command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_right_answer_button.config(text=self.bottom_right,
                                               command=lambda: self.reveal_answer(self.bottom_right))

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    something = Start()
    root.mainloop()

