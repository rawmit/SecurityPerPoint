import time
from spptypes import Entity
from database import Database

class Methods(Database):
    def __init__(self, dbhost, dbuser, dbpass, dbport, dbname, autoinc, pertick, secfortick, maxscoreuser):
        super().__init__(user=dbuser, password=dbpass, port=dbport, host=dbhost, dbname=dbname, autoinc=autoinc)
        self.pertick = pertick
        self.secfortick = secfortick
        self.maxscoreuser = maxscoreuser

    def createEntity(self, score, id=None):
        conn = self.connect()
        cursor = conn.cursor()

        timeCreated = time.time()
        if self.autoinc:
            cursor.execute("INSERT INTO entity(score, lastcheck) VALUES(%s, %s) ; SELECT lastval();", (score, timeCreated))
            id, = cursor.fetchone()
        else:
            cursor.execute("INSERT INTO entity(id, score, lastcheck) VALUES(%s, %s, %s)", (score, id, timeCreated))
        conn.commit()
        conn.close()
        return Entity(id, score, False, timeCreated)

    def getEntity(self, id):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM entity WHERE id = %s", (id, ))
        result = cursor.fetchone()
        conn.close()
        if result:
            entity = Entity(result[0], result[1], result[2], result[3])
            entity = self.__updateEntityCheck(entity)
            return entity

    def __updateEntityCheck(self, entity):
        conn = self.connect()
        cursor = conn.cursor()
        spendtime = time.time() - entity.lastcheck
        if spendtime >= self.secfortick:
            ticks = int(spendtime / self.secfortick)
            newscore = entity.score + ticks*self.pertick
            if newscore <= self.maxscoreuser:
                cursor.execute("UPDATE entity SET lastcheck = %s, score = %s WHERE id = %s", (entity.lastcheck + ticks * self.secfortick, newscore, entity.id))
            else:
                newscore = self.maxscoreuser
                cursor.execute("UPDATE entity SET lastcheck = %s, score = %s WHERE id = %s", (time.time(), newscore, entity.id))
            cursor.execute("SELECT * FROM entity WHERE id = %s", (entity.id, ))
            entity = cursor.fetchone()
            entity = Entity(entity[0], entity[1], entity[2], entity[3])
            conn.commit()
        conn.close()
        return entity

    def removeEntity(self, id):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM entity WHERE id = %s", (id, ))

        conn.commit()
        conn.close()

    def increaseEntityScore(self, id, value):
        entity = self.getEntity(id)
        entity = self.__updateEntityCheck(entity)

        if entity.score + value > self.maxscoreuser:
            value = self.maxscoreuser - entity.score

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("UPDATE entity SET score = score + %s WHERE id = %s", (value, id))

        conn.commit()
        conn.close()

        return entity.score + value

    def decreaseEntityScore(self, id, value):
        entity = self.getEntity(id)
        entity = self.__updateEntityCheck(entity)

        if entity.score - value < 0:
            return None

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("UPDATE entity SET score = score - %s WHERE id = %s", (value, id))

        conn.commit()
        conn.close()

        return entity.score - value

    def setEntityScore(self, id, value):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("UPDATE entity SET score = %s WHERE id = %s", (value, id))

        conn.commit()
        conn.close()



