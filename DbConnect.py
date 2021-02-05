import pymysql as mysql


class Data:

    def __init__(self):
        self.con = mysql.connect("localhost", "root", "root", "mysql")
        self.cursor = self.con.cursor()

    def disconnect(self):
        self.con.close()

    def executeSQL(self, sql):
        self.cursor.execute(sql)
        self.con.commit()

    def getdata(self, sql):
        self.cursor.execute(sql)
        return self.cursor
