from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, ValidationError, URL, Optional

def validate_species(form, field):
    species_lst = ["porcupine", "cat", "dog"]
    if(field.data.lower() not in species_lst):
        raise ValidationError('We cannot accept that animal')

def validate_age(form, field):
    if field.data < 0 or field.data > 30:
        raise ValidationError('Please pick an age between 0 and 30')

class PetForm(FlaskForm):

    name = StringField("Pet name", validators=[InputRequired(message="Please provide pet name")])
    species = StringField("Species", validators=[InputRequired(message="Please provide pet species"), validate_species])

    photo_url = StringField("Photo link", validators=[Optional(),URL()])
    age = IntegerField("Age", validators=[Optional(),validate_age])
    notes = StringField("Notes")
    available = BooleanField("Available")
