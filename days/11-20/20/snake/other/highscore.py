import os.path

from libraries.FileIO import hson
class handler:
    def check(self, score):
        home = self.players[self.user]
        if(home < score):
            self.players[self.user] = score
    def getHighscore(self):
        return self.players[self.user]

    def save(self):
        hson.hson(self.path, self.players).save()

    def getScore(self):
        try:
            self.players[self.user]
        except:
            self.players[self.user] = 0

    def __init__(self, path, username):
        self.user = username
        self.path = path
        self.players = hson.hson(self.path, {}).get()
        self.getScore()


# handler(f"{os.path.dirname(__file__)}/Highscores.json", "BBC")