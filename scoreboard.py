import json

class Scoreboard:
    def __init__(self):
        with open("score.json") as json_file:
            scoreboard = json.load(json_file)
            self.score = scoreboard
            # self.totalScore = 

    def getScore(self):
        return self.score

    def getTotalScore(self):
        return (self.score["lm1Score"]+self.score["lm2Score"]+self.score["lm13core"]+self.score["lm4Score"])/4

    def printScore(self):
        print('Testing Scoreboard')

    def saveToFile(self, filename):
        print('Saving Scorebo.ard')        

    def loadFromFile(self, filename):
        print('Loading Scoreboard')  