#!/bin/env python
#-*- coding: utf-8 -*-

import sys
import yaml
import logging
import logging.config

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

import app
import config

#设置系统默认编码为UTF-8
if 'utf-8' != sys.getdefaultencoding():
    reload(sys)
    sys.setdefaultencoding('utf-8')

#定义日志格式
logging.config.dictConfig(yaml.load(open('logging.yaml', 'r')))

#启动应用
def start_server(conf, logger = None):
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app.Application(conf))
    http_server.listen(port = conf['port'], address = conf['ip'])
    logger.info('Development server is running at http://%s:%s/.' % (conf['ip'], conf['port']))
    logger.info('Quit the server with CONTROL-C.')
    tornado.ioloop.IOLoop.instance().start()

#主函数
def main():
    logger = logging.getLogger('tornado.starting')
    try:
        start_server(config.conf, logger)
    except KeyboardInterrupt:
        logger.warn('Development server is stopped.')
    except Exception, e:
        logger.error(e)

if __name__ == '__main__':
    main()
