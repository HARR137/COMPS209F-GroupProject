from library.graphics import *
from gobal_var import fontSize
import random
from common import createMsgBox, createImg, createRectangle, createCircle


MSG_1 = "Correct answer. Well done! Keep going!"
MSG_2 = "Wrong answer. Add oil!"
MSG_3 = ""



def checkAnswer(a, b, ans):
    print(a, b, ans)
    if (a > b) and (ans == a):
        Correctans = a
    elif (a > b) and (ans == b):
        Correctans = a
    elif (a < b) and (ans == a):
        Correctans = b
    elif (a < b) and (ans == b):
        Correctans = b
    else:
        return None # invalid input
    theGrade = Correctans == ans
    return theGrade

def genQuestion():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return (a, b)

class lm2GUI():
    def __init__(self):
        pass

    def run(self):
        self.winWidth = 500
        self.winHeight = 500
        self.score = 0  # initialize score to 0
        self.attempt = 0  # how many questions answers
        self.max_attempt = 3  # how many questions total

        self.win = GraphWin('Learning Module 2', self.winWidth, self.winHeight)

        #ExitButton
        self.exitButtonSize = {"radius": 25}
        self.exitButtonCrood = {"x": 5, "y": 5}
        self.exitButton = createCircle(self,
                                          x=self.exitButtonCrood["x"],
                                          y=self.exitButtonCrood["y"],
                                          radius=self.exitButtonSize["radius"], 
                                          fillColor = "#C73618", 
                                          outlineColor = "#C73618")
        self.exitButtonText = createMsgBox(
            self,
            msg="x",
            x=self.exitButtonCrood["x"] + 8.4, 
            y=self.exitButtonCrood["y"] + 7.4, 
            color="white",
            fontSize=fontSize["mFont"])

        MsgBox = Text(Point(250, 150), "Which number is bigger")
        MsgBox.draw(self.win)

        StatusBox = Text(Point(250, 240), "")
        StatusBox.draw(self.win)


        while True:
            if self.attempt >= self.max_attempt:  # finished all attempts
                self.updateResult('Completed. Your score is {}/{}'.format(self.score, self.attempt))
                break

            self.question = genQuestion()
            questiontxt = self.question
            QuestionBox = Text(Point(250, 180), questiontxt )
            QuestionBox.draw(self.win)
            a = self.question[0]
            b = self.question[1]
            self.updateStatus("")
            while True:
                ans = self.waitGetInput()
                theGrade = checkAnswer(a, b, ans)
                if theGrade == True:
                     self.updateStatus(MSG_1)
                     self.score += 1
                     self.attempt += 1
                     QuestionBox.setText("")
                else:
                     self.updateStatus(MSG_2)
                     self.attempt += 1
                     QuestionBox.setText("")
                break
                  

        self.exitButtonSize = {"radius": 25}
        self.exitButtonCrood = {"x": 5, "y": 5}
        self.exitButton = createCircle(self,
                                          x=self.exitButtonCrood["x"],
                                          y=self.exitButtonCrood["y"],
                                          radius=self.exitButtonSize["radius"], 
                                          fillColor = "#C73618", 
                                          outlineColor = "#C73618")
        self.exitButtonText = createMsgBox(
            self,
            msg="x",
            x=self.exitButtonCrood["x"] + 8.4, 
            y=self.exitButtonCrood["y"] + 7.4, 
            color="white",
            fontSize=fontSize["mFont"])

        self.lm1OnClickHandler(self.win)
        return self.score


    def closeWin(self):
        self.win.close()

    def updateStatus(self, text):
        StatusBox = Text(Point(250, 240), "")
        StatusBox.draw(self.win)
        StatusBox.setText(text)

    def updateResult(self, text):
        resultBox = Text(Point(250, 270), "")
        resultBox.draw(self.win)
        resultBox.setText(text)


    def waitGetInput(self):
        inputbox = Entry(Point(250, 210), 10)
        inputbox.draw(self.win)
        self.win.getMouse()
        ans = inputbox.getText()
        try: 
            ans_int = int(ans)
            return ans_int
        except ValueError:
            pass
        return None

    def lm1OnClickHandler(self, win):
        while True:
            checkMouse = win.getMouse()
            targetX = checkMouse.getX()
            targetY = checkMouse.getY()
            
            if targetX >= self.exitButtonCrood["x"] - self.exitButtonSize["radius"] and targetX <= self.exitButtonCrood["x"] + self.exitButtonSize["radius"] and targetY >= self.exitButtonCrood["y"] - self.exitButtonSize["radius"] and targetY <= self.exitButtonCrood["y"] + self.exitButtonSize["radius"]:
                self.closeWin()
                break

                    

if __name__ == "__main__":
    lm2_GUI = lm2GUI()
    lm2GUI.waitGetInput()
    lm2GUI.run()