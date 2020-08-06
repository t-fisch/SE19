from app import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    body = db.Column(db.String(4000))

    def __repr__(self):
        return '<Comment {}>'.format(self.firstname)
