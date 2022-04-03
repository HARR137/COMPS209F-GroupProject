from library.graphics import *
from gobal_var import fontSize, screenSize, lmGifSize
from common import createMsgBox, createImg, createRectangle

import learning_module.lm1.lm1_gui as lm1_gui
import learning_module.lm2.lm2_gui as lm2_gui
import learning_module.lm3.lm3_gui as lm3_gui
import learning_module.lm4.lm4_gui as lm4_gui


class MainGUI:
    def __init__(self):
        self.winWidth = 416
        self.winHeight = 896
        self.win = GraphWin('Home', screenSize["width"], screenSize["height"])

        row1X = 104
        col1Y = 150
        margin = 200

        self.lmCrood1 = {"x": row1X, "y": col1Y}
        self.lmCrood2 = {"x": row1X + margin, "y": col1Y}
        self.lmCrood3 = {"x": row1X, "y": col1Y + margin}
        self.lmCrood4 = {"x": row1X + margin, "y": col1Y + margin}

        #Homepage Header
        createMsgBox(self,
                     msg="Math Learning Module",
                     x=208,
                     y=20,
                     color=None,
                     fontSize=None)

        #Exit Main Program Button
        self.exitButtonSize = {"width": 50, "height": 25}
        self.exitButtonCrood = {"x": 5, "y": 5}
        self.exitButton = createRectangle(self,
                                          x=self.exitButtonCrood["x"],
                                          y=self.exitButtonCrood["y"],
                                          width=self.exitButtonSize["width"],
                                          height=self.exitButtonSize["height"])
        self.exitButtonText = createMsgBox(
            self,
            msg="EXIT",
            #+5 is a offset, since exitButton x,y crood is (5,5)
            x=self.exitButtonSize["width"] / 2 + 5,
            y=self.exitButtonSize["height"] / 2 + 5,
            color="black",
            fontSize=fontSize["sFont"])

        #Learning Moduel 1
        self.lm1MsgBox = createMsgBox(self,
                                      msg="Learning Module1",
                                      x=104,
                                      y=100,
                                      color="black",
                                      fontSize=fontSize["sFont"])
        self.lm1Img = createImg(self, "resources/img/aca1.png",
                                self.lmCrood1["x"], self.lmCrood1["y"])

        #Learning Moduel 2
        self.lm2MsgBox = createMsgBox(self,
                                      msg="Learning Module2",
                                      x=304,
                                      y=100,
                                      color=None,
                                      fontSize=fontSize["sFont"])
        self.lm2Img = createImg(self, "resources/img/aca2.png",
                                self.lmCrood2["x"], self.lmCrood2["y"])

        #Learning Moduel 3
        self.lm3MsgBox = createMsgBox(self,
                                      msg="Learning Module3",
                                      x=104,
                                      y=300,
                                      color=None,
                                      fontSize=fontSize["sFont"])
        self.lm3Img = createImg(self, "resources/img/aca3.png",
                                self.lmCrood3["x"], self.lmCrood3["y"])

        #Learning Moduel 4
        self.lm4MsgBox = createMsgBox(self,
                                      msg="Learning Module4",
                                      x=304,
                                      y=300,
                                      color=None,
                                      fontSize=fontSize["sFont"])
        self.lm4Img = createImg(self, "resources/img/aca4.png",
                                self.lmCrood4["x"], self.lmCrood4["y"])

        #learning module onclick handler:
        self.homeComponentOnClickHandler()

    def closeWin(self):
        self.win.close()

    def homeComponentOnClickHandler(self):
        print("Just get in homeComponentOnClickHandler")
        while True:
            checkMouse = self.win.getMouse()
            targetX = checkMouse.getX()
            targetY = checkMouse.getY()
            print("User click sth !")

            #Learning module 1 onLick handling condition
            if targetX >= self.lmCrood1["x"] - lmGifSize[
                    "width"] / 2 and targetX <= self.lmCrood1["x"] + lmGifSize[
                        "width"] / 2 and targetY >= self.lmCrood1[
                            "y"] - lmGifSize[
                                "height"] / 2 and targetY <= self.lmCrood1[
                                    "y"] + lmGifSize["height"] / 2:
                print("We click learning mocdule 1 !!")
                learn_module1 = lm1_gui.lm1GUI()
                learn_module1.run()

            #Learning module 2 onLick handling condition
            if targetX >= self.lmCrood2["x"] - lmGifSize[
                    "width"] / 2 and targetX <= self.lmCrood2["x"] + lmGifSize[
                        "width"] / 2 and targetY >= self.lmCrood2[
                            "y"] - lmGifSize[
                                "height"] / 2 and targetY <= self.lmCrood2[
                                    "y"] + lmGifSize["height"] / 2:
                print("We click learning mocdule 2 !!")
                learn_module2 = lm2_gui.lm2GUI()
                learn_module2.run()

            #Learning module 3 onLick handling condition
            if targetX >= self.lmCrood3["x"] - lmGifSize[
                    "width"] / 2 and targetX <= self.lmCrood3["x"] + lmGifSize[
                        "width"] / 2 and targetY >= self.lmCrood3[
                            "y"] - lmGifSize[
                                "height"] / 2 and targetY <= self.lmCrood3[
                                    "y"] + lmGifSize["height"] / 2:
                print("We click learning mocdule 3 !!")
                learn_module3 = lm3_gui.lm3GUI()
                learn_module3.run()

            #Learning module 4 onLick handling condition
            if targetX >= self.lmCrood4["x"] - lmGifSize[
                    "width"] / 2 and targetX <= self.lmCrood4["x"] + lmGifSize[
                        "width"] / 2 and targetY >= self.lmCrood4[
                            "y"] - lmGifSize[
                                "height"] / 2 and targetY <= self.lmCrood4[
                                    "y"] + lmGifSize["height"] / 2:
                print("We click learning mocdule 4 !!")
                learn_module4 = lm4_gui.lm4GUI()
                learn_module4.run()

            if targetX >= self.exitButtonCrood[
                    "x"] and targetX <= self.exitButtonCrood[
                        "x"] + self.exitButtonSize[
                            "width"] and targetY >= self.exitButtonCrood[
                                "y"] and targetY <= self.exitButtonCrood[
                                    "y"] + self.exitButtonSize["height"]:
                self.closeWin()
                break


if __name__ == "__main__":
    theGUI = MainGUI()
