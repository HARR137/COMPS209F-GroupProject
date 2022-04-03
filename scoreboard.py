import json

class Scoreboard:
    def __init__(self):
        self.loadFromFile()
            # self.totalScore = 

    def getTotalScore(self):
        return (self.score["lm1Score"]+self.score["lm2Score"]+self.score["lm13core"]+self.score["lm4Score"])

    def saveScore(self, scoreFromLm):
        #scoreFromLm  < need to determine this score come from which LM
        #after, update self.score dict
        #finally step save to json file saveToFile()
        pass       

    def printScore(self):
        print(self.score)

    def saveToFile(self, filename):
        print('Saving Scorebo.ard')

    def loadFromFile(self, filename):
        with open("score.json") as json_file:
            scoreboard = json.load(json_file)
            self.score = scoreboard