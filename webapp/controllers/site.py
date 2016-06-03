#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.render('base.html')


