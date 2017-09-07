from  app import  db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

# class User_check():
#     def __init__(self,user,email_addr):
#         self.user = user
#         self.email = email_addr
#
#     def User_create(self):
#         u = User(nickname=self.user,email=self.email)
#         db.session.add(u)
#         db.session.commit
#
#     def User_query(self):
#         users = User.query.all()
#         print users
#
# A=User_check('xiaod','xiaod@email.com')
# #A.User_create()
# #A.User_query()