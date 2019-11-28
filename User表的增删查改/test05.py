# 查找当前user所有的亲缘关系
# father,monther,father's father,fahter's mother

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
        # print("查找失败")
        return None
    else:
        # print("查找成功")
        data = cursor.fetchall()
        for i in range(len(data)):
            user = User(0, "", "", 0, "", "")
            user.id = data[i][0]
            user.username = data[i][1]
            user.birth_data = data[i][2]
            user.money = data[i][3]
            user.father = data[i][4]
            user.mother = data[i][5]
            users.append(user)
            ids.append(data[i][0])
    closeDb()
    return ids, users


# 根据名字返回这个人用户对象（未考虑重名问题）
def NameSearchUser(name):
    ids, users = serarchDbAll()
    for user in users:
        if user.username == name:
            return user
    return None


# 找某用户的爸爸用户
def searchFa(user):
    if user.father != None:
        fauser = NameSearchUser(user.father)  # 根据爸爸的名字返回爸爸用户
        if fauser != None:
            print("他的名字是：", fauser.username)
            return fauser
    print("他的名字为空")
    return None


# 找某用户的妈妈用户
def searchMo(user):
    if user.mother != None:
        mouser = NameSearchUser(user.mother)  # 根据名字返回妈妈用户
        if mouser != None:
            print("她的名字是：", mouser.username)
            return mouser
    print("她的名字为空")
    return None


# 查找13号的祖先
currentuser = serarchDb(13)  # 得到13号用户本人
print("当前用户是：", currentuser.username)

print("当前用户的父亲是：")
cur_fa = searchFa(currentuser)  # 得到当前用户的父亲
print(cur_fa)

print("当前用户的母亲是：")
cur_mo = searchMo(currentuser)  # 得到当前用户的母亲
print(cur_mo)

print("当前用户的爷爷:")
cur_fa_fa = searchFa(cur_fa)  # 得到当前用户的爷爷
print(cur_fa_fa)

print("当前用户的奶奶:")
cur_fa_mo = searchMo(cur_fa)  # 得到当前用户的奶奶
print(cur_fa_mo)

print("当前用户的姥爷:")
cur_mo_fa = searchFa(cur_mo)  # 得到当前用户的姥爷
print(cur_mo_fa)

print("得到当前用户的姥姥:")
cur_mo_mo = searchMo(cur_mo)  # 得到当前用户的姥姥
print(cur_mo_mo)
