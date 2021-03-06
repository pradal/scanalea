# -*- utf-8 -*-
#
#       VPlants.PlantGL
#
#       Copyright 2013-2013 INRIA - CIRAD - INRA
#
#       File author(s): Christophe Pradal <christophe.pradal@cirad.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite: http://openalea.gforge.inria.fr
#
###############################################################################
""" VTK codecs for PlantGL

This module provide a codec for VTK file format.

This codec allow to read and write `VTK`_ file format. 

.. _VTK: http://en.wikipedia.org/wiki/Wavefront_.obj_file
"""

__license__ = "Cecill-C"
__revision__ = " $Id: $ "

import os
import warnings
from itertools import izip_longest

import openalea.plantgl.math as mt
import openalea.plantgl.scenegraph as sg
import openalea.plantgl.algo as alg
#from openalea.plantgl.ext import color
import numpy as np

def generic_vtk_read(reader, fname, split=True,**kwds):

    r = reader
    r.initialize(fname)
    mesh = r.outputs[0] 

    points = mesh.points.to_array()
    polys = mesh.polys
    faces = polys.to_array()

    faces = faces.reshape((polys.number_of_cells,polys.max_cell_size+1))
    indexList = faces[:,1:]
    
    pts = points.tolist()

    scene = sg.Scene()

    scalars = mesh.point_data.scalars
    if scalars and split:
        scalars = scalars.to_array()
        dim = 1 if len(scalars.shape)==1 else scalars.shape[-1]
        set_scalars = []
        if dim == 1:
            set_scalars = np.unique(scalars)
        elif dim in (3,4):
            set_scalars = set(tuple(x) for x in scalars.tolist())

        leaf_index = 100
        for s in set_scalars:
            idx = None
            if dim ==1:
                idx = (scalars[indexList]==s).any(axis=1).nonzero()[0]
            elif dim in (3,4):
                vertex_has_color = (scalars==s).all(axis=1)
                idx = vertex_has_color[indexList].any(axis=1).nonzero()[0]

            if len(idx) == 0: #or s <= 99:
                continue
            my_faces = indexList[idx].tolist()
            tset = sg.FaceSet(pointList=pts, indexList=my_faces)
            color = np.random.randint(0,255,3).tolist() if dim == 1 else s
            shape = sg.Shape(tset,sg.Material(color))
            if dim == 1:
                shape.id = int(s)
            else:
                if s == (153, 102, 51):
                    shape.id = 1
                elif s == (0,255,255):
                    shape.id = 2
                else:
                    shape.id = leaf_index
                    leaf_index+=1
                if dim == 3 and s == (150,150,150):
                    continue
            scene.add(shape)
    else:
        tset = sg.FaceSet(pointList=pts, indexList=indexList.tolist())
        scene+= tset

    return scene



class VtkCodec (sg.SceneCodec):
    """ VTK File Format 

    """
    
    def __init__(self):
        """
        Initialisation of the codec info
        """
        sg.SceneCodec.__init__(self,"VTK",sg.SceneCodec.Mode.ReadWrite)

    def formats(self):
        """ return formats """
        return [ sg.SceneFormat("VTK Codec",["vtk"],"The vtk file format") ]


    def read(self,fname, split=True, *args):
        """ read a vtk file """
        from mayavi.sources.vtk_file_reader import VTKFileReader
        my_reader = VTKFileReader()

        return generic_vtk_read(my_reader,fname, split=split)



    #############################################################################
    #############################################################################
    # PlantGL -> PLY codec
    def write(self,fname,scene):
        """ Write an OBJ file from a plantGL scene graph.

        This method will convert a PlantGL scene graph into an OBJ file.
        It does not manage  materials correctly yet.

        :Examples:
            import openalea.plantgl.scenegraph as sg
            scene = sg.Scene()"""
        print("Write "+fname)
        d = alg.Discretizer()
        f = file(fname,'w')

        

        line = '# File generated by PlantGL'
        f.write(line+'\n')

        vertices = [] # List of point List
        normals= [] # List of normal List
        texcoords= [] # List of texture List
        faces = [] # list  of tuple (offset,index List)

        counter = 0
        for i in scene:
            if i.apply(d):
                p = d.discretization
                pts = p.pointList
                ns = p.normalList
                ts = p.texCoordList
                indices = p.indexList
                n = len(p.pointList)
                if n > 0:
                    vertices.append(pts)
                    if ns:
                        normals.append(ns)
                    if ts:
                        texcoords.append(ts)
                    faces.append(Faces(i.name, counter+1, p))
                counter += n

        for pts in vertices:
            for x, y, z in pts:
                f.write('v    %f %f %f\n'%(x, y, z))
            f.write('\n')
        for pts in normals:
            for x, y, z in pts:
                f.write('vn    %f %f %f\n'%(x, y, z))
            f.write('\n')

        for pts in texcoords:
            for x, y in pts:
                f.write('vt    %f %f \n'%(x, y))
            f.write('\n')

        mtl_file = os.path.basename(fname)
        mtl_file = os.path.splitext(mtl_file)[0]+'.mtl'
        f.write('mtllib %s'%(mtl_file))
        for face in faces:
            face.obj(f)

        f.close()
    

codec = VtkCodec()
sg.SceneFactory.get().registerCodec(codec)
