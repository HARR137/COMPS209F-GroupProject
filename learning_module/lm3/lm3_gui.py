from library.graphics import *
from gobal_var import fontSize
from common import createMsgBox, createImg, createRectangle,createInputBox
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
        self.winWidth = 500
        self.winHeight = 500

        #ExitButton
        self.exitButtonSize= { "width": 50, "height": 25 }
        self.exitButtonCrood = { "x": 5, "y": 5 }

        self.win = GraphWin('Learning Module 3', self.winWidth, self.winHeight)
        self.exitButton = createRectangle(
            self,
            starting_x = self.exitButtonCrood["x"],
            starting_y = self.exitButtonCrood["y"],
            ending_x = self.exitButtonSize["width"],
            ending_y = self.exitButtonSize["height"], 
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

        self.inputBox = createInputBox(self, x=250, y=300, length=20)

        
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
                                    msg="Question" + str(index+1),
                                    x=250 ,
                                    y=100,
                                    color="black",
                                    fontSize=fontSize["xxlFont"]
                                )

        self.currentQuestion =  createMsgBox(
                                    self,
                                    msg=self.questions[index],
                                    x=250 ,
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

            #enterButton onClick
            if targetX >= self.enterButtonCrood["starting_x"] and targetX <= self.enterButtonCrood["ending_x"] and targetY >= self.enterButtonCrood["starting_y"] and targetY <= self.enterButtonCrood["ending_y"]:
                self.enterButtonClicked = True
                checkedAnswer = self.checkAnswer(self.questions[counter])
                self.correctOrNot = createMsgBox(
                            self,
                            msg=resultMessage(checkedAnswer),
                            x=250 ,
                            y=250,
                            color=resultMessageColor(checkedAnswer),
                            fontSize=fontSize["lFont"]
                            )
                self.inputBox.setText("")
                print(checkedAnswer)

            # nextButton onClick
            if self.enterButtonClicked == True and targetX >= self.nextButtonCrood["starting_x"] and targetX <= self.nextButtonCrood["ending_x"] and targetY >= self.nextButtonCrood["starting_y"] and targetY <= self.nextButtonCrood["ending_y"]:
                finishAnswerQuestion = True
                self.currentTitle.undraw()
                self.currentQuestion.undraw()
                self.correctOrNot.undraw()
                counter += 1
                if counter == 4:
                    self.closeWin()
                    break
      
            #exitButton onClick
            if targetX >= self.exitButtonCrood["x"]  and targetX <= self.exitButtonCrood["x"] + self.exitButtonSize["width"] and targetY >= self.exitButtonCrood["y"] and targetY <= self.exitButtonCrood["y"] + self.exitButtonSize["height"] :
                self.closeWin()
                break
                    

if __name__ == "__main__":
    lm3GUI = lm3GUI()
    lm3GUI.run()