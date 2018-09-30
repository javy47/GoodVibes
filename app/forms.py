from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ArtistForm(FlaskForm):
    artist = StringField('ArtistName', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[DataRequired()])
    bio = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Artist')
