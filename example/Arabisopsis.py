
# In[1]:

get_ipython().magic(u'matplotlib inline')
get_ipython().magic(u'gui qt')
#from vpltkdisplay import *
from arabido import data, plant3d


# In[2]:

fn = '../share/Arabido.txt'
df = data.read(fn)


# In[3]:

df


# In[4]:

dfg = df.groupby('plant')
dfg.plot(x='init_time', y='phy')


# In[5]:

g = plant3d.dynamic_mtg(df)
#g.display()


# In[6]:

plants = g.vertices(scale=1)
#plants


# In[8]:

for i in range(0,600):
    scene = plant3d.plot3d_with_time(g,plants[0], time=i)
    Viewer.display(scene)
#display(PlantGL(scene))


# In[9]:

for i in range(0,600):
    scene = plant3d.plot3d_with_time(g,plants[1], time=i)
    Viewer.display(scene)
#display(PlantGL(scene))


# In[16]:

from alinea.caribu.CaribuScene import CaribuScene
import alinea.caribu.sky_tools.turtle as sky_turtle


# In[20]:

energy, emission, direction, elevation , azimuth  = sky_turtle.turtle()
lights = zip(energy,direction)
c_scene = CaribuScene()
idmap = c_scene.add_Shapes(scene)
#idmap = c_scene.add_Shapes(lscene)
c_scene.addSources(lights)
#output = c_scene.runCaribu(infinity=False)
#c_res = c_scene.output_by_id(output, idmap)['Einc']


# In[ ]:



