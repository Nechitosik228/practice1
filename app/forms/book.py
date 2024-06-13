from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length
)


class BookForm(Form):
    name = StringField("Enter name of the book", validators=[DataRequired("Give the name of the book")])

    author = StringField("Enter name of the author",validators=[DataRequired("Give the name of the author")])

    price = StringField("Enter the price", validators=[DataRequired("Give the price")])

    submit = SubmitField("Add")