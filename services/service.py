# -*- coding: UTF-8 -*-

import os
import json
import logging


class Service(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)


    def handle(self, query):
        self.logger.info('handle request, path: %s', query)

