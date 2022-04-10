from library.graphics import *
from gobal_var import fontSize
from common import createMsgBox, createImg, createRectangle, createCircle

class hintsGui():
    def __init__(self):
        self.winWidth = 600
        self.winHeight = 500
        self.win = 0

        #ExitButton
        self.exitButtonSize= { "width": 50, "height": 25 }
        self.exitButtonCrood = { "x": 5, "y": 5 }
        
        
    def run(self):
        self.win = GraphWin('Learning Module 4 - How to play this game?', self.winWidth, self.winHeight)
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

        self.exitToStartTips = createMsgBox(
            self,
            msg = "←  Close This Window to Begin :)",
            x = 140, 
            y=self.exitButtonCrood["y"] + 7.4,
            color = "#C73618",
            fontSize = fontSize["mFont"]
        )

        self.tipsHeader = createMsgBox(
            self,
            msg = "Are you up for the sorting challenge?",

            x = self.winWidth/2,
            y = self.winHeight/2-150,
            color = None,
            fontSize = fontSize["xlFont"]
        )

        self.tips1 = createMsgBox(
            self,
            msg = "There will be 5 numbers in the game.\nCan you sort it by Ascending order?\nType in your answer in the grey box.\n(Separate numbers with ',' (comma). See example below.)",

            x = self.winWidth/2,
            y = self.winHeight/2-60,
            color = None,
            fontSize = fontSize["lFont"]
        )
        # self.tips2 = createMsgBox(
        #     self,
        #     msg = "Can you sort it by Ascending order?",

        #     x = self.winWidth/2,
        #     y = self.winHeight/2-60,
        #     color = None,
        #     fontSize = fontSize["lFont"]
        # )
        # self.tips3 = createMsgBox(
        #     self,
        #     msg = "Type in your answer in the grey box.",

        #     x = self.winWidth/2,
        #     y = self.winHeight/2-40,
        #     color = None,
        #     fontSize = fontSize["lFont"]
        # )
        # self.tips4 = createMsgBox(
        #     self,
        #     msg = "(Separate numbers with ',' (comma). See example below.)",
        #     x = self.winWidth/2,
        #     y = self.winHeight/2-20,
        #     color = None,
        #     fontSize = fontSize["lFont"]
        # )

        self.tips5 = createImg(
            self,
            "resources/img/sort_example1.png",
            x = self.winWidth/2,
            y = self.winHeight/2 +50
        )



        # self.exitAndNoTipsButton = createRectangle(
        #     self,
        #     starting_x = self.nextButtonCrood["starting_x"],
        #     starting_y = self.nextButtonCrood["starting_y"], 
        #     ending_x = self.nextButtonCrood["ending_x"],
        #     ending_y = self.nextButtonCrood["ending_y"], 
        #     fillColor = None, 
        #     outlineColor = None
        # )
        # self.exitAndNoTipsButtonText = createMsgBox(
        #     self,
        #     msg = "EXIT (Don't display tips again)",

        #     x = self.exitButtonSize["width"]/2+5,
        #     y = self.exitButtonSize["height"]/2+5,
        #     color = "black",
        #     fontSize = fontSize["sFont"]
        # )
        


        self.lm1OnClickHandler(self.win)
        return 1

    def closeWin(self):
        self.win.close()


    def lm1OnClickHandler(self, win):
        while True:
            checkMouse = win.getMouse()
            targetX = checkMouse.getX()
            targetY = checkMouse.getY()
            
            # exitButton onClick
            if targetX >= self.exitButtonCrood["x"] - self.exitButtonSize["radius"] and targetX <= self.exitButtonCrood["x"] + self.exitButtonSize["radius"] and targetY >= self.exitButtonCrood["y"] - self.exitButtonSize["radius"] and targetY <= self.exitButtonCrood["y"] + self.exitButtonSize["radius"]:
                self.closeWin()
                break

if __name__ == "__main__":
    hintsModule = hintsGui()
    hintsModule.run()