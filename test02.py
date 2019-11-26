# 增删查改
from .User import User
import pymysql


def openDb():
    global db, cursor
    db = pymysql.connect("localhost", "root", "test1234", "pythontest", charset='utf8')
    cursor = db.cursor()


def closeDb():
    db.close()


# 按照用户id查询用户记录(输出相应内容，并返回查到的user对象)
def serarchDb(id):
    openDb()
    sql = "select * from user where id = " + str(id)
    rst = cursor.execute(sql)
    if rst == 0:
        print("查找失败")
        return None
    else:
        print("查找成功")
        data = cursor.fetchone()
        print(data)
        user1 = User(data[0], data[1], data[2], int(data[3]), data[4], data[5])
        return user1
    closeDb()

# 按照用户id删除用户记录
def deleteDb(id):
    openDb()
    sql = "delete from user where id = " + str(id)
    rst = cursor.execute(sql)
    if rst == 0:
        print("删除失败")
    else:
        print("删除成功")
    closeDb()


# 新增用户
def insertDb(user1):
    openDb()
    sql = "insert into user values('%d','%s','%s','%d','%s','%s')" % (
        user1.id, user1.username, user1.birth_data, user1.money, user1.father, user1.mother)
    # "INSERT INTO mytb(title,keywd) VALUES('%s','%s')"%(x,y)
    cursor.execute(sql)
    db.commit()
    closeDb()


# 更新用户信息
def updateDb(user1):
    openDb()
    sql = "update user set username = '%s', money='%d' where id='%d'" % (user1.username, user1.money, user1.id)
    # update user set username='C', money=9999 where id=5;
    rst = cursor.execute(sql)
    if rst == 0:
        print("更新失败")
    else:
        print("更新成功")
    closeDb()


#  测试数据
# testuser = serarchDb(5)
# testuser.set_username('C')
# testuser.set_money(9088)
# # print(testuser.id, testuser.username, testuser.money, testuser.father, testuser.mother)
# updateDb(testuser)

# user1 = User(5, "c", "1111-03-11", 10000, father='A', mother='a')
# insertDb(user1)
# user2 = User(0, "d", "1111-03-11", 10000, 'A', 'a')  # 自增键id设置为0，新增时即可实现自增
# insertDb(user2)

# user2 = User(1, "A", "1111-03-11", 10000, father=None, mother=None)
# user3 = User(2, "a", "1111-03-11", 10000, father=None, mother=None)
# user1 = User(3, "B", "1111-03-11", 10000, user2, user3)
# user1.dayin()
# user1.father.dayin()
