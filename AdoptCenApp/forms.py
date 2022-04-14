from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequried, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Adding Pets Form"""

    name=StringField(
        "Pet's Name",
        validators=[InputRequired()],
    )

    species=StringField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"),],
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    age=IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=99)],
    )

    notes=TextAreaField(
        "Pet Comments"
        validators=[Optional(), Length(min=5)],
    )


class EditPetForm(FlaskForm):
    """Form to Edit Existing Pets Submissions"""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Pet Comments",
        validators=[Optional(), Length(min=5)],
    )

    available= BooleanField("Pet Available")