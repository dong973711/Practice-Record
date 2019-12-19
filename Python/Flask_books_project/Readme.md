##### 利用flask简单实战实现一个简单的图书管理
[视频学习地址](https://www.bilibili.com/video/av26468502?p=18)
实现过程及用到的内容：
##### 1、配置数据库
    a.导入SQLAlchemy拓展
    b.创建bd对象，并配置参数
    c.终端创建数据库
##### 2、添加书和作者模型
    a.模型继承db.Model
    b.__tablename__:表名
    c.db.Column:字段
    d.db.relationship :关系引用
##### 3、添加数据
##### 4、使用模板显示数据库查询数据
    a.查询所有的作者信息，让信息传递给模板
    b.模板中按照格式，依次for循环坐着和书籍
##### 5、使用WTF显示表单
    a.自定义表单类
    b.模板中显示
    c.secret_key/编码/csrf_token
6、实现相关的增删逻辑
    a.增加数据
    b.删除数据 url_for/for else/redirect的使用
    c.删除作者