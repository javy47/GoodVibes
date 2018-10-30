from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, DateField, SelectField, \
    SelectMultipleField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import Artist, User, Venues, Events


class ArtistForm(FlaskForm):
    artist = StringField('ArtistName', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[DataRequired()])
    bio = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Artist')

    def validate_artist(self, artist):
        art1 = Artist.query.filter_by(name=artist.data).first()
        if art1 is not None:
            raise ValidationError("This artist already exist in the Database")


class VenueForm(FlaskForm):
    venue = StringField('Venue Location', validators=[DataRequired()])
    submit = SubmitField('Add Venue')

    def validate_venue(self, venue):
        ven1 = Venues.query.filter_by(location=venue.data).first()
        if ven1 is not None:
            raise ValidationError("This venue already exist in the Database")


class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user2 = User.query.filter_by(username=username.data).first()
        if user2 is not None:
            raise ValidationError("Please use a different Username")


class EventForm(FlaskForm):
    artistName = SelectMultipleField('Artist', choices=[], coerce=int)
    eventName = StringField('Event Name', validators=[DataRequired()])
    venueName = SelectField('Venue Name', choices=[], coerce=int, validators=[DataRequired()])
    eventDate = DateField('Event Date (YYYY-MM-DD)', format='%Y-%m-%d', validators=[DateField])

    submit = SubmitField('Add Event')

    def validate_eventName(self, eventName):
        event2 = Events.query.filter_by(name=eventName.data).first()
        if event2 is not None:
            raise ValidationError("Please create a different Event")

