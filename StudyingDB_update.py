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
    def __get_data(self, table, test_data):
        '''
         取出table表中所有数据
         并与测试数据进行比较，返回最小值
         如果table表中无数据，则全部取0
        '''

        try:
            if table < 0 or table > 9:
                raise Exception("错误！table的值不能为%d！" % table)
            self.conn = pymssql.connect(host='127.0.0.1',
                                        user='sa',
                                        password='123456',
                                        database='PyLearningDB',
                                        charset='utf8')
            self.cursor = self.conn.cursor()
            self.sql='select * from table%d' %table
            self.cursor.execute(self.sql)
            receive_sql = self.cursor.fetchall()

            if not receive_sql:
                new_receive_sql = [(0, 0, 0, 0, 0, 0, 0, 0, 0)]
            else:
                new_receive_sql = receive_sql
        finally:
            self.conn.close()
        # 计算最小值
        dim_data = []
        for receive_data in new_receive_sql:
            dim_data.append(self.__distance_data(test_data, receive_data))
        # 返回dimData中最小值
        return min(dim_data)