# -*- coding: UTF-8 -*-

import os
import service


from service_router import route


@route('query_combat_lst')
class QueryCombatService(service.Service):

    def handle(self, query):
        super(QueryCombatService, self).handle(query)

        import time
        data = []
        for i in xrange(0, 10):
            combat = {'time': int(time.time()), 'map_guid': 'combat_%d' % i}
            data.append(combat)

        return {
            'err_code': 0,
            'data': {
                'combat_lst': data,
            }
        }

