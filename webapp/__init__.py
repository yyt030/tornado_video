#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import base64
import uuid

import os
import tornado.web
from webapp.controllers import site, user


class CreateApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', site.IndexHandler),
            (r'/login', user.LoginHandler),
            (r'/video',site.CourseHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
            cookie_secret=base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
            xsrf_cookies=True,
            login_url='/login'
        )
        # mongo_client = pymongo.MongoClient(host='localhost', port=27017)
        # self.db = mongo_client['example']

        tornado.web.Application.__init__(self, handlers, **settings)
