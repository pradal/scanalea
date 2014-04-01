import numpy as np
import openalea.plantgl.all as pgl


def lamina_area(tt_phy, surface_P1=6, surface_P2=64, surface_Vm=0.04):
    """    doc"""
    
    return float(surface_P1)/(1 + np.exp(4*surface_Vm*(surface_P2-tt_phy)/surface_P1))

def petiole_length(lamina_area, a=-8,b=12,c=0.08):
    """    doc"""

    return a+b*float(lamina_area)**c

def Arabido_visitor(g, v, turtle, time):
    """     doc"""
    turtle.setId(v)
    node = g.node(v)
    metamer = node.complex()
    tt_phy = time - metamer.init_phy
    if "Petiole" in node.label:
        lamina = node.child()
    
        metamer.Sf = lamina_area(tt_phy, lamina.surface_P1, lamina.surface_P2, lamina.surface_Vm)
        metamer.pl = petiole_lenght(Sf, node.a_length, node.b_length, node.c_length)
        turtle.roll(137)
        turtle.F(pl)
    elif "Lamina" in node.label:
        Sf = metamer.Sf
        lw = Sf / np.pi
        l = np.sqrt(lw / node.Rlimbe)
        geom = pgl.Scaled(pgl.Vector3(l,l*node.Rlimbe,0),pgl.Disc(slices=12))
        turtle.customGeometry(geom)
    else:
	pass



