# imports
import tkinter as tk   
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font as tkfont
from pathlib import Path
from typing import Any
import consultingMath
from dataclasses import dataclass

# making rounded buttons class https://stackoverflow.com/questions/42579927/how-to-make-a-rounded-button-tkinter

# define constants
QUESTIONNAMES = {0:"Break Even Point", 1:"Net Present Value", 2:"Return on Investment", 3:"Percent of Market Share", 4:"Total Market Share", 5:"Calculate ROI"}
QUESTIONFUNCTIONS = {0:consultingMath.breakEvenProblem, 1:consultingMath.netPresentValue, 2:consultingMath.netPresentValue, 3:consultingMath.percentOfM, 4:consultingMath.percentOfWhat, 5:consultingMath.calcROI}
FONT_TITLE = ("Montserrat", 46 * -1)
FONT_BODY = ("Montserrat", 17 * -1)

@dataclass
class defaultButton:
    bgColour: str = "#65A1C9"
    textColour: str = "#FFFFFF"
    bgColourOnClick: str = "#6B7C87"
    textColourOnClick:str = "#FFFFFF"
    font: tuple = ("Montserrat", 12)
    relief: str = "flat"

def checkCountQuestions(problemType, countQuestions):
    try: 
        int(countQuestions)
    except:
        return
    questionPage(problemType=problemType, countQuestions=countQuestions)
    
# function to build assets for the main page
def mainPage(): # frame 0
    canvas = Canvas(
    window,
    bg = "#171C29",
    height = 727,
    width = 1022,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )                                                                                           

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        78,
        173,
        anchor="nw",
        text="PRACTICE YOUR \nCONSULTING MATH!",
        fill="#FFFFFF",
        font=FONT_TITLE
    )

    canvas.create_text(
        78,
        330,
        anchor="nw",
        text="A math drill a day keeps the panic away!",
        fill="#FFFFFF",
        font=FONT_BODY
    )

    canvas.create_text(
        78,
        391.8984375,
        anchor="nw",
        text="BUSINESS BASICS",
        fill="#8C8C8C",
        font=FONT_BODY
    )

    canvas.create_text(
        343,
        391.8984375,
        anchor="nw",
        text="MARKET SHARE PERCENTS",
        fill="#8C8C8C",
        font=FONT_BODY
    )

    # insert question buttons. This is adaptive to the number of question types included in QUESTIONNAMES
    firstQuestionButtonLocation = {"x":78, "y":426.6865234375, "width":85.9052734375, "height":48.9873046875}
    for button in QUESTIONNAMES:
        Button(
            bg=defaultButton.bgColour,
            activebackground=defaultButton.bgColourOnClick,
            fg=defaultButton.textColour,
            activeforeground=defaultButton.textColourOnClick,
            relief=defaultButton.relief,
            font=defaultButton.font,
            text=QUESTIONNAMES[button],
            command=lambda b=button: problemCountScreen(b) # QUESTIONFUNCTIONS[button]()
        ).place(
            x=firstQuestionButtonLocation["x"] + 260 * (button // 3), 
            y=firstQuestionButtonLocation["y"] + 70 * (button % 3),
            width=len(max(list(QUESTIONNAMES.values()), key=len))*10,
            height=firstQuestionButtonLocation["height"]
        )

    # insert exit button
    Button(
        bg=defaultButton.bgColour,
        activebackground=defaultButton.bgColourOnClick,
        fg=defaultButton.textColour,
        activeforeground=defaultButton.textColourOnClick,
        relief=defaultButton.relief,
        font=defaultButton.font,
        text="Exit",
        command=lambda: print(scoreBoard.get_score_dict())# exit()
    ).place(
        x=908,
        y=30,
        width=85.9052734375,
        height=48.9873046875
    )
    
    window.mainloop()

# function to build assets for a 'number of questions' page
def problemCountScreen(problemType):
    canvas = Canvas(
        window,
        bg = "#171C29",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        107.0,
        407.0,
        anchor="nw",
        text=QUESTIONNAMES[problemType],
        fill="#FFFFFF",
        font=FONT_TITLE
    )

    canvas.create_text(
        107.0,
        501.0,
        anchor="nw",
        text="How many questions would you like to answer?",
        fill="#FFFFFF",
        font=FONT_BODY
    )
 
    questionsToAsk = tk.Entry(
        window,
        bg="#FFFFFF",
        bd=2,
        font=FONT_BODY,
        exportselection=0,
        fg="#000000",
        relief="flat"
    )
    questionsToAsk.place(
        x=107.0,
        y=557.0,
        width=335.0,
        height=58.0
    )
      
    # add enter button
    Button(
            bg=defaultButton.bgColour,
            activebackground=defaultButton.bgColourOnClick,
            fg=defaultButton.textColour,
            activeforeground=defaultButton.textColourOnClick,
            relief=defaultButton.relief,
            font=defaultButton.font,
            text="Enter",
            command=lambda: checkCountQuestions(problemType, questionsToAsk.get())
        ).place(
            x=107.0+335 +20,
            y=557.0,
            width=70.0,
            height=58.0
        )

    window.mainloop()

# function to build assets for the questions page
def questionPage(problemType, countQuestions):

    # input validation for user answers
    def confirmInteger(checkInt):
        try:
            float(checkInt) + 1
        except:
            return
        print("var set")
        submitFlag.set(True)
        return

    def diplayQuestion(phrase):
        printQuestion = tk.Text(
            bd=0,
            bg="#171C29",
            fg="#FFFFFF",
            font=FONT_BODY
        )
        printQuestion.place(
            x=107.0,
            y=280.0,
        )
        printQuestion.insert(tk.END, phrase)

        enterAnswer = tk.Entry(
            window,
            bg="#FFFFFF",
            bd=2,
            font=FONT_BODY,
            exportselection=0,
            fg="#000000",
            relief="flat"
        )
        enterAnswer.place(
            x=107.0,
            y=557.0,
            width=335.0,
            height=58.0
        )

        Button(
            bg=defaultButton.bgColour,
            activebackground=defaultButton.bgColourOnClick,
            fg=defaultButton.textColour,
            activeforeground=defaultButton.textColourOnClick,
            relief=defaultButton.relief,
            font=defaultButton.font,
            text="Enter",
            command=lambda: confirmInteger(enterAnswer.get()) # submitFlag.set(True)
        ).place(
            x=107.0+335 +20,
            y=557.0,
            width=70.0,
            height=58.0
        )

        window.wait_variable(submitFlag)
        userAns.set(enterAnswer.get())
        printQuestion.destroy()
        enterAnswer.destroy()
        
    def displayAnswer(phrase):

        printAnswer = tk.Text(
            bd=0,
            bg="#171C29",
            fg="#FFFFFF",
            font=FONT_BODY
        )
        printAnswer.place(
            x=107.0,
            y= 501.0,
        )
        printAnswer.insert(tk.END, phrase)

        Button(
            bg=defaultButton.bgColour,
            activebackground=defaultButton.bgColourOnClick,
            fg=defaultButton.textColour,
            activeforeground=defaultButton.textColourOnClick,
            relief=defaultButton.relief,
            font=defaultButton.font,
            text="OK",
            command=lambda: submitFlag.set(True)
        ).place(
            x=107.0+335 +20,
            y=557.0,
            width=70.0,
            height=58.0
        )

        window.wait_variable(submitFlag)
        printAnswer.destroy()

    canvas = Canvas(
        window,
        bg = "#171C29",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        107.0,
        200.0,
        anchor="nw",
        text=QUESTIONNAMES[problemType],
        fill="#FFFFFF",
        font=FONT_TITLE
    )
 
    userAns = tk.DoubleVar()
    submitFlag = tk.BooleanVar(value=False)
    for question in range(int(countQuestions)):
        phrase, answer = QUESTIONFUNCTIONS[problemType]()
        submitFlag.set(False)
        diplayQuestion(phrase)
        submitFlag.set(False)
        if answer == userAns.get():
            phrase = f"Correct, the answer is {answer}. \nIn the future we hope to add the solution here as well."
            scoreBoard.update_problems_correct(problem_type=problemType)
        else:
            phrase = f"Incorrect, the answer is {answer}. \nIn the future we hope to add the solution here as well."
        displayAnswer(phrase)
        scoreBoard.update_problems_asked(problem_type=problemType)
    mainPage()
    window.mainloop()

# function to build assets for the results page
def resultsPage():
    
    canvas = Canvas(
        window,
        bg = "#171C29",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)
    canvas.create_text(
        107.0,
        200.0,
        anchor="nw",
        text="Results",
        fill="#FFFFFF",
        font=FONT_TITLE
    )


if __name__ == "__main__":

    # define the window
    window = Tk()
    window.title("Consulting Math")
    window.geometry("1022x727")
    window.configure(bg = "#171C29")
    window.resizable(False, False)
    scoreBoard = consultingMath.ScoreKeeper(QUESTIONNAMES)
    mainPage()