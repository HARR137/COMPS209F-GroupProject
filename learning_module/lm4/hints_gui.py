from library.graphics import *
from gobal_var import fontSize
from common import createMsgBox, createImg, createRectangle, createCircle


class hintsGui():
    def __init__(self):
        self.winWidth = 600
        self.winHeight = 500
        self.win = 0

        self.exitButtonSize= { "width": 50, "height": 25 }
        self.exitButtonCrood = { "x": 5, "y": 5 }
        
        
    def run(self):
        self.win = GraphWin('Learning Module 4 - How to play this game?', self.winWidth, self.winHeight)

        # exit button
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

        self.exitToStartTips = createMsgBox(
            self,
            msg = "(←  Close This Window to Begin)",
            x = 140, 
            y=self.exitButtonCrood["y"] + 7.4,
            color = "#C73618",
            fontSize = fontSize["sFont"]
        )

        self.tipsHeader = createMsgBox(
            self,
            msg = "Are you up for the sorting challenge?",

            x = self.winWidth/2,
            y = self.winHeight/2-150,
            color = None,
            fontSize = fontSize["lFont"]
        )

        self.tips1 = createMsgBox(
            self,
            msg = "There will be 5 numbers in the game.\nCan you sort it by Ascending order?\nType in your answer in the grey box.\n(Separate numbers with ',' (comma). See example below.)", 
            x = self.winWidth/2,
            y = self.winHeight/2-60,
            color = None,
            fontSize = fontSize["mFont"]
        )

        self.tips2 = createImg(
            self,
            "resources/img/sort_example1.png",
            x = self.winWidth/2,
            y = self.winHeight/2 +50
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
            
            # exit button onClick
            if targetX >= self.exitButtonCrood["x"] - self.exitButtonSize["radius"] and targetX <= self.exitButtonCrood["x"] + self.exitButtonSize["radius"] and targetY >= self.exitButtonCrood["y"] - self.exitButtonSize["radius"] and targetY <= self.exitButtonCrood["y"] + self.exitButtonSize["radius"]:
                self.closeWin()
                break


if __name__ == "__main__":
    hintsModule = hintsGui()
    hintsModule.run()
    