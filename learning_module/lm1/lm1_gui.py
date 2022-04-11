from library.graphics import *
from gobal_var import fontSize
import random
from common import createMsgBox, createCircle




def checkAnswer(randnum, ans):
    if (randnum % 2 == 0) and (ans == "odd"):
        Correct = False
    elif (randnum % 2 != 0) and (ans == "odd"):
        Correct = True
    elif (randnum % 2 != 0) and (ans == "even"):
        Correct = False
    elif (randnum % 2 == 0) and (ans == "even"):
        Correct = True
    else:
        return None # invalid input
    return Correct

class lm1GUI():
    def __init__(self):
        pass

    def run(self):
        self.winWidth = 500
        self.winHeight = 500
        self.score = 0  # initialize score to 0
        self.attempt = 0  # how many questions answers
        self.max_attempt = 5  # how many questions total

        self.win = GraphWin('Learning Module 1 - Odd or Even?', self.winWidth, self.winHeight)

        # # #ExitButton
        # self.exitButtonSize = { "width": 50, "height": 25 }
        # self.exitButtonCrood = { "x": 5, "y": 50 }
        # self.exitButtonSize = {"radius": 25}
        # self.exitButtonCrood = {"x": 5, "y": 5}
        # self.exitButton = createCircle(self,
        #                                   x=self.exitButtonCrood["x"],
        #                                   y=self.exitButtonCrood["y"],
        #                                   radius=self.exitButtonSize["radius"], 
        #                                   fillColor = "#C73618", 
        #                                   outlineColor = "#C73618")
        # self.exitButtonText = createMsgBox(
        #     self,
        #     msg="x",
        #     x=self.exitButtonCrood["x"] + 8.4, 
        #     y=self.exitButtonCrood["y"] + 7.4, 
        #     color="white",
        #     fontSize=fontSize["mFont"])

        MsgBox = Text(Point(250, 150), "Is this number odd or even? (Enter odd / even)")
        MsgBox.draw(self.win)

        theStatusBox = Text(Point(250, 240), "")
        theStatusBox.draw(self.win)


        while True:
            if self.attempt >= self.max_attempt:  # finished all attempts
                self.updateResult('Completed. Your score is {}/{}'.format(self.score, self.attempt))

                # #ExitButton
                self.exitButtonSize = { "width": 50, "height": 25 }
                self.exitButtonCrood = { "x": 5, "y": 50 }
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
                    
                break


            QuestionBox = Text(Point(250, 180), random.randint(1, 10))
            QuestionBox.draw(self.win)
            randnum = QuestionBox.getText()
            while True:
                ans = self.waitGetInput()
                Correct = checkAnswer(randnum, ans)
                if Correct == True:
                     self.score += 1
                     self.attempt += 1
                     QuestionBox.setText("")
                     theStatusBox.setText("")
                     theStatusBox.setText("Correct! Keep going")
                else: 
                     self.attempt += 1
                     QuestionBox.setText("")
                     theStatusBox.setText("")
                     theStatusBox.setText("Wrong! Add oil")
                break
                  

        self.lm1OnClickHandler(self.win)
        return self.score


    def closeWin(self):
        self.win.close()


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
    lm1_GUI = lm1GUI()
    lm1GUI.run()