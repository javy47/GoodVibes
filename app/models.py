from app import db


class Artist(db.Model):
    __tablename__= "Artist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(512), index=True, unique=True)

    def __repr__(self):
        return '<Artist {}>'.format(self.name)


class Events(db.Model):
    __tablename__ = "Events"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    price = db.Column(db.Integer, index=True, unique=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venues.id'))

    def __repr__(self):
        return '<Events {}>'.format(self.name)


class Venues(db.Model):
    __tablename__ = "Venues"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), index=True, unique=True)
    date = db.Column(db.String(10), index=True, unique=True)

    def __repr__(self):
        return '<Venues {}>'.format(self.name)


class ArtistToEvent(db.Model):
    __tablename__ = "Artist to Events"
    id = db.Column(db.Integer, primary_key=True)
    Artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    Event_id = db.Column(db.Integer, db.ForeignKey('Events.id'))


