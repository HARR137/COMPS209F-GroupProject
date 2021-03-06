import json

class Scoreboard:


    def __init__(self):
        self.loadFromFile()
        self.score = 0
        # pass

    # def getTotalScore(self):
    #     return (self.score["lm1Score"]+self.score["lm2Score"]+self.score["lm13core"]+self.score["lm4Score"])


    #scoreFromLm = {"lm1": 1000}
    def saveScore(self, scoreFromLm):
        #scoreFromLm  < need to determine this score come from which LM
        #after, update self.score dict
        #finally step save to json file saveToFile()
        # self.scoreList[scoreFromLm.keys()] = scoreFromLm.get("lm1")
        key = list( list ( scoreFromLm.values() ) [0].keys() )[0]

        self.loadFromFile()

        if key in self.score["latestScore"]: 
            self.score["latestScore"][key] = scoreFromLm["latestScore"][key]
            if self.score["bestScore"][key] == 0 or self.score["latestScore"][key] > self.score["bestScore"][key]: 
                self.score["bestScore"][key] = self.score["latestScore"][key]
                    
        self.saveToFile()


    def printScore(self):
        print(self.score)


    def saveToFile(self):
        print('Saving Scoreboard')
        with open("score.json", "w") as outfile: 
            json.dump(self.score, outfile)


    def loadFromFile(self):
        with open("score.json") as json_file:
            scoreboard = json.load(json_file)
            self.score = scoreboard


    def loadIndividualLmMarks(self, whichLm):
        self.loadFromFile()

        latest = self.score["latestScore"][whichLm]
        best = self.score["bestScore"][whichLm]
        latestAndBestScore = {"latest": latest, "best": best}
        return latestAndBestScore


    def resetScore(self): 
        reset = {"latestScore": {"lm1": 0, "lm2": 0, "lm3": 0, "lm4": 0}, "bestScore": {"lm1": 0, "lm2": 0, "lm3": 0, "lm4": 0}}
        print("Reseting Score")
        with open("score.json", "w") as outfile: 
            json.dump(reset, outfile)