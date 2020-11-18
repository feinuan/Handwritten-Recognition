import math
import pymssql
from PyQt5.QtWidgets import QMessageBox

class LearningDB():

    def __init__(self):
        self.conn = pymssql.connect(host='127.0.0.1',user='sa',password='123456',database='PyLearningDB',charset='utf8')
        self.cursor = self.conn.cursor()
        self.sql = ''
        self.distance = 0.0
        self.conn.close()

    def learn_data(self, table, dim):
        '''
         学习数据，将数据存到对应的数据库
         table指定哪个表，dim是维度数组
        '''

        learn_result = False

        try:
            if table < 0 or table > 9:
                raise Exception("错误！table的值为%d！" % table)
            for num in dim:
                if num < 0:
                    raise Exception("错误！dim的值不能小于0！")

            self.conn = pymssql.connect(host='127.0.0.1',user='sa',password='123456',database='PyLearningDB',charset='utf8')
            self.cursor = self.conn.cursor()
            self.sql = 'insert into table%d values(%d, %d, %d, %d, %d, %d, %d, %d, %d)' % (
                table, dim[0], dim[1], dim[2], dim[3], dim[4], dim[5], dim[6], dim[7], dim[8])
            self.cursor.execute(self.sql)
            self.conn.commit()
            learn_result = True
        except Exception as ex_learn:
            self.conn.rollback()
            raise ex_learn
        finally:
            self.conn.close()
        return learn_result