from flask import Flask, render_template,flash,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# 数据库配置：数据库地址/关闭自动跟踪修改
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:test1234@127.0.0.1/pythontest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'test'

# 创建数据库对象
db = SQLAlchemy(app)

'''
1、配置数据库
    a.导入SQLAlchemy拓展
    b.创建bd对象，并配置参数
    c.终端创建数据库
2、添加书和作者模型
    a.模型继承db.Model
    b.__tablename__:表名
    c.db.Column:字段
    d.db.relationship :关系引用
3、添加数据
4、使用模板显示数据库查询数据
    a.查询所有的作者信息，让信息传递给模板
    b.模板中按照格式，依次for循环坐着和书籍
5、使用WTF显示表单
    a.自定义表单类
    b.模板中显示
    c.secret_key/编码/csrf_token
6、实现相关的增删逻辑
    a.增加数据
    b.删除数据 url_for/for else/redirect的使用
    c.删除作者
'''


# 定义书和作者模型
# 坐着模型
class Author(db.Model):
    # 表名
    __tablename__ = 'authors'
    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 关系引用
    # books是给自己（Author模型）用的，author是给Book模型用的
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return 'Author : %s' % self.name


# 书籍模型
# 表名
class Book(db.Model):
    __tablename__ = 'books'
    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'Book : %s %s' % (self.name, self.id)

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    # print(book_id)
    # 查询数据库，是否有该id的书，如果有就删除，没有就提示错误
    book = Book.query.get(book_id)
    # print(book)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash("删除书籍出错")
    else:
        flash("没有书籍")
    # redirect:重定向，需要传入网络/路由地址
    # url_for('index'):如果需要传入试图函数名，返回试图函数对应的路由地址
    return redirect(url_for('index'))
@app.route('/delete_author/<authorid>')
def delete_author(authorid):
    # 查询数据库，是否有该id的书，如果有就删除，没有就提示错误
    author = Author.query.get(authorid)
    #print(author)
    if author:
        books = Book.query.get(authorid)
        # print(books)
        if books:
            try:
                db.session.delete(books)
                db.session.delete(author)
                db.session.commit()
            except Exception as e:
                print(e)
        else:
            try:
                db.session.delete(author)
                db.session.commit()
            except Exception as e:
                print(e)
    else:
        flash("没有这个作者")
    # redirect:重定向，需要传入网络/路由地址
    # url_for('index'):如果需要传入试图函数名，返回试图函数对应的路由地址
    return redirect(url_for('index'))


# 自定义表单类
class AuthorForm(FlaskForm):
    author = StringField('作者', validators=[DataRequired()])
    book = StringField('书籍', validators=[DataRequired()])
    submit = SubmitField('提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    # 创建自定义表单类
    author_form = AuthorForm()

    '''
    验证逻辑：
    1.调用WTF的函数实现验证
    2.验证通过获取数据
    3.判断作者是否存在
    4.如果作者存在，欧安段数据是否存在，没有重复书籍就提娜佳数据，如果重复就提示错误
    5.如果作者不存在，添加作者和书籍
    6.验证不通过就提示错误
        a.添加数据
        b.删除书籍--》网页中删除--》点击需要发送书籍的ID给删除书籍的路由--》路由需要接受参数
    '''
    # 1
    if author_form.validate_on_submit():
        # 2
        author_name = author_form.author.data
        book_name = author_form.book.data
        # print(author_name, book_name)

        # 3
        author = Author.query.filter_by(name=author_name).first()
        # 4
        if author :
            # 作者存在，判断书籍是否存在
            book = Book.query.filter_by(name=book_name).first()
            if book:
                flash("该书籍已经存在")
            else:
                # 添加
                try:
                    new_book = Book(name=book_name, author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash("添加书籍失败")
                    db.session.rollback()
        else:
            # print("开始添加")
            # 5
            try:
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()
                new_book = Book(name=book_name, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                print(e)
                flash("添加作者和书籍失败")

    else:
        # 6
        if request.method == 'POST':
            flash('参数不全')

    # 查询所有的坐着信息，让信息传递给模板
    authors = Author.query.all()
    # print(authors)

    return render_template('books.html', authors=authors, form=author_form)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # 生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老会')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='隔壁老王', author_id=au1.id)
    bk2 = Book(name='彩笔', author_id=au1.id)
    bk3 = Book(name='隔', author_id=au2.id)
    bk4 = Book(name='飞机', author_id=au3.id)
    bk5 = Book(name='大炮', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    db.session.commit()

    app.run(debug=True)
