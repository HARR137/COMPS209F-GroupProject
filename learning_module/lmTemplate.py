from library.graphics import *
from gobal_var import fontSize
from common import createMsgBox, createImg, createRectangle

class lmTemplateGUI():
    def __init__(self):
        self.winWidth = 500
        self.winHeight = 500
        self.win = 0

        #ExitButton
        self.exitButtonSize= { "width": 50, "height": 25 }
        self.exitButtonCrood = { "x": 5, "y": 5 }
        
        
    def run(self):
        self.win = GraphWin('Learning Module Template', self.winWidth, self.winHeight)
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
        self.lm1OnClickHandler(self.win)
        return 1

    def closeWin(self):
        self.win.close()


    def lm1OnClickHandler(self, win):
        while True:
            checkMouse = win.getMouse()
            targetX = checkMouse.getX()
            targetY = checkMouse.getY()
            
            if targetX >= self.exitButtonCrood["x"]  and targetX <= self.exitButtonCrood["x"] + self.exitButtonSize["width"] and targetY >= self.exitButtonCrood["y"] and targetY <= self.exitButtonCrood["y"] + self.exitButtonSize["height"] :
                    self.closeWin()
                    break

if __name__ == "__main__":
    lmTemplateGUI = lmTemplateGUI()
    lmTemplateGUI.run()