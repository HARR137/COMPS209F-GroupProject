from library.graphics import *
from gobal_var import fontSize
from common import createMsgBox, createInputBox, createRectangle

import learning_module.lm4.hips_gui as hips


class lm4GUI():
    def __init__(self):
        pass
        
        
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
        self.gameBox.setFill("red")


        self.inputBox = createInputBox(self, x=250, y=300, length=20)
        print(self.inputBox.getText())

        hipsModule = hips.hipsGui()
        hipsModule.run()

        self.lm1OnClickHandler(self.win)
        return 80

    def closeWin(self):
        self.win.close()


    def generateNumber():
        pass


    def lm1OnClickHandler(self, win):
        while True:
            checkMouse = win.getMouse()
            targetX = checkMouse.getX()
            targetY = checkMouse.getY()
            
            if targetX >= self.exitButtonCrood["x"]  and targetX <= self.exitButtonCrood["x"] + self.exitButtonSize["width"] and targetY >= self.exitButtonCrood["y"] and targetY <= self.exitButtonCrood["y"] + self.exitButtonSize["height"] :
                self.closeWin()
                break
                    