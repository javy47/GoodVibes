from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import Artist


class ArtistForm(FlaskForm):
    artist = StringField('ArtistName', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[DataRequired()])
    bio = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Artist')

    def validate_artist(self, artist):
        art1 = Artist.query.filter_by(name=artist.data).first()
        if art1 is not None:
            raise ValidationError("This artist already exist in the Database")