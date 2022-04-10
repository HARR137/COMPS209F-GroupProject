from library.graphics import *
from gobal_var import fontSize
import random
from common import createMsgBox, createImg, createRectangle, createCircle


MSG_1 = "Correct answer. Well done!Keep going!"
MSG_2 = "Wrong answer. Add oil!"
MSG_3 = ""



def checkAnswer(randnum, ans):
    if (randnum % 2 == 0) and (ans == "Odd"):
        Correct = False
    elif (randnum % 2 != 0) and (ans == "Odd"):
        Correct = True
    elif (randnum % 2 != 0) and (ans == "Even"):
        Correct = False
    elif (randnum % 2 == 0) and (ans == "Even"):
        Correct = True
    else:
        return None # invalid input
    return Correct

class lm3GUI():
    def __init__(self):
        pass

    def run(self):
        self.winWidth = 500
        self.winHeight = 500
        self.score = 0  # initialize score to 0
        self.attempt = 0  # how many questions answers
        self.max_attempt = 3  # how many questions total


        #ExitButton
        self.exitButtonSize= { "width": 50, "height": 25 }
        self.exitButtonCrood = { "x": 5, "y": 5 }

        self.win = GraphWin('Learning Module 3', self.winWidth, self.winHeight)
        self.exitButton = createRectangle(
            self,
            x = self.exitButtonCrood["x"],
            y = self.exitButtonCrood["y"],
            width = self.exitButtonSize["width"],
            height = self.exitButtonSize["height"]
        )
        self.exitButtonText = createMsgBox(
            self,
            msg = "EXIT",
            #+5 is a offset, since exitButton x,y crood is (5,5)
            x = self.exitButtonSize["width"]/2+5,
            y = self.exitButtonSize["height"]/2+5,
            color = "black",
            fontSize = fontSize["sFont"]
        )

        MsgBox = Text(Point(250, 150), "This number is an odd or evne number?(Enter Odd/Even)")
        MsgBox.draw(self.win)

        StatusBox = Text(Point(250, 240), "")
        StatusBox.draw(self.win)


        while True:
            if self.attempt >= self.max_attempt:  # finished all attempts
                self.updateResult('Completed.Your score is {}/{}'.format(self.score, self.attempt))
                break


            QuestionBox = Text(Point(250, 180), random.randint(1, 10))
            QuestionBox.draw(self.win)
            randnum = QuestionBox.getText()
            self.updateStatus("")
            while True:
                ans = self.waitGetInput()
                Correct = checkAnswer(randnum, ans)
                if Correct == True:
                     self.updateStatus(MSG_1)
                     self.score += 1
                     self.attempt += 1
                     QuestionBox.setText("")
                else:
                     self.updateStatus(MSG_2)
                     self.attempt += 1
                     QuestionBox.setText("")
                break
                  

        self.exitButtonSize = { "width": 50, "height": 25 }
        self.exitButtonCrood = { "x": 5, "y": 50 }
        
        self.win = GraphWin('Learning Module 4', self.winWidth, self.winHeight)

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
        return 1


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
            return ans
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
    lm3_GUI = lm3GUI()
    lm3GUI.run()