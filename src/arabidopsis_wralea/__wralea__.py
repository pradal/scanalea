
# This file has been generated at Fri Apr  4 09:28:38 2014

from openalea.core import *


__name__ = 'ScanAlea.Arabido'

__editable__ = True
__description__ = ''
__license__ = 'CeCILL-C'
__url__ = 'http://openalea.gforge.inria.fr'
__alias__ = []
__version__ = '1.0.0'
__authors__ = ''
__institutes__ = 'CSIRO, INRIA, CIRAD, INRA'
__icon__ = ''


__all__ = ['plant3d_dynamic_mtg', '_4686572880', 'data_read', 'plant3d_plot3d_with_time']



plant3d_dynamic_mtg = Factory(name='dynamic_mtg',
                authors=' (wralea authors)',
                description='',
                category='Unclassified',
                nodemodule='arabido.plant3d',
                nodeclass='dynamic_mtg',
                inputs=({'name': 'table'},),
                outputs=({'name': 'g'},),
                widgetmodule=None,
                widgetclass=None,
               )



_4686572880 = DataFactory(name='Arabido.txt',
                    description='Karine Chenu PhD data',
                    editors=None,
                    includes=None,
                    )



data_read = Factory(name='growth_data_arabido',
                authors=' (wralea authors)',
                description='',
                category='Unclassified',
                nodemodule='arabido.data',
                nodeclass='read',
                inputs=({'interface': 'IFileStr', 'name': 'filename'},),
                outputs=({'interface': None, 'name': 'table'},),
                widgetmodule=None,
                widgetclass=None,
               )




plant3d_plot3d_with_time = Factory(name='single_time_point',
                authors=' (wralea authors)',
                description='',
                category='Unclassified',
                nodemodule='arabido.plant3d',
                nodeclass='plot3d_with_time',
                inputs=({'name': 'g'}, {'interface': 'IInt', 'name': 'vid', 'value': 0}, {'interface': 'IInt', 'name': 'time', 'value': 0}, {'hide': True, 'name': 'visitor'}, {'hide': True, 'name': 'turtle'}, {'interface': 'ISequence', 'hide': True, 'name': 'show'}, {'interface': 'ISequence', 'name': 'positions'}),
                outputs=({'name': 'scene'},),
                widgetmodule=None,
                widgetclass=None,
               )




