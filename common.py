from library.graphics import Text, Point, Image, Rectangle

def createMsgBox(self, **setting):
    theMsgBox = Text(Point(setting["x"], setting["y"]), setting["msg"])
    
    if setting["color"] != None:
        theMsgBox.setTextColor(setting["color"])
    if setting["fontSize"] != None:
        theMsgBox.setSize( setting["fontSize"] )
    else:
        theMsgBox.setSize(18)
        
    theMsgBox.draw(self.win)
    return theMsgBox



def createImg(self, imgName, x, y):
    newImg = Image(Point(x,y), imgName)
    newImg.draw(self.win)
    return newImg


def createRectangle(self, **setting):
    # x, y, width, height
    newRectangle = Rectangle(Point(setting["x"], setting["y"]), Point(setting["width"], setting["height"]))
    newRectangle.draw(self.win)
    return newRectangle


def createExitButton(self):
    #Exit Main Program Button
        # self.exitButtonSize= { "width": 50, "height": 25 }
        # self.exitButtonCrood = { "x": 5, "y": 5 }
        # self.exitButton = createRectangle(
        #     self,
        #     x = self.exitButtonCrood["x"],
        #     y = self.exitButtonCrood["y"],
        #     width = self.exitButtonSize["width"],
        #     height = self.exitButtonSize["height"]
        # )
        
        #Exit Main Program Button
        exitButtonSize= { "width": 50, "height": 25 }
        exitButtonCrood = { "x": 5, "y": 5 }
        exitButton = createRectangle(
            self,
            x = exitButtonCrood["x"],
            y = exitButtonCrood["y"],
            width = exitButtonSize["width"],
            height = self.exitButtonSize["height"]
        )

# def buttonOnClickHandler(self, element, callBackFunc):
