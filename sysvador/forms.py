from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ImageRequestForm(FlaskForm):
    image_description = StringField("How should the image look", validators=[DataRequired()])
    submit = SubmitField("Submit")

