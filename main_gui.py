from library.graphics import *
from gobal_var import fontSize, screenSize, lmGifSize
from common import createMsgBox, createImg, createCircle

import learning_module.lm1.lm1_gui as lm1_gui
import learning_module.lm2.lm2_gui as lm2_gui
import learning_module.lm3.lm3_gui as lm3_gui
import learning_module.lm4.lm4_gui as lm4_gui

import scoreboard as sb

class MainGUI:
    def __init__(self):

        self.scoreboard = sb.Scoreboard()
        self.scoreboard.printScore()

        self.winWidth = 416
        self.winHeight = 896
        self.win = GraphWin('Home', screenSize["width"], screenSize["height"])
        self.win.setBackground("black")

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
                     color="white",
                     fontSize=fontSize["xlFont"])  

        # self.headerCrood = {"x": 208, "y": 30}    
        # self.headerImg = createImg(self, "resources/img/m-l-m.png",
        #                         self.headerCrood["x"], self.headerCrood["y"])   

        #Exit Main Program Button
        self.exitButtonSize = {"radius": 25}
        self.exitButtonCrood = {"x": 5, "y": 5}
        self.exitButton = createCircle(self,
                                          x=self.exitButtonCrood["x"],
                                          y=self.exitButtonCrood["y"],
                                          radius=self.exitButtonSize["radius"], 
                                          fillColor = "red", 
                                          outlineColor = "red")
        self.exitButtonText = createMsgBox(
            self,
            msg="x",
            x=self.exitButtonCrood["x"] + 7, 
            y=self.exitButtonCrood["y"] + 7, 
            color="white",
            fontSize=fontSize["mFont"])

        #Learning Moduel 1
        self.lm1MsgBox = createMsgBox(self,
                                      msg="Learning Module 1",
                                      x=104,
                                      y=100,
                                      color="white",
                                      fontSize=fontSize["mFont"])
        self.lm1Img = createImg(self, "resources/img/o-or-e.png",
                                self.lmCrood1["x"], self.lmCrood1["y"])
        self.lm1LatestScoreBoard = createMsgBox(self, 
                                            msg = "Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm1")["latest"]),
                                            x = 104, 
                                            y = 200, 
                                            color = "pink", 
                                            fontSize=fontSize["sFont"])
        self.lm1BestScoreBoard = createMsgBox(self, 
                                            msg = "Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm1")["best"]), 
                                            x = 104, 
                                            y = 215, 
                                            color = "orange", 
                                            fontSize=fontSize["sFont"])

        #Learning Moduel 2
        self.lm2MsgBox = createMsgBox(self,
                                      msg="Learning Module 2",
                                      x=304,
                                      y=100,
                                      color="white",
                                      fontSize=fontSize["mFont"])
        self.lm2Img = createImg(self, "resources/img/l-or-s.png",
                                self.lmCrood2["x"], self.lmCrood2["y"])
        self.lm2LatestScoreBoard = createMsgBox(self, 
                                            msg = "Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm2")["latest"]),
                                            x = 304, 
                                            y = 200, 
                                            color = "pink", 
                                            fontSize=fontSize["sFont"])
        self.lm2BestScoreBoard = createMsgBox(self, 
                                            msg = "Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm2")["best"]), 
                                            x = 304, 
                                            y = 215, 
                                            color = "orange", 
                                            fontSize=fontSize["sFont"])

        #Learning Moduel 3
        self.lm3MsgBox = createMsgBox(self,
                                      msg="Learning Module 3",
                                      x=104,
                                      y=300,
                                      color="white",
                                      fontSize=fontSize["mFont"])
        self.lm3Img = createImg(self, "resources/img/a-s-m-d.png",
                                self.lmCrood3["x"], self.lmCrood3["y"])
        self.lm3LatestScoreBoard = createMsgBox(self, 
                                            msg = "Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm3")["latest"]),
                                            x = 104, 
                                            y = 400, 
                                            color = "pink", 
                                            fontSize=fontSize["sFont"])
        self.lm3BestScoreBoard = createMsgBox(self, 
                                            msg = "Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm3")["best"]), 
                                            x = 104, 
                                            y = 415, 
                                            color = "orange", 
                                            fontSize=fontSize["sFont"])

        #Learning Moduel 4
        self.lm4MsgBox = createMsgBox(self,
                                      msg="Learning Module 4",
                                      x=304,
                                      y=300,
                                      color="white",
                                      fontSize=fontSize["mFont"])
        self.lm4Img = createImg(self, "resources/img/n-o.png",
                                self.lmCrood4["x"], self.lmCrood4["y"])
        self.lm4LatestScoreBoard = createMsgBox(self, 
                                            msg = "Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm4")["latest"]),
                                            x = 304, 
                                            y = 400, 
                                            color = "pink", 
                                            fontSize=fontSize["sFont"])
        self.lm4BestScoreBoard = createMsgBox(self, 
                                            msg = "Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm4")["best"]), 
                                            x = 304, 
                                            y = 415, 
                                            color = "orange", 
                                            fontSize=fontSize["sFont"])

        self.resetButtonSize = {"radius": 35}
        self.resetButtonCrood = {"x": 208, "y": 650}
        self.resetButton = createCircle(self,
                                          x=self.resetButtonCrood["x"],
                                          y=self.resetButtonCrood["y"],
                                          radius=self.resetButtonSize["radius"], 
                                          fillColor = "green", 
                                          outlineColor = "green")
        self.resetButtonText = createMsgBox(
            self,
            msg="RESET\nALL SCORE",
            x=self.resetButtonCrood["x"],
            y=self.resetButtonCrood["y"],
            color="white",
            fontSize=fontSize["sFont"])

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
            print("User click X: ", targetX, "and Y :", targetY )

            #Learning module 1 onLick handling condition
            if targetX >= self.lmCrood1["x"] - lmGifSize["width"] / 2 and targetX <= self.lmCrood1["x"] + lmGifSize["width"] / 2 and targetY >= self.lmCrood1["y"] - lmGifSize["height"] / 2 and targetY <= self.lmCrood1["y"] + lmGifSize["height"] / 2:
                print("We click learning mocdule 1 !!")
                learn_module1 = lm1_gui.lm1GUI()
                self.scoreboard.saveScore( {"latestScore": {"lm1": learn_module1.run()}} )
                self.lm1LatestScoreBoard.setText("Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm1")["latest"]))
                self.lm1BestScoreBoard.setText("Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm1")["best"]))
                # self.scoreboard.loadFromFile()

            #Learning module 2 onLick handling condition
            if targetX >= self.lmCrood2["x"] - lmGifSize["width"] / 2 and targetX <= self.lmCrood2["x"] + lmGifSize["width"] / 2 and targetY >= self.lmCrood2["y"] - lmGifSize["height"] / 2 and targetY <= self.lmCrood2["y"] + lmGifSize["height"] / 2:
                print("We click learning mocdule 2 !!")
                learn_module2 = lm2_gui.lm2GUI()
                self.scoreboard.saveScore( {"latestScore": {"lm2": learn_module2.run()}} )
                self.lm2LatestScoreBoard.setText("Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm2")["latest"]))
                self.lm2BestScoreBoard.setText("Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm2")["best"]))

            #Learning module 3 onLick handling condition
            if targetX >= self.lmCrood3["x"] - lmGifSize["width"] / 2 and targetX <= self.lmCrood3["x"] + lmGifSize["width"] / 2 and targetY >= self.lmCrood3["y"] - lmGifSize["height"] / 2 and targetY <= self.lmCrood3["y"] + lmGifSize["height"] / 2:
                print("We click learning mocdule 3 !!")
                learn_module3 = lm3_gui.lm3GUI()
                self.scoreboard.saveScore( {"latestScore": {"lm3": learn_module3.run()}} )
                self.lm3LatestScoreBoard.setText("Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm3")["latest"]))
                self.lm3BestScoreBoard.setText("Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm3")["best"]))

            #Learning module 4 onLick handling condition
            if targetX >= self.lmCrood4["x"] - lmGifSize["width"] / 2 and targetX <= self.lmCrood4["x"] + lmGifSize["width"] / 2 and targetY >= self.lmCrood4["y"] - lmGifSize["height"] / 2 and targetY <= self.lmCrood4["y"] + lmGifSize["height"] / 2:
                print("We click learning mocdule 4 !!")
                learn_module4 = lm4_gui.lm4GUI()
                self.scoreboard.saveScore( {"latestScore": {"lm4": learn_module4.run()}} )
                self.lm4LatestScoreBoard.setText("Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm4")["latest"]))
                self.lm4BestScoreBoard.setText("Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm4")["best"]))

            #resetButton onLick handling condition
            if targetX >= self.resetButtonCrood["x"] - self.resetButtonSize["radius"] and targetX <= self.resetButtonCrood["x"] + self.resetButtonSize["radius"] and targetY >= self.resetButtonCrood["y"] - self.resetButtonSize["radius"] and targetY <= self.resetButtonCrood["y"] + self.resetButtonSize["radius"]:
                self.scoreboard.resetScore()
                self.lm1LatestScoreBoard.setText("Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm1")["latest"]))
                self.lm1BestScoreBoard.setText("Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm1")["best"]))
                self.lm2LatestScoreBoard.setText("Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm2")["latest"]))
                self.lm2BestScoreBoard.setText("Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm2")["best"]))
                self.lm3LatestScoreBoard.setText("Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm3")["latest"]))
                self.lm3BestScoreBoard.setText("Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm3")["best"]))
                self.lm4LatestScoreBoard.setText("Latest Score: " + str(self.scoreboard.loadIndividualLmMarks("lm4")["latest"]))
                self.lm4BestScoreBoard.setText("Best Score: " + str(self.scoreboard.loadIndividualLmMarks("lm4")["best"]))

            #exitButton onLick handling condition
            if targetX >= self.exitButtonCrood["x"] - self.resetButtonSize["radius"] and targetX <= self.exitButtonCrood["x"] + self.exitButtonSize["radius"] and targetY >= self.exitButtonCrood["y"] - self.resetButtonSize["radius"] and targetY <= self.exitButtonCrood["y"] + self.exitButtonSize["radius"]:
                self.closeWin()
                break


if __name__ == "__main__":
    theGUI = MainGUI()
