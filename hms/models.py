from datetime import datetime
from hms import db
class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),unique=True,nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	image_file = db.Column(db.String(32),nullable=False,default='default.jpg')
	password=db.Column(db.String(60),nullable=False)
	posts = db.relationship('Post',backref='author',lazy=True)

	def __repr__(self):
		Message=self.username + " "+self.email+ " "+self.image_file
		return Message
class Post(db.Model):
		id=db.Column(db.Integer,primary_key=True)
		title=db.Column(db.String(100),nullable=False)

		data_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
		content=db.Column(db.Text,nullable=False)
		user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
		def __repr__(self):
			Message=self.title+" "+self.data_posted
			return Message
class userstore(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),nullable=False,unique=True)
	password=db.Column(db.String(40),nullable=False)
	def __repr__():
		Message=self.id+" "+self.username
		return Message
class Patient(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	pname=db.Column(db.String(30),nullable=False)
	pdob=db.Column(db.DateTime,nullable=False)
	page=db.Column(db.Integer,nullable=False)
	ptob=db.Column(db.String(20),nullable=False)
	padd=db.Column(db.String(20),nullable=False)
	pcity=db.Column(db.String(20),nullable=False)
	pstate=db.Column(db.String(20),nullable=False)