# 查询父辈信息 直接查数据库，把所有信息查出来，内存里面操作
from Practice_Recode.UserTest.test02 import *
import pymysql


def openDb():
    global db, cursor
    db = pymysql.connect("localhost", "root", "test1234", "pythontest", charset='utf8')
    cursor = db.cursor()


def closeDb():
    db.close()


# 查找所有用户id,并返回ids,users
def serarchDbAll():
    openDb()
    ids = []
    users = []
    sql = "select * from user"
    rst = cursor.execute(sql)
    if rst == 0:
        print("查找失败")
        return None
    else:
        print("查找成功")
        data = cursor.fetchall()
        for i in range(len(data)):
            user = User(0, "", "", 0, "", "")
            user.id = data[i][0]
            user.username = data[i][1]
            user.birth_data = data[i][2]
            user.money = data[i][3]
            user.father = data[i][4]
            user.money = data[i][5]
            users.append(user)
            ids.append(data[i][0])
    closeDb()
    return ids, users


# 根据爸爸的名字返回爸爸用户
def searchFaUser(faname):
    for user in users:
        if user.username == faname:
            return user
    return None


# 找某用户的爸爸用户
def searchFa(user):
    if user.father != None:
        fauser = searchFaUser(user.father)  # 根据爸爸的名字返回爸爸用户
        if fauser != None:
            return fauser
    return None


# 测试 查找13号的祖辈
ids, users = serarchDbAll()
currentuser = serarchDb(13)
fausers = [currentuser]
tempuser = currentuser
while searchFa(tempuser) != None:
    fausers.append(searchFa(tempuser))
    tempuser = searchFa(tempuser)
print(currentuser.username + "的家族成员是：")
for fau in fausers:
    print(fau.username)
