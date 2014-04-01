""" Arabidopsis model built from a multi-variate time series measurements

"""

import pandas as pd
from openalea.mtg import *

def stub():
    """ Build a fake dataframe """
    d = {}
    phe = range(1,11)
    time_init = map(float,range(10))
    d['phe']= phe
    d['init_time'] = time_init
    d['surface_P1']= [5,6]+[float(20*i) for i in range(2,10)]
    d['surface_P2'] = [2.* p1 for p1 in d['surface_P1']]
    d['surface_Vm'] = [0.5 for i in range(10)]

    dataset = pd.DataFrame.from_dict(d)
    return dataset

def dynamic_mtg(dataset, *args, **kwds):
    """ 
    Create a dynamic MTG from a pandas dataset.


    """
    df = dataset

    phytomer_ids = df.phe.unique()
    phytomer_ids.sort()
    n = len(phytomer_ids)

    phytomers = []
    g = MTG()
    pid = g.add_component(g.root, label='Plant')

    #axis_id = g.add_component(pid, label='Axis')
    phe_id = g.add_component(pid, label='Phytomer%d'%(phytomer_ids[0]))
    internode_id = g.add_component(phe_id, label='Internode%d'%(phytomer_ids[0]), length=0.)
    petiole_id = g.add_child(internode_id, label='Petiole%d'%(phytomer_ids[0]), edge_type='+')
    lamina_id = g.add_child(petiole_id, label='Lamina%d'%(phytomer_ids[0]), edge_type='<')
    
    phytomers.append((g.node(petiole_id),g.node(lamina_id)))

    for i in range(1,n):
        phe_id = g.add_child(phe_id, edge_type='<', label='Phytomer%s'%(phytomer_ids[i]))
        internode_id = g.add_child(internode_id, edge_type='<', label='Internode%d'%(phytomer_ids[i]), length=0.)
        internode_id = g.add_component(phe_id, component_id=internode_id)
        petiole_id = g.add_child(internode_id, label='Petiole%d'%(phytomer_ids[i]), edge_type='+')
        lamina_id = g.add_child(petiole_id, label='Lamina%d'%(phytomer_ids[i]), edge_type='<')

        phytomers.append((g.node(petiole_id),g.node(lamina_id)))

    g = fat_mtg(g)
    return g
