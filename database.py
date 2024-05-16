import psycopg2

class Database:
    def __init__(self, user, password, host, port, dbname, autoinc):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname
        self.autoinc = autoinc

        self.initiate()

    def connect(self):
        return psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.dbname)

    def initiate(self):
        conn = self.connect()
        cursor = conn.cursor()

        query = f"""
        CREATE TABLE IF NOT EXISTS entity(id {"SERIAL" if self.autoinc else "BIGINT"} PRIMARY KEY, score INT, active BOOLEAN DEFAULT False, lastcheck BIGINT);
        """

        cursor.execute(query)
        conn.commit()
        conn.close()
