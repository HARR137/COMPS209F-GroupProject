from library.graphics import Text, Point, Image, Rectangle, Circle


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
    newRectangle.setFill(setting["fillColor"])
    newRectangle.setOutline(setting["outlineColor"])
    newRectangle.draw(self.win)
    return newRectangle


def createCircle(self, **setting):
    newCircle = Circle(Point(setting["x"], setting["y"]), setting["radius"])
    newCircle.setFill(setting["fillColor"])
    newCircle.setOutline(setting["outlineColor"])
    newCircle.draw(self.win)
    return newCircle
    
