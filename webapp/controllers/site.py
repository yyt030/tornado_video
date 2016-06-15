#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        courses = [{'id': 1, 'name': 'C', 'title': '俄罗斯方块', 'desc': 'you can move and play'},
                   {'id': 2, 'name': 'C++', 'title': 'C++ learning', 'desc': 'you can move and play'},
                   {'id': 3, 'name': 'Python', 'title': 'Python learning', 'desc': 'you can move and play'},
                   {'id': 4, 'name': 'Java', 'title': 'Java learning', 'desc': 'you can move and play'},
                   {'id': 1, 'name': 'C', 'title': 'C learning', 'desc': 'you can move and play'},
                   {'id': 2, 'name': 'C++', 'title': 'C++ learning', 'desc': 'you can move and play'},
                   ]
        self.render('index.html', courses=courses)



class CourseHandler(RequestHandler):
    def get(self):
        self.render('video.html')