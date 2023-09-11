from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


# READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES

totalCategories = ['suv', 'hatchback', 'sedan', 'coupe', 'truck', 'van/minivan', 'wagon']

import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

uniform_data = np.random.rand(15, 6)
ax = sns.heatmap(uniform_data, linewidth=0.5)


scriptName = '11b'

fig = plt.gcf()
fig.set_size_inches(4, 4)

fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 
