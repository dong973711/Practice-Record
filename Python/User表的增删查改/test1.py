# 测试操作
import pymysql

# user1 = User(2, "dong", "1997-02-26", 10000, father=None, mother=None)
# user2 = User(3, "d", "1997-02-26", 10000, father=None, mother=None)
# user = User(1, "donghu", "1997-02-26", 10000, father=user1, mother=user2)
# user.dayin()

# 打开数据库
db = pymysql.connect("localhost", "root", "test1234", "pythontest", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute执行sql语句
cursor.execute("select * from user")
data = cursor.fetchall()
print(data)
db.close()
