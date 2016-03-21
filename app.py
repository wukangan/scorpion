#-*- coding: utf-8 -*-

import os.path

import tornado.web

from ctrl import ErrorHandler
from ctrl.index import IndexHandler

class Application(tornado.web.Application):
    def __init__(self, conf):
        handlers = [
            (r'/', IndexHandler),

            (r'.*', ErrorHandler)
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), 'template'),
            static_path   = os.path.join(os.path.dirname(__file__), 'static'),
            static_uri    = conf['static'],
            xsrf_cookies  = True,
            cookie_secret = conf['cookie_secret'],
            debug         = True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)