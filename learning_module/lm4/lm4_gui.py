from hashlib import new
from library.graphics import *
from gobal_var import fontSize
from common import createMsgBox, createInputBox, createRectangle
from random import randrange, sample

import learning_module.lm4.hints_gui as hints



class lm4GUI():
    def __init__(self):
        self.randNumList = []
        self.roundNum = 5
        # self.value2
        # self.value3
        
        
    def run(self):
        self.winWidth = 500
        self.winHeight = 500

        #ExitButton
        self.exitButtonSize= { "width": 50, "height": 25 }
        self.exitButtonCrood = { "x": 5, "y": 5 }
        
        self.win = GraphWin('Learning Module 4', self.winWidth, self.winHeight)
        self.exitButton = createRectangle(
            self,
            x = self.exitButtonCrood["x"],
            y = self.exitButtonCrood["y"],
            width = self.exitButtonSize["width"],
            height = self.exitButtonSize["height"], 
            fillColor = None, 
            outlineColor = None
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
        
        self.gameBox = createRectangle(
            self,
            x = 60,
            y = 50,
            width = 440,
            height = 200,
            fillColor = None,
            outlineColor = None
        )
        self.gameBox.setFill("black")
        self.generateNumber()


        self.inputBox = createInputBox(self, x=250, y=300, length=20)
        # print(self.inputBox.getText())

        hintsModule = hints.hintsGui()
        hintsModule.run()

        self.lm1OnClickHandler(self.win)
        return 80

    def closeWin(self):
        self.win.close()


    def generateNumber(self):
        for j in range(self.roundNum): 
            self.randNumList.append(sample(range(1, 20), 5))
        print(self.randNumList)


    def lm1OnClickHandler(self, win):
        i = 0
        while self.roundNum:
            questions = self.randNumList[i]

            margin = 50
            for number in questions:
                questionsSeperate = str(number) + " "
                createMsgBox(self,
                            msg=questionsSeperate,
                            x=90 + margin,
                            y=120,
                            color="white",
                            fontSize=fontSize["xxxlFont"])
                margin = margin + 100
            i += 1

        
        #just finish looping the first questions's digit to the screen
        #On user click enter / nexr questions, check answer and then show correct or wrong -> next question ->  self.roundNum--
        #and then draw an other questions



            checkMouse = win.getMouse()
            targetX = checkMouse.getX()
            targetY = checkMouse.getY()
            #ending part
            self.roundNum -= 1


            
            if targetX >= self.exitButtonCrood["x"]  and targetX <= self.exitButtonCrood["x"] + self.exitButtonSize["width"] and targetY >= self.exitButtonCrood["y"] and targetY <= self.exitButtonCrood["y"] + self.exitButtonSize["height"] :
                self.closeWin()
                break
                
