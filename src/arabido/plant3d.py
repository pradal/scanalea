""" Arabidopsis model built from a multi-variate time series measurements

"""

import pandas as pd
from openalea.mtg import *
from openalea.mtg.traversal import *
from openalea.mtg.plantframe import turtle as mtg_turtle, color as mtg_color
from openalea.plantgl import all as pgl
from arabido.visitor import *

def stub():
    """ Build a fake dataframe """
    d = {}
    phy = range(1,11)
    time_init = map(float,range(10))
    d['phy']= phy
    d['init_time'] = time_init
    d['surface_P1']= [5,6]+[float(20*i) for i in range(2,10)]
    d['surface_P2'] = [2.* p1 for p1 in d['surface_P1']]
    d['surface_Vm'] = [0.5 for i in range(10)]

    df = dataset = pd.DataFrame.from_dict(d)
    df['plant']=1

    return dataset

def props(df, plant, phy):
    vid_props = df[(df.plant==plant)&(df.phy==phy)].to_dict(outtype='list')
    return dict( (k, v[0]) for k, v in vid_props.iteritems())

def petiol_props(props):
    d={}
    names = ['a_length','b_length','c_length']
    for name in names:
        d[name] = props[name]
    return d

def lamina_props(props):
    d={}
    names = ['surface_P1','surface_P2','surface_Vm','R_limbe']
    for name in names:
        d[name] = props[name]
    return d

def dynamic_mtg(dataset, *args, **kwds):
    """ 
    Create a dynamic MTG from a pandas dataset.


    """
    df = dataset

    plant_ids = df.plant.unique()
    plant_ids.sort()

    g = MTG()
    
    for plant in plant_ids:
        phytomers = []

        pid = g.add_component(g.root, label='Plant%d'%(plant))

        df_plant= df[df['plant']==plant]
        phytomer_ids = df_plant.phy.unique()
        phytomer_ids.sort()
        n = len(phytomer_ids)

        phy = phytomer_ids[0]
        values = props(df_plant, plant, phy)

        #axis_id = g.add_component(pid, label='Axis')

        phe_id = g.add_component(pid, label='Phytomer%d'%(phytomer_ids[0]), init_time=values['init_time'])
        internode_id = g.add_component(phe_id, label='Internode%d'%(phytomer_ids[0]), length=0.)
        petiole_id = g.add_child(internode_id, label='Petiole%d'%(phytomer_ids[0]), edge_type='+', **petiol_props(values))
        lamina_id = g.add_child(petiole_id, label='Lamina%d'%(phytomer_ids[0]), edge_type='<', **lamina_props(values))
        
        phytomers.append((g.node(petiole_id),g.node(lamina_id)))

        for i in range(1,n):
            phy = phytomer_ids[i]
            values = props(df_plant, plant, phy)

            phe_id = g.add_child(phe_id, edge_type='<', label='Phytomer%s'%(phy), init_time=values['init_time'])
            internode_id = g.add_child(internode_id, edge_type='<', label='Internode%d'%(phy), length=0.)
            internode_id = g.add_component(phe_id, component_id=internode_id)
            petiole_id = g.add_child(internode_id, label='Petiole%d'%(phy), edge_type='+', **petiol_props(values))
            lamina_id = g.add_child(petiole_id, label='Lamina%d'%(phy), edge_type='<', **lamina_props(values))

            phytomers.append((g.node(petiole_id),g.node(lamina_id)))

        # Update properties

    g = fat_mtg(g)

    return g


def traverse_with_turtle_time(g, vid, time,  visitor=None, turtle=None, gc=True, show=[], start_time = 'init_time'):
    if turtle is None:
        turtle = pgl.PglTurtle()
    
    _start_time = g.property(start_time)
    def push_turtle(v):
        complex_id = g.complex(v)
        start_tt = _start_time.get(complex_id,0)
        if start_tt > time:
            return False
        if g.edge_type(v) == '+':
            turtle.push()
            if gc:
                turtle.startGC()
        return True

    def pop_turtle(v):
        complex_id = g.complex(v)
        start_tt = _start_time.get(complex_id,0)
        if start_tt > time:
            return False
        if g.edge_type(v) == '+':
            if gc:
                turtle.stopGC()
            turtle.pop()

    start_tt = _start_time.get(g.complex(vid),0)
    if start_tt <= time:
        visitor(g,vid,turtle,time,show=show)
        turtle.push()
    
    for v in pre_order2_with_filter(g, vid, None, push_turtle, pop_turtle):
        if v == vid: continue
        start_tt = _start_time.get(g.complex(v),0)
        if start_tt > time:
            print 'Do not consider ', v, time
            continue
        visitor(g,v,turtle,time,show=show)

    scene = turtle.getScene()
    return scene


def plot3d_with_time(g, vid, time=0, visitor=None, turtle=None, show=[], positions=None, **kwds ):

    if turtle is None:
        turtle = pgl.PglTurtle()
    if visitor is None:
        visitor = arabido_visitor

    #color_index = define_colors(g,turtle, 'year')
    max_scale = g.max_scale() 
    plants = g.component_roots_at_scale(vid, scale=max_scale)

    if not positions:
        positions = [(10*i, 0,0) for i in range(len(plants))]
    elif len(positions) < len(plants):
        diff = len(plants) - len(positions)
        p = positions[-1]
        for i in range(len(positions), len(plants)):
            p1= (p[0]+10,p[1],p[2])
            positions.append(p1)
            p = p1

    i = 0
    for plant_id in plants:

        turtle.move(*positions[i])
        traverse_with_turtle_time(g,plant_id, time, visitor=visitor, turtle=turtle, gc=False, show=show)
        i+=1
    
    scene = turtle.getScene()

    # Colors : 
    shapes = scene.todict()

    colors = g.property('color')
    for vid in colors:
        if vid in shapes:
            for sh in shapes[vid]:
                sh.appearance = pgl.Material(colors[vid])
    scene = pgl.Scene([shape for list_shape in shapes.itervalues() for shape in list_shape])

    return scene

