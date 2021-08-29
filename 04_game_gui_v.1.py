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
        self.easy_button = Button(text="Play", command= self.to_game)
        self.easy_button.grid(row=1)

    def to_game(self):
        Game()

class Game:
    def __init__(self):

        # Importing csv file
        with open('movies-directors.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # Inital Score
        self.score = 0

        # Amounts of games played
        self.played = 0

        # chooses four different movies / directors from the list
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

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid(padx=10, pady=10)

        # Director Label row 0
        self.capital_label = Label(self.game_frame, text=self.question,
                                   font="Helvetica 15 bold")
        self.capital_label.grid(row=0)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box, width=50, height=50)
        self.top_answers_frame.grid(row=2, padx=5)

        # width, wrap and height for buttons
        wt=15
        ht=3
        wr=100

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text=button_list[0],
                                             font="Helvetica 10 bold", padx=5, pady=5,width=wt,height=ht,wrap=wr,
                                             command=lambda: self.reveal_answer(0))
        self.top_left_answer_button.grid(column=0, row=0,padx=5,pady=5)

        self.top_right_answer_button = Button(self.top_answers_frame, text=button_list[1],
                                             font="Helvetica 10 bold", padx=5,pady=5,width=wt,height=ht,wrap=wr,
                                             command=lambda: self.reveal_answer(1))
        self.top_right_answer_button.grid(column=1, row=0,padx=5,pady=5)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text=button_list[2],
                                             font="Helvetica 10 bold", padx=5, pady=5,width=wt,height=ht,wrap=wr,
                                             command=lambda: self.reveal_answer(2))
        self.bottom_left_answer_button.grid(column=0, row=1,padx=5,pady=5)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text=button_list[3],
                                              font="Helvetica 10 bold", padx=5, pady=5,width=wt,height=ht,wrap=wr,
                                              command=lambda: self.reveal_answer(3))
        self.bottom_right_answer_button.grid(column=1, row=1,padx=5,pady=5)


    def reveal_answer(self, location):
        # Print corresponding number based on location
        # TL = 0 TR =1 BL = 2 BR = 3
        print(location)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    something = Start()
    root.mainloop()

