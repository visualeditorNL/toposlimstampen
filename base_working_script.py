from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#import shapefile as shp
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
import numpy as np

map = Basemap()

sh = map.readshapefile("ne_110m_admin_0_countries/ne_110m_admin_0_countries","landen")
map.fillcontinents(color='lightgrey', alpha=0.5, lake_color='white')

countries = [r['NAME_NL'] for r in map.landen_info]
countries = list(dict.fromkeys(countries))


for i in countries:
    fig = plt.figure(figsize=(16,8))
    ax  = fig.add_subplot(111)
    
    map = Basemap()

    sh = map.readshapefile("ne_110m_admin_0_countries/ne_110m_admin_0_countries","landen")
    map.fillcontinents(color='lightgrey', alpha=0.5, lake_color='white')
    
    patches = []
    for info, shape in zip(map.landen_info, map.landen):
        if info['NAME_NL'] == str(i):
            patches.append(Polygon(np.array(shape), True))
            print(str(i), patches)
        patchcol = PatchCollection(patches, facecolor= 'g', edgecolor='k', linewidths=1., zorder=2)
        ax.add_collection(patchcol)

         
    naam = f'{i}{".png"}'

    fig.savefig(naam, dpi=100)
    patchcol.remove()
    fig.canvas.draw_idle()
    fig.clf()
