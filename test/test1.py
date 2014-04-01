from openalea.deploy.shared_data import shared_data
from vpltkdisplay import *
from IPython.display import display
from openalea.plantgl.all import *
import scanalea
from scanalea import segmentation as seg
from scanalea.codecs import read, ply
import numpy as np
from openalea.core.path import path
import pandas

def normalised(shape, translation=(0,0,0), color=(60,150,80) ):
    bc=BBoxComputer(Discretizer())
    shape.apply(bc)
    bbox = bc.boundingbox
    gi = shape.geometry
    X,Y=bbox.getXRange(), bbox.getYRange()
    scale = max(X,Y)
    gi=Scaled((1./scale,1./scale,1./scale),gi)
    return Shape(Translated(translation,gi),Material(color))

def test_simple():
    data = path(scanalea.__path__[0])/'..'/'..'

    scene = read(fn)
    geometry = scene[0]

def test_full():
    data = path(scanalea.__path__[0])/'..'/'..'
    datadir = data/'share'/'INRIA_maize'/'finemesh'
    files =datadir.glob('*.ply')

    report = pd.read_csv(datadir/'report.txt',
            sep=' *', 
            header=None, 
            names=['Date', 'num'], 
            infer_datetime_format=True)

    report =report.sort('Date')
    # bad option to  do the trick...
    def fun(x):
        return [f for f in files if ('_'+str(x)+'_') in f][0]
    report['filename'] = report['num'].map(fun)

    scenes = [read(fn) for fn in report['filename']]
    shapes = [normalised(scenes[xx][0], (xx/5,xx%5.,0), (xx*10,80,(xx*30)%255)) for xx in range(len(scenes))]

    scene = Scene(shapes)
    return scene