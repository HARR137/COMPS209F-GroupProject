from library.graphics import *
from gobal_var import fontSize
from common import createMsgBox, createImg, createRectangle

class hintsGui():
    def __init__(self):
        self.winWidth = 600
        self.winHeight = 500
        self.win = 0

        #ExitButton
        self.exitButtonSize= { "width": 50, "height": 25 }
        self.exitButtonCrood = { "x": 5, "y": 5 }
        
        
    def run(self):
        self.win = GraphWin('How to play this game !?', self.winWidth, self.winHeight)
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

            x = self.exitButtonSize["width"]/2+5,
            y = self.exitButtonSize["height"]/2+5,
            color = "black",
            fontSize = fontSize["sFont"]
        )
        self.tipsHeader = createMsgBox(
            self,
            msg = "Are you up for the sorting challenge !? ",

            x = self.winWidth/2,
            y = self.winHeight/2-150,
            color = None,
            fontSize = fontSize["xlFont"]
        )

        self.tips1 = createMsgBox(
            self,
            msg = "This game will give you some numbers.",

            x = self.winWidth/2,
            y = self.winHeight/2-80,
            color = None,
            fontSize = fontSize["lFont"]
        )
        self.tips2 = createMsgBox(
            self,
            msg = "Can you sort it by Ascending or Descending order?",

            x = self.winWidth/2,
            y = self.winHeight/2-60,
            color = None,
            fontSize = fontSize["lFont"]
        )
        self.tips3 = createMsgBox(
            self,
            msg = "Type in your answer in the input field !",

            x = self.winWidth/2,
            y = self.winHeight/2-40,
            color = None,
            fontSize = fontSize["lFont"]
        )
        self.tips4 = createMsgBox(
            self,
            msg = "(separate number with ',' (comma). Just like below example)",
            x = self.winWidth/2,
            y = self.winHeight/2-20,
            color = None,
            fontSize = fontSize["lFont"]
        )

        self.tips5 = createImg(
            self,
            "resources/img/sort_example1.png",
            x = self.winWidth/2,
            y = self.winHeight/2 +50
        )



        self.exitAndNoTipsButton = createRectangle(
            self,
            x = self.exitButtonCrood["x"],
            y = self.exitButtonCrood["y"],
            width = self.exitButtonSize["width"],
            height = self.exitButtonSize["height"], 
            fillColor = None, 
            outlineColor = None
        )
        self.exitAndNoTipsButtonText = createMsgBox(
            self,
            msg = "EXIT (Don't display tips again)",

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
    hintsModule = hintsGui()
    hintsModule.run()