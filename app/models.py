from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    passwordH = db.Column(db.String(128))

    def __repr__(self):
        return '{}'.format(self.username)

    def set_password(self, password):
        self.passwordH = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordH, password)


@login.user_loader
def load_user(id):
    return User.query.get(id)


class Artist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(512), index=True )

    def __repr__(self):
        return '{}'.format(self.name)


class Events(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    price = db.Column(db.Integer, index=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    event_date = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return ' {}'.format(self.name)


class Venues(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), index=True, unique=True)
    date = db.Column(db.String(10), index=True, unique=True)
    event = db.relationship('Events', backref='venue', lazy='dynamic')

    def __repr__(self):
        return ' {}'.format(self.location)


class ArtistToEvent(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    Event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    artist = db.relationship('Artist', backref='eventA')
    event = db.relationship('Events', backref='authorE')


