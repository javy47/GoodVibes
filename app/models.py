from app import db


class Artist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(512), index=True, )

    def __repr__(self):
        return '{}'.format(self.name)


class Events(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    price = db.Column(db.Integer, index=True, unique=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))

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


