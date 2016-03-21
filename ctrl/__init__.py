#-*- coding: utf-8 -*-

import logging

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        tornado.web.RequestHandler.__init__(self, application, request, **kwargs)

    #设置Response Headers
    def set_default_headers(self):
        self.set_header('Server', 'wka.name')

    #重写错误页面
    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.finish('404')
        else:
            self.finish('50X')

class ErrorHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        BaseHandler.__init__(self, application, request, **kwargs)

    def get(self):
        self.write_error(404)

    def post(self):
        self.write_error(404)