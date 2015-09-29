import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.colors import rgb2hex

file_path = 'C:\\Users\\graham\\Desktop\\DataScience\\'
file_name = 'StateParticipationCsv.csv'
data_set = np.recfromcsv(file_path + file_name, delimiter=',')

state_rates = np.rec.fromarrays((data_set.state, (data_set.count/data_set.pop)), names=('state', 'rate'))

#get mean line
mean = np.mean(state_rates.rate)

#get standard deviation
stddev = np.std(state_rates.rate)

participation_min = state_rates.rate[state_rates.rate.argmin()]
participation_max = state_rates.rate[state_rates.rate.argmax()]
participation_range = participation_max - participation_min

# create the map
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
# load the shapefile, use the name 'states'
map.readshapefile(file_path + 'st99_d00', name='states', drawbounds=True)

# collect the state names from the shapefile attributes so we can
# look up the shape obect for a state by its name
state_names = [shape_dict['NAME'] for shape_dict in map.states_info]

colors={}
statenames=[]
cmap = plt.cm.RdBu # use 'red-blue' colormap

for state_info in state_rates:
    divisor = participation_max + state_info.rate 
    operator = -1.0*(state_info.rate)/(mean)
    colors[state_info.state] = cmap(1.+ operator*np.sqrt((state_info.rate-participation_min)/divisor))[:3] #participation_min
    print state_info.state, 1.+ operator*np.sqrt((state_info.rate-participation_min)/divisor)

ax = plt.gca() # get current axes instance

# draw filled state polygons
for nshape,seg in enumerate(map.states):
    if state_names[nshape] != 'Puerto Rico':
        color = rgb2hex(colors[state_names[nshape]]) 
        poly = Polygon(seg,facecolor=color,edgecolor=color)
        ax.add_patch(poly)

plt.title('Participation by State')
plt.show()
