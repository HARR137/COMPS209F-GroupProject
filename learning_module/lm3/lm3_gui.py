from library.graphics import *
from gobal_var import fontSize
from common import createMsgBox, createRectangle,createInputBox, createCircle
import random


class lm3GUI():
    def __init__(self):
        # self.expression = ["+", "-", "*", "/"]
        self.expression = ["+", "-"]
        self.gameTurns = 5
        self.questions = []
        self.score = 0
        self.enterButtonClicked = False
        pass
        
        
    def run(self):
        self.winWidth = 700
        self.winHeight = 700

        self.win = GraphWin('Learning Module 3 - Add and Substract', self.winWidth, self.winHeight)

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

        self.enterButtonCrood = { "starting_x": 215, "starting_y": 380, "ending_x": 315, "ending_y": 410 }
        self.enterTextCrood = { "x": 265, "y": 395 }
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


        self.nextButtonCrood = { "starting_x": 385, "starting_y": 380, "ending_x": 485, "ending_y": 410 }
        self.nextTextCrood = { "x": 435, "y": 395 }
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

        self.inputBox = createInputBox(self, x=350, y=300, length=20)

        
        self.generateQuestions()
        self.lm1OnClickHandler(self.win)
        return self.score

    def closeWin(self):
        self.win.close()

    def checkAnswer(self, queston):
        userInput = int( self.inputBox.getText())

        if userInput == eval(queston):
            self.score = self.score+1 
            return True
        else:
            return False

    def mergeTwoList(self, list1, list2, position):
        for i, element in enumerate(list2, 1):
            list1.insert(i * position - 1, element)
        return list1

    def generateQuestions(self):
        
        lostOfNums = []
        temp = []
        listOfSymbol = []
        tempSymbol = []

        for turns in range(self.gameTurns):
            howManynumberInQuestion = ( random.randint(2,4) )
            # print("howManynumberInQuestion : ", howManynumberInQuestion)
            for index, number in enumerate(range(howManynumberInQuestion)):
                temp.append(random.randint(1,9))
                if index != howManynumberInQuestion-1:
                    tempSymbol.append(self.expression[random.randint(0, 1)] )
            lostOfNums.append(temp)
            temp = []
            listOfSymbol.append(tempSymbol)
            tempSymbol = []

        print(lostOfNums)
        print(listOfSymbol)

        tempQuestions = []
        for index, item in enumerate(lostOfNums):
            temp = self.mergeTwoList(lostOfNums[index], listOfSymbol[index] ,2)
            tempQuestions.append(temp)
            

        for index, question in enumerate(tempQuestions):
            self.questions.append("".join(map(str, question)))


    def drawQuestions(self, index):
        print(self.questions)
        self.currentTitle =  createMsgBox(
                                    self,
                                    msg="Question " + str(index+1) + " / 5",
                                    x=350 ,
                                    y=100,
                                    color="black",
                                    fontSize=fontSize["xxlFont"]
                                )

        self.currentQuestion =  createMsgBox(
                                    self,
                                    msg=self.questions[index],
                                    x=350 ,
                                    y=150,
                                    color="black",
                                    fontSize=fontSize["xxlFont"]
                                )
            

    def lm1OnClickHandler(self, win):
        counter = 0
        finishAnswerQuestion = True
        while True:
            
            if finishAnswerQuestion:
                self.drawQuestions(counter)
                finishAnswerQuestion = False
                print("finishAnswerQuestion", finishAnswerQuestion)
            checkMouse = win.getMouse()
            targetX = checkMouse.getX()
            targetY = checkMouse.getY()
            

            resultMessage = lambda ans: "Very good! It's correct!" if (ans) else "Wrong answer... Practice makes perfect!"
            resultMessageColor = lambda ans: "green" if (ans) else "red"

            # enterButton onClick
            if targetX >= self.enterButtonCrood["starting_x"] and targetX <= self.enterButtonCrood["ending_x"] and targetY >= self.enterButtonCrood["starting_y"] and targetY <= self.enterButtonCrood["ending_y"]:
                self.enterButtonClicked = True
                checkedAnswer = self.checkAnswer(self.questions[counter])
                self.correctOrNot = createMsgBox(
                            self,
                            msg=resultMessage(checkedAnswer),
                            x=350 ,
                            y=250,
                            color=resultMessageColor(checkedAnswer),
                            fontSize=fontSize["lFont"]
                            )
                print(checkedAnswer)

            # nextButton onClick
            if self.enterButtonClicked == True and targetX >= self.nextButtonCrood["starting_x"] and targetX <= self.nextButtonCrood["ending_x"] and targetY >= self.nextButtonCrood["starting_y"] and targetY <= self.nextButtonCrood["ending_y"]:
                finishAnswerQuestion = True
                self.currentTitle.undraw()
                self.currentQuestion.undraw()
                self.correctOrNot.undraw()
                self.inputBox.setText("")
                counter += 1
                if counter == 5:
                    self.closeWin()
                    break
      
            # exitButton onClick
            if targetX >= self.exitButtonCrood["x"] - self.exitButtonSize["radius"] and targetX <= self.exitButtonCrood["x"] + self.exitButtonSize["radius"] and targetY >= self.exitButtonCrood["y"] - self.exitButtonSize["radius"] and targetY <= self.exitButtonCrood["y"] + self.exitButtonSize["radius"]:
                self.closeWin()
                break
                    

if __name__ == "__main__":
    lm3GUI = lm3GUI()
    lm3GUI.run()