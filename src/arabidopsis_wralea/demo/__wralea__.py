
# This file has been generated at Fri Apr  4 09:40:15 2014

from openalea.core import *


__name__ = 'ScanAlea.Arabido.Demo'

__editable__ = True
__description__ = ''
__license__ = 'CeCILL-C'
__url__ = 'http://openalea.gforge.inria.fr'
__alias__ = []
__version__ = '1.0.0'
__authors__ = ''
__institutes__ = 'CSIRO, INRIA, CIRAD, INRA'
__icon__ = ''


__all__ = ['Arabido', '_4708024272']



Arabido = CompositeNodeFactory(name='Arabido',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('ScanAlea.Arabido', 'Arabido.txt'),
   3: ('ScanAlea.Arabido', 'growth_data_arabido'),
   4: ('ScanAlea.Arabido', 'dynamic_mtg'),
   5: ('ScanAlea.Arabido', 'single_time_point'),
   6: ('openalea.data structure', 'int'),
   7: ('vplants.plantgl.visualization', 'plot3D')},
                             elt_connections={  140445745220336: (5, 0, 7, 0),
   140445745220360: (6, 0, 5, 2),
   140445745220384: (4, 0, 5, 0),
   140445745220408: (2, 0, 3, 0),
   140445745220432: (3, 0, 4, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'Arabido.txt',
         'delay': 0,
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': 35.03566702920244,
         'posy': -41.390974071708925,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'growth_data_arabido',
         'delay': 0,
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 9.288525677509483,
         'posy': -4.725741134171493,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'dynamic_mtg',
         'delay': 0,
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 23.302792489190466,
         'posy': 34.546797256701936,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'single_time_point',
         'delay': 0,
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 99.93949821705056,
         'posy': 86.19605342494955,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': '213',
         'delay': 0,
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 178.42680953155335,
         'posy': 21.441848355723153,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'block': False,
         'caption': 'plot3D',
         'delay': 0,
         'hide': True,
         'id': 7,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 135.3174897001279,
         'posy': 128.69177457356795,
         'priority': 0,
         'use_user_color': False,
         'user_application': True,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set([]),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set([]),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [  (0, 'PackageData(ScanAlea.Arabido, Arabido.txt)'),
         (1, 'None'),
         (2, 'None')],
   3: [],
   4: [],
   5: [  (1, '0'),
         (3, 'None'),
         (4, 'None'),
         (5, '[]'),
         (6, '[(-10, 0, 0), (10, 0, 0), None]')],
   6: [(0, '213')],
   7: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [35.03566702920244, -41.390974071708925], 'userColor': None, 'useUserColor': False},
   3: {'position': [9.288525677509483, -4.725741134171493], 'userColor': None, 'useUserColor': False},
   4: {'position': [23.302792489190466, 34.546797256701936], 'userColor': None, 'useUserColor': False},
   5: {'position': [99.93949821705056, 86.19605342494955], 'userColor': None, 'useUserColor': False},
   6: {'position': [178.42680953155335, 21.441848355723153], 'userColor': None, 'useUserColor': False},
   7: {'position': [135.3174897001279, 128.69177457356795], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




_4708024272 = CompositeNodeFactory(name='dynamic arabido',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('ScanAlea.Arabido', 'Arabido.txt'),
   3: ('ScanAlea.Arabido', 'growth_data_arabido'),
   4: ('ScanAlea.Arabido', 'dynamic_mtg'),
   5: ('ScanAlea.Arabido', 'single_time_point'),
   6: ('openalea.data structure', 'int'),
   7: ('vplants.plantgl.visualization', 'plot3D'),
   8: ('openalea.flow control', 'iter'),
   9: ('openalea.python method', 'range')},
                             elt_connections={  140445745220288: (8, 0, 5, 2),
   140445745220312: (9, 0, 8, 0),
   140445745220336: (5, 0, 7, 0),
   140445745220360: (6, 0, 9, 1),
   140445745220384: (4, 0, 5, 0),
   140445745220408: (2, 0, 3, 0),
   140445745220432: (3, 0, 4, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'Arabido.txt',
         'delay': 0,
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': 35.03566702920244,
         'posy': -41.390974071708925,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'growth_data_arabido',
         'delay': 0,
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 9.288525677509483,
         'posy': -4.725741134171493,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'dynamic_mtg',
         'delay': 0,
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 23.302792489190466,
         'posy': 34.546797256701936,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'single_time_point',
         'delay': 0,
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 99.93949821705056,
         'posy': 86.19605342494955,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': '500',
         'delay': 0,
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 280.3061860765093,
         'posy': -85.73175851366463,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'block': False,
         'caption': 'plot3D',
         'delay': 0,
         'hide': True,
         'id': 7,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 135.3174897001279,
         'posy': 128.69177457356795,
         'priority': 0,
         'use_user_color': False,
         'user_application': False,
         'user_color': None},
   8: {  'block': False,
         'caption': 'iter',
         'delay': 0,
         'hide': True,
         'id': 8,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 252.1226536519073,
         'posy': 43.65865750272046,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': 'range',
         'delay': 0,
         'hide': True,
         'id': 9,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 253.79654135676498,
         'posy': -11.672004803985322,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set([]),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set([]),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [  (0, 'PackageData(ScanAlea.Arabido, Arabido.txt)'),
         (1, 'None'),
         (2, 'None')],
   3: [  (  0,
            "'/Users/pradal/devlp/scanalea/src/arabidopsis_wralea/Arabido.txt'")],
   4: [],
   5: [  (1, '0'),
         (3, 'None'),
         (4, 'None'),
         (5, '[]'),
         (6, '[(-10, 0, 0), (20, 0, 0), None]')],
   6: [(0, '500')],
   7: [],
   8: [],
   9: [(0, '0'), (2, '1')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [35.03566702920244, -41.390974071708925], 'userColor': None, 'useUserColor': False},
   3: {'position': [9.288525677509483, -4.725741134171493], 'userColor': None, 'useUserColor': False},
   4: {'position': [23.302792489190466, 34.546797256701936], 'userColor': None, 'useUserColor': False},
   5: {'position': [99.93949821705056, 86.19605342494955], 'userColor': None, 'useUserColor': False},
   6: {'position': [280.3061860765093, -85.73175851366463], 'userColor': None, 'useUserColor': False},
   7: {'position': [135.3174897001279, 128.69177457356795], 'userColor': None, 'useUserColor': False},
   8: {'position': [252.1226536519073, 43.65865750272046], 'userColor': None, 'useUserColor': False},
   9: {'position': [253.79654135676498, -11.672004803985322], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='DiscreteTimeEvaluation',
                             )



