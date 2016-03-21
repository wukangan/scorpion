#-*- coding: utf-8 -*-

import ctrl

class IndexHandler(ctrl.BaseHandler):
    def __init__(self, application, request, **kwargs):
        ctrl.BaseHandler.__init__(self, application, request, **kwargs)

    def get(self):
        self.render('index.html')