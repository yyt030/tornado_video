#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

from tornado.web import RequestHandler
from ..forms.user import LoginForm


class LoginHandler(RequestHandler):
    def get(self):
        self.write('hello world')

    def post(self):
        form = LoginForm(self.request.arguments)
        if form.validate():
            self.write(str(form.data['a'] + form.data['b']))
        else:
            self.set_status(400)
            self.write("" % form.errors)
