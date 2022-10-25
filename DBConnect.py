import pymysql


class DB:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='headset', password='headset', port=3306,  # sql테이블 읽어오기
                                    db='headset_db', charset='utf8')

    def excute(self, qry, args=None):
        cursor = self.conn.cursor()
        print(cursor)
        cursor.execute(qry, args)
        self.conn.commit()
        cursor.close()

    def execute_one(self, qry, *argv):
        cursor = self.conn.cursor()
        self.conn.connect()
        cursor.execute(qry)
        data = cursor.fetchone()
        cursor.close()
        return data

    def execute_all(self, qry, *argv):
        cursor = self.conn.cursor()
        self.conn.connect()
        cursor.execute(qry)
        data = cursor.fetchall()
        cursor.close()
        return data
