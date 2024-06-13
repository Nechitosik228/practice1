from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length
)


class RegisterForm(Form):
    nickname = StringField("Enter your nickname", 
                            validators =[
                            DataRequired("This is required"), 
                            Length(min=5)

                                       ]
                          )
    password = PasswordField("Enter password", validators=
                             [
                                EqualTo("subtext", "Must be equal"),
                                DataRequired("This is required"),
                                Length(min=5)
                             ]
                            )
    subtext = PasswordField("Please repeat")
    submit = SubmitField("Submit")