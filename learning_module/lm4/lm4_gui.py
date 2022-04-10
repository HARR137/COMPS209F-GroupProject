from hashlib import new
from library.graphics import *
from gobal_var import fontSize
from common import createMsgBox, createInputBox, createRectangle, createCircle
from random import randrange, sample

import learning_module.lm4.hints_gui as hints

class lm4GUI():
    def __init__(self):
        self.randNumList = []
        self.roundNum = 5
        self.checkEnterButton = False
        self.score = 0
        
        
    def run(self):
        self.winWidth = 500
        self.winHeight = 500
        self.win = GraphWin('Learning Module 4', self.winWidth, self.winHeight)
        # self.win.setBackground("#161616")

        #ExitButton
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
        

        self.gameBoxCrood = { "starting_x": 60, "starting_y": 50, "ending_x": 440, "ending_y": 200 }
        self.gameBox = createRectangle(
            self,
            starting_x = self.gameBoxCrood["starting_x"],
            starting_y = self.gameBoxCrood["starting_y"], 
            ending_x = self.gameBoxCrood["ending_x"],
            ending_y = self.gameBoxCrood["ending_y"],
            fillColor = None,
            outlineColor = None
        )
        self.gameBox.setFill("black")

        self.inputBox = createInputBox(self, x=250, y=300, length=20)

        self.generateNumber()

        hintsModule = hints.hintsGui()
        hintsModule.run()

        # self.enterButtonSize = { "width": 50, "height": 25 }
        # self.enterButtonCrood = { "x": 150, "y": 400 }


        self.enterButtonCrood = { "starting_x": 115, "starting_y": 380, "ending_x": 215, "ending_y": 410 }
        self.enterTextCrood = { "x": 165, "y": 395 }
        self.enterButton = createRectangle(
            self,
            starting_x = self.enterButtonCrood["starting_x"],
            starting_y = self.enterButtonCrood["starting_y"], 
            ending_x = self.enterButtonCrood["ending_x"],
            ending_y = self.enterButtonCrood["ending_y"],
            fillColor = "#159947", 
            outlineColor = "#159947"
        )
        self.enterButtonText = createMsgBox(
            self,
            msg = "ENTER",
            x = self.enterTextCrood["x"],
            y = self.enterTextCrood["y"],
            color = "white",
            fontSize = fontSize["sFont"]
        )


        self.nextButtonCrood = { "starting_x": 285, "starting_y": 380, "ending_x": 385, "ending_y": 410 }
        self.nextTextCrood = { "x": 335, "y": 395 }
        self.nextButton = createRectangle(
            self,
            starting_x = self.nextButtonCrood["starting_x"],
            starting_y = self.nextButtonCrood["starting_y"], 
            ending_x = self.nextButtonCrood["ending_x"],
            ending_y = self.nextButtonCrood["ending_y"],
            fillColor = "#0193A5", 
            outlineColor = "#0193A5"
        )
        self.nextButtonText = createMsgBox(
            self,
            msg = "NEXT QUESTION",
            x = self.nextTextCrood["x"],
            y = self.nextTextCrood["y"],
            color = "white",
            fontSize = fontSize["sFont"]
        )


        self.lm1OnClickHandler(self.win)

        return self.score

    def closeWin(self):
        self.win.close()


    def generateNumber(self):
        for j in range(self.roundNum): 
            self.randNumList.append(sample(range(1, 20), 5))
        print(self.randNumList)

    def generateNumList(self, questions): 
        margin = 55
        for number in questions:
            questionsSeperate = str(number) + " "
            self.textMsgBox.append(createMsgBox(self,
                        msg=questionsSeperate,
                        x=90 + margin,
                        y=120,
                        color="white",
                        fontSize=fontSize["xxxlFont"])
                        )
            margin = margin + 55

    def getAns(self): 
        userAns = self.inputBox.getText()
        return list(eval(userAns))

    def checkAns(self, question): 
        returnUserAns = self.getAns()
        question.sort()

        if question == returnUserAns: 
            self.score += 1
            return True
        else: 
            return False
        

        # if question == returnUserAns: 
        #     return "Very good! It's correct!"
        # else: 
        #     return "Wrong answer... Practice makes perfect!"

    def lm1OnClickHandler(self, win):
        i = 4
        finishAns = True
        self.textMsgBox = []
        # self.roundNum = 5
        while True:

            if finishAns: 
                #start of printing questions--------

                questions = self.randNumList[i]

                self.generateNumList(questions)
                #End of printing questions--------

                #load the next 5 int in the randNumList
                finishAns = False


            checkMouse = win.getMouse()
            targetX = checkMouse.getX()
            targetY = checkMouse.getY()
        
        #just finish looping the first questions's digit to the screen
        #On user click enter / nexr questions, check answer and then show correct or wrong -> next question ->  self.roundNum--
        #and then draw an other questions

            # enterButton onClick
            if targetX >= self.enterButtonCrood["starting_x"] and targetX <= self.enterButtonCrood["ending_x"] and targetY >= self.enterButtonCrood["starting_y"] and targetY <= self.enterButtonCrood["ending_y"]:
                self.checkEnterButton = True
                self.getAns()
                
                returnedAns = self.checkAns(questions)

                returnMsg = lambda ans: "Very good! It's correct!" if (ans) else "Wrong answer... Practice makes perfect!"
                returnColor = lambda ans: "green" if (ans) else "red"

                self.checkAnsMsgBox = createMsgBox(self,
                                      msg=returnMsg(returnedAns),
                                    #   msg=self.checkAns(questions),
                                      x=250,
                                      y=240,
                                      color=returnColor(returnedAns),
                                      fontSize=fontSize["mFont"])

                if self.roundNum == 0: 
                    self.win.close()
                    break
                # self.enterAns()
                # break
                print("enter button")

            # nextButton onClick
            if self.checkEnterButton == True and targetX >= self.nextButtonCrood["starting_x"] and targetX <= self.nextButtonCrood["ending_x"] and targetY >= self.nextButtonCrood["starting_y"] and targetY <= self.nextButtonCrood["ending_y"]:
                self.checkEnterButton = False
                # self.nextQue()
                # break
                self.roundNum -= 1
                i -= 1
                if i == -1: 
                    self.closeWin()
                    break
                
                for k in self.textMsgBox:
                    k.undraw()
                self.textMsgBox.clear()
                # for m in self.inputBox: 
                #     m.undraw()
                self.inputBox.setText("")
                self.checkAnsMsgBox.setText("")
                finishAns = True
                print("next button")


           # exitButton onClick
            if targetX >= self.exitButtonCrood["x"] - self.exitButtonSize["radius"] and targetX <= self.exitButtonCrood["x"] + self.exitButtonSize["radius"] and targetY >= self.exitButtonCrood["y"] - self.exitButtonSize["radius"] and targetY <= self.exitButtonCrood["y"] + self.exitButtonSize["radius"]:
                self.closeWin()
                break
                    
