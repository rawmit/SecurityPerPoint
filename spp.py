from methods import Methods

class SPP(Methods):
    def __init__(
            self,
            PgDbName:str,
            PgDbUser:str,
            PgDbPassword:str,
            PgDbHost:str='localhost',
            PgDbPort:int=5432,
            AutoFillId:bool=True,
            HowMuchScorePerTick:int=5,
            HowMuchSecondsForTick:int=1,
            MaxScorePerUser:int=500,
            UserDefaultScore:int=50,
    ):
        self.AutoFillId = AutoFillId
        self.HowMuchScorePerTick = HowMuchScorePerTick
        self.HowMuchSecondsForTick = HowMuchSecondsForTick
        self.MaxScorePerUser = MaxScorePerUser
        self.UserDefaultScore = UserDefaultScore

        super().__init__(dbhost=PgDbHost, dbpass=PgDbPassword, dbport=PgDbPort, dbuser=PgDbUser, dbname=PgDbName,
                autoinc=AutoFillId, pertick=HowMuchScorePerTick, secfortick=HowMuchSecondsForTick, maxscoreuser=MaxScorePerUser)

    def createEntity(self, id:int=None, score:int=None):
        if not self.AutoFillId and not id:
            raise ValueError("Please enter a valid integer value for id")

        return super().createEntity(self.UserDefaultScore if score is None else score, id)

    def getEntity(self, id:int):
        return super().getEntity(id)

    def removeEntity(self, id:int):
        return super().removeEntity(id)

    def increaseEntityScore(self, id:int, value:int):
        return super().increaseEntityScore(id, value)

    def decreaseEntityScore(self, id:int, value:int):
        return super().decreaseEntityScore(id, value)

    def setEntityScore(self, id:int, value:int):
        return super().setEntityScore(id, value)