#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired
from wtforms_tornado import Form


class LoginForm(Form):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
