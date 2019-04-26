# -*- coding: UTF-8 -*-

import os
import json


__all_service__ = {}


def route(service_name):
    def _route(kclass):
        __all_service__[service_name] = kclass

        return kclass

    return _route


def _get_services_modules(path):
    modules = []
    for dirpath, _, files in os.walk(path):
        if dirpath.find('.svn') != -1 or dirpath.find('.git') != -1:
            continue

        for filepath in files:
            if not filepath.endswith('.py') and not filepath.endswith('.pyc'):
                continue

            if filepath.startswith('__'):
                continue

            fullpath = os.path.join(dirpath, filepath)
            module_name = fullpath.replace('.pyc', '').replace('.py', '')
            module_name = module_name.replace('/', '.').replace('\\', '.')
            module_name not in modules and modules.append(module_name)

    return modules


def register_all():
    modules = _get_services_modules('services')
    for module_name in modules:
        try:
            __import__(module_name, fromlist=['services'])
        except Exception as e:
            logging.error('error in register services : %s', module_name)


def get_all_services():
    return __all_service__

