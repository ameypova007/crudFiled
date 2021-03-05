from datetime import datetime
from sound import db
from sqlalchemy_utils import ScalarListType

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    uploadedTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Song('{self.title}', '{self.duration}')"

class Podcast(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	uploadedTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	duration = db.Column(db.Integer, nullable=False)
	participants = db.Column(ScalarListType(str),nullable=True)
	host = db.Column(db.String(100), nullable=False)

class AudioBook(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	uploadedTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	duration = db.Column(db.Integer, nullable=False)
	author = db.Column(db.String(100), nullable=False)
	narrator = db.Column(db.String(100), nullable=False)
