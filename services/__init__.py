# -*- coding: UTF-8 -*-

import service_router


service_router.register_all()


def generate():
    servies = service_router.get_all_services()

    return {name : service_cls() for name, service_cls in servies.iteritems()}

