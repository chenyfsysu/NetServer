# -*- coding: UTF-8 -*-

import os
import json
import signal
import httplib
import logging
import services
import urlparse
import SocketServer
import SimpleHTTPServer

_dispatcher = None

class HTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.send_header("Access-Control-Allow-Methods", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type,Authorization")
        self.send_header("Access-Control-Expose-Headers", "*")
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        code, data = _dispatcher.dispatch(self)
        self.send_response(code)
        self.send_header('Content-type', 'text/json')
        self.send_header('charset', 'utf-8')
        self.end_headers()

        logging.info('>>>>>>>>>>>>>>>>>> %s', data)
        self.wfile.write(json.dumps(data, 'utf8'))
        pass

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


class ServiceDispatcher(object):
    def __init__(self):
        self.services = services.generate()

    def dispatch(self, handler):
        path, query = self.parse_args(handler.path)

        if path not in self.services:
            logging.error("service %s is not find....", path)
            return httplib.NOT_FOUND, None

        code, data = httplib.OK, None
        service = self.services[path]
        try:
            data = service.handle(query)
        except Exception as e:
            print e
            logging('service process error')
            code = httplib.INTERNAL_SERVER_ERROR

        return code, data

    def parse_args(self, path):
        try:
            request = urlparse.urlparse(path)
        except Exception as e:
            logging.error('parse argument error....')
            return None, None

        query = urlparse.parse_qs(request.query)
        path = request.path.strip('/')

        return path, query


if __name__ == '__main__':
    global _dispatcher
    _dispatcher = ServiceDispatcher()

    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer(('', 18888), HTTPHandler)
    server.serve_forever()

