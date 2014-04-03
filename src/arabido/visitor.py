import numpy as np
import openalea.plantgl.all as pgl
from random import randint

def lamina_area(tt_phy, surface_P1=6, surface_P2=64, surface_Vm=0.04):
    """    doc"""
    
    return float(surface_P1)/(1 + np.exp(4*surface_Vm*(surface_P2-tt_phy)/surface_P1))

def petiole_length(lamina_area, a=-8,b=12,c=0.08):
    """    doc"""

    return a+b*float(lamina_area)**c

def arabido_visitor(g, v, turtle, time, **args):
    """     doc"""
    turtle.setId(v)
    node = g.node(v)
    metamer = node.complex()
    tt_phy = time - metamer.init_time
    node.color = (10,100,10)
    if "Petiole" in node.label:
        lamina = node.children()[0]
    
        Sf = metamer.Sf = lamina_area(tt_phy, lamina.surface_P1, lamina.surface_P2, lamina.surface_Vm)
        pl = metamer.pl = petiole_length(Sf, node.a_length, node.b_length, node.c_length)
        if 'inclination' not in g[v]:
            node.inclination = 90. - randint(0,15)
        turtle.down(node.inclination)
        turtle.setWidth(.05)

        turtle.F(pl)
    elif "Lamina" in node.label:
        turtle.down(90.)
        Sf = metamer.Sf
        lw = Sf / np.pi
        l = np.sqrt(lw / node.R_limbe)
        geom = pgl.Translated(pgl.Vector3(l/2.,0,0),pgl.Scaled(pgl.Vector3(l,l*node.R_limbe,0),pgl.Disc(slices=12)))
        turtle.customGeometry(geom)
    else:
        turtle.rollL(137)



