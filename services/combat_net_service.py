# -*- coding: UTF-8 -*-

import os
import service
import logging
import random
import copy

from service_router import route


@route('combat_net')
class CombatNetService(service.Service):
    def handle(self, query):
        super(CombatNetService, self).handle(query)

        player_tmpl = {
                'id': 'player1',
                'name': '战狂',

                'trend_seg': 10,
                'device_flow_trend': [100, 100, 200, 300, 400, 500],
                'game_flow_trend':  [100, 100, 200, 300, 400, 500],
                'ping_trend': [100, 100, 200, 300, 400, 500],
                'kcp_ping_trend': [100, 100, 200, 300, 400, 500],
                'logic_ping_trend': [100, 100, 200, 300, 400, 500],

                'dist_seg'  : 50,
                'ping_dist' : [0, 0, 1, 2, 3, 4],
                'kcp_ping_dist': [0, 0, 1, 2, 3, 4],
                'logic_ping_dist': [0, 0, 1, 2, 3, 4],


                'packet_loss_rate': 0.02,
                'slow_start': 2,
                't_rsnd_times': 2,
                'f_rsnd_times': 2,
                'snd_times': 243,
                'rcv_time': 323,

                'snd_sz': 1343,
                'rcv_sz': 2343,
        }


        data = {
            'pivot_player': 'player1',
            'faction_players': [
                ['player0', 'player1', 'player2', 'player3', 'player4'],
                ['player5', 'player6', 'player7', 'player8', 'player9']
            ],
            'net_infos': {
            }
        }

        for i in xrange(10):
            net_item = copy.deepcopy(player_tmpl)

            player_id = 'player%d' % i
            net_item['id'] = player_id

            for key, value in net_item.iteritems():
                if isinstance(value, str):
                    continue

                if isinstance(value, list):
                    for i in xrange(len(value)):
                        value[i] *= int(random.random() * 3 + 1)
                else:
                    net_item[key] *= random.random()

            data['net_infos'][player_id] = net_item

        return data

