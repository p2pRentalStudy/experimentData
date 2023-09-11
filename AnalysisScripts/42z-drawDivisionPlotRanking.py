from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date

# library
import seaborn as sns
import pandas as pd
import numpy as np



import matplotlib.colors as colors
import numpy as np

def inter_from_256(x):
    return np.interp(x=x,xp=[0,255],fp=[0,1])

# This dictionary defines the colormap
cdict1 = {'green':  ((0.0, 0.0, 0.0),   # no red at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.8, 0.8)),  # set to 0.8 so its not too bright at 1

        'red': ((0.0, 0.8, 0.8),   # set to 0.8 so its not too bright at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.0, 0.0)),  # no green at 1

        'blue':  ((0.0, 0.0, 0.0),   # no blue at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.0, 0.0))   # no blue at 1
       }

cdict2 = {
    'red':((0.0,inter_from_256(64),inter_from_256(64)),
           (1/5*1,inter_from_256(112),inter_from_256(112)),
           (1/5*2,inter_from_256(230),inter_from_256(230)),
           (1/5*3,inter_from_256(253),inter_from_256(253)),
           (1/5*4,inter_from_256(244),inter_from_256(244)),
           (1.0,inter_from_256(169),inter_from_256(169))),
    'green': ((0.0, inter_from_256(57), inter_from_256(57)),
            (1 / 5 * 1, inter_from_256(198), inter_from_256(198)),
            (1 / 5 * 2, inter_from_256(241), inter_from_256(241)),
            (1 / 5 * 3, inter_from_256(219), inter_from_256(219)),
            (1 / 5 * 4, inter_from_256(109), inter_from_256(109)),
            (1.0, inter_from_256(23), inter_from_256(23))),
    'blue': ((0.0, inter_from_256(144), inter_from_256(144)),
              (1 / 5 * 1, inter_from_256(162), inter_from_256(162)),
              (1 / 5 * 2, inter_from_256(246), inter_from_256(146)),
              (1 / 5 * 3, inter_from_256(127), inter_from_256(127)),
              (1 / 5 * 4, inter_from_256(69), inter_from_256(69)),
              (1.0, inter_from_256(69), inter_from_256(69))),
}
# Create the colormap using the dictionary
GnRd = colors.LinearSegmentedColormap('GnRd', cdict1)

# Create a dataset
legendLabels = []
xLabels = []
xticks = []

dataDict = {}
dataDict['Turo'] = {}
dataDict['GetAround'] = {}
dataDict['GerAroundEurope'] = {}


totalAttributes = ['Rating','Rating count', 'Pictures count', 'Review count', 'Owner gender','Milage', 'Make year', '-ve reviews : +ve reviews' , 'Trips count',  'Features count', 'Description words count', 'Vehicles per owner', 'Listed Since', 'allowed miles', 'Repeated Reviewers', 'Category', 'Response time',  'Response rate', 'Verified owner', 'Fuel type', 'Transmission type', 'Faces in DP', 'Color of Vehicle', 'Fuel economy', 'Favorite count', 'Owner member since', 'Owner total trips', 'Onwer rating', 'Pets', 'Smoking', 'Protection plan', 'Days since the last trip', 'Days since the last +ve review', 'Days since the last -ve review']

for platform in ['Turo', 'GetAround', 'GerAroundEurope']:
    for attr in totalAttributes:
        dataDict[platform][attr] = round(random.uniform(-1.5,1.5),2)
# dataDict['GerAroundEurope'][''] = 
# dataDict['GetAround'][''] = 
# dataDict['Turo'][''] = 
dataDict['GerAroundEurope']['Rating'] = -0.05
dataDict['GetAround']['Rating'] = -0.07
dataDict['Turo']['Rating'] = -0.04
dataDict['GerAroundEurope']['Rating count'] = -0.59
dataDict['GetAround']['Rating count'] = -0.2
dataDict['Turo']['Rating count'] = -0.41
dataDict['GerAroundEurope']['Pictures count'] = -0.33
dataDict['GetAround']['Pictures count'] = -0.11
dataDict['Turo']['Pictures count'] = -0.18
dataDict['GerAroundEurope']['Review count'] = -0.67
dataDict['GetAround']['Review count'] = 0
dataDict['Turo']['Review count'] = -0.58
dataDict['GerAroundEurope']['Owner gender'] = 0.23
dataDict['GetAround']['Owner gender'] = -0.16
dataDict['Turo']['Owner gender'] = -0.05
dataDict['GerAroundEurope']['Milage'] = -0.14
dataDict['GetAround']['Milage'] = 0.09
dataDict['Turo']['Milage'] = 0.04
dataDict['GerAroundEurope']['Make year'] = -0.07
dataDict['GetAround']['Make year'] = -0.21
dataDict['Turo']['Make year'] = -0.03
dataDict['GerAroundEurope']['-ve reviews : +ve reviews'] = -0.49
dataDict['GetAround']['-ve reviews : +ve reviews'] = 0.0
dataDict['Turo']['-ve reviews : +ve reviews'] = -0.25
dataDict['GerAroundEurope']['Trips count'] = -0.32
dataDict['GetAround']['Trips count'] = -0.1
dataDict['Turo']['Trips count'] = -0.21
dataDict['GerAroundEurope']['Features count'] = -0.16
dataDict['GetAround']['Features count'] = -0.23
dataDict['Turo']['Features count'] = -0.14
dataDict['GerAroundEurope']['Description words count'] = -0.34
dataDict['GetAround']['Description words count'] = -0.1
dataDict['Turo']['Description words count'] = -0.26
dataDict['GerAroundEurope']['Vehicles per owner'] = -0.44
dataDict['GetAround']['Vehicles per owner'] = 0.5
dataDict['Turo']['Vehicles per owner'] = -0.23
dataDict['GerAroundEurope']['Listed Since'] = -0.14
dataDict['GetAround']['Listed Since'] = 0.13
dataDict['Turo']['Listed Since'] = -0.28
dataDict['GerAroundEurope']['allowed miles'] = 0.06
dataDict['GetAround']['allowed miles'] = 0.34
dataDict['Turo']['allowed miles'] = 0.16
dataDict['GerAroundEurope']['Repeated Reviewers'] = -0.43
dataDict['GetAround']['Repeated Reviewers'] = 0
dataDict['Turo']['Repeated Reviewers'] = -0.22
dataDict['GerAroundEurope']['Category'] = 0.28
dataDict['GetAround']['Category'] = -0.12
dataDict['Turo']['Category'] = 0.04
dataDict['GerAroundEurope']['Response time'] = 0.17
dataDict['GetAround']['Response time'] = 0
dataDict['Turo']['Response time'] = 0.36
dataDict['GerAroundEurope']['Response rate'] = -0.21
dataDict['GetAround']['Response rate'] = 0
dataDict['Turo']['Response rate'] = -0.17
dataDict['GerAroundEurope']['Verified owner'] = -0.33
dataDict['GetAround']['Verified owner'] = -0.26
dataDict['Turo']['Verified owner'] = -0.31
dataDict['GerAroundEurope']['Fuel type'] = 0.08
dataDict['GetAround']['Fuel type'] = 0.3
dataDict['Turo']['Fuel type'] = 0.04
dataDict['GerAroundEurope']['Transmission type'] = -0.21
dataDict['GetAround']['Transmission type'] = 0.14
dataDict['Turo']['Transmission type'] = 0.08
dataDict['GerAroundEurope']['Faces in DP'] = -0.09
dataDict['GetAround']['Faces in DP'] = 0.15
dataDict['Turo']['Faces in DP'] = -0.33
dataDict['GerAroundEurope']['Color of Vehicle'] = -0.11
dataDict['GetAround']['Color of Vehicle'] = 0.43
dataDict['Turo']['Color of Vehicle'] = 0.17
dataDict['GerAroundEurope']['Fuel economy'] = -0.11
dataDict['GetAround']['Fuel economy'] = -0.13
dataDict['Turo']['Fuel economy'] = -0.19
dataDict['GerAroundEurope']['Favorite count'] = 0
dataDict['GetAround']['Favorite count'] = 0
dataDict['Turo']['Favorite count'] = -0.49
dataDict['GerAroundEurope']['Owner member since'] = -0.4
dataDict['GetAround']['Owner member since'] = 0
dataDict['Turo']['Owner member since'] = -0.21
dataDict['GerAroundEurope']['Onwer rating'] = -0.29
dataDict['GetAround']['Onwer rating'] = 0
dataDict['Turo']['Onwer rating'] = -0.36
dataDict['GerAroundEurope']['Owner total trips'] = -0.54
dataDict['GetAround']['Owner total trips'] = 0
dataDict['Turo']['Owner total trips'] = -0.31
dataDict['GerAroundEurope']['Smoking'] = 0.33
dataDict['GetAround']['Smoking'] = 0.41
dataDict['Turo']['Smoking'] = 0.52
dataDict['GerAroundEurope']['Pets'] = 0.27
dataDict['GetAround']['Pets'] = 0.21
dataDict['Turo']['Pets'] = 0.35
#least to max, least in by traveller and max is comprehensive by the owner
dataDict['GerAroundEurope']['Protection plan'] = 0
dataDict['GetAround']['Protection plan'] = 0
dataDict['Turo']['Protection plan'] = -0.12

# 'Days since the last trip', 'Days since the last +ve review', 'Days since the last -ve review']
dataDict['GerAroundEurope']['Days since the last trip'] = 0.21
dataDict['GetAround']['Days since the last trip'] = 0.44
dataDict['Turo']['Days since the last trip'] = 0.27
dataDict['GerAroundEurope']['Days since the last +ve review'] = 0.2
dataDict['GetAround']['Days since the last +ve review'] = 0
dataDict['Turo']['Days since the last +ve review'] = 0.2
dataDict['GerAroundEurope']['Days since the last -ve review'] = 0.15
dataDict['GetAround']['Days since the last -ve review'] = 0
dataDict['Turo']['Days since the last -ve review'] = -0.43


# print(dataDict)

lengthAttrbiutes = len(totalAttributes)
for i in range(1,lengthAttrbiutes+1):
    xLabels.append('V'+str(i))
    legendLabels.append('V'+str(i)+': '+totalAttributes[i-1])
    xticks.append(i-1+.5)

platforms = ['TR', 'GA', 'GA-E']
df = pd.DataFrame(np.random.random((3,lengthAttrbiutes)))
fig, ax = plt.subplots()

# fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)


# dataDict = {
#     'Turo': {'Rating': 0.23, 'Male': -0.8, 'Female': 0.42, 'Review count': 0.22, 'Negative Reviews': -0.63, 'Positive ReviewsTrips count': -0.09, 'Pictures count': 0.19, 'Features': -0.07, 'Description words count': -0.02, 'Vehicles per owner': 0.17, 'Listed Since': 0.71, 'allowed miles': -0.67, 'Repeated Reviewers': -0.87, 'Make year': 0.41, 'pet': -0.27, 'Smoking': 0.17, 'response time': 0.44, 'Verified owner': 0.16, 'Last Trip Recorded': 0.02, 'Last Negative Review': 0.93, 'Last Positive Review': -0.93, 'Fuel type': 0.55, 'Transmission type': 0.26, 'Faces in DP': 0.17, 'Color of Vehicle': -0.12, 'Fuel economy': -0.52, 'Smoking': 0.68, 'Pets': -0.92, 'Favorite count': 0.06, 'Also on Uber': 0.06, 'Owner member since': 0.98, 'Response rate': 0.21, 'Response time': -0.85, 'Owner total trips': -0.57, 'Onwer rating': -0.95, 'carPolicies': -0.84, 'Milage': 0.52}, 
#     'GetAround': {'Rating': 0.18, 'Male': 0.27, 'Female': 0.11, 'Review count': 0.45, 'Negative Reviews': -0.05, 'Positive ReviewsTrips count': -0.52, 'Pictures count': 0.93, 'Features': 0.83, 'Description words count': -0.61, 'Vehicles per owner': -0.88, 'Listed Since': 0.01, 'allowed miles': 0.75, 'Repeated Reviewers': 0.63, 'Make year': -0.98, 'pet': 0.98, 'Smoking': 0.28, 'response time': -0.46, 'Verified owner': 0.69, 'Last Trip Recorded': -0.81, 'Last Negative Review': 0.03, 'Last Positive Review': 0.8, 'Fuel type': -0.03, 'Transmission type': -0.13, 'Faces in DP': -0.24, 'Color of Vehicle': 0.99, 'Fuel economy': -0.7, 'Smoking': -0.27, 'Pets': 0.32, 'Favorite count': 0.93, 'Also on Uber': -0.78, 'Owner member since': -0.3, 'Response rate': 0.45, 'Response time': 0.05, 'Owner total trips': 0.35, 'Onwer rating': -0.66, 'carPolicies': 0.38, 'Milage': 0.76}, 
#     'GerAroundEurope': {'Rating': -0.14, 'Male': -0.42, 'Female': -0.19, 'Review count': -0.16, 'Negative Reviews': -0.45, 'Positive ReviewsTrips count': 0.05, 'Pictures count': -0.3, 'Features': 0.84, 'Description words count': -0.9, 'Vehicles per owner': 0.92, 'Listed Since': 0.65, 'allowed miles': 0.67, 'Repeated Reviewers': -0.32, 'Make year': 0.52, 'pet': 0.97, 'Smoking': 0.82, 'response time': -0.2, 'Verified owner': -0.23, 'Last Trip Recorded': 0.04, 'Last Negative Review': -0.08, 'Last Positive Review': 0.73, 'Fuel type': 0.23, 'Transmission type': -0.68, 'Faces in DP': 0.51, 'Color of Vehicle': 0.12, 'Fuel economy': 0.24, 'Smoking': -0.04, 'Pets': -0.29, 'Favorite count': 0.47, 'Also on Uber': 0.07, 'Owner member since': 0.05, 'Response rate': 0.68, 'Response time': -0.68, 'Owner total trips': -0.15, 'Onwer rating': 0.73, 'carPolicies': 0.92, 'Milage': 0.04}
#     }



cmap = plt.get_cmap(GnRd,30)
cmap.set_under('dimgrey')#Colour values less than vmin in white
cmap.set_over('dimgrey')# colour valued larger than vmax in red

heatmapData = []

for platform in ['Turo', 'GetAround', 'GerAroundEurope']:
    tempList = []
    for i in range(0,len(totalAttributes)):
        tempList.append(dataDict[platform][totalAttributes[i]])
    heatmapData.append(tempList)
        
# Default heatmap


ax = sns.heatmap(heatmapData, cmap=cmap,annot=True,square=True,ax=ax,vmin=-1.05,vmax=1.05,
                    cbar_kws={"shrink": 0.8, "orientation": "horizontal"},linewidths=0.8,linecolor="grey", cbar = False)

for t in ax.texts:
    if float(t.get_text())<=1 and float(t.get_text())>=-1:
        t.set_text(t.get_text()) #if the value is greater than 0.4 then I set the text 
    else:
        t.set_text('') # if not it sets an empty text

# ax.invert_yaxis()
ax.set_xticks(xticks)
ax.set_xticklabels(xLabels,  fontsize=11,  rotation = 45)
ax.set_yticklabels(platforms, fontsize=12, rotation=0)



from matplotlib.lines import Line2D
custom_lines = []
for i in range(0, lengthAttrbiutes):
    custom_lines.append(Line2D([0], [0], color=cmap(0.), lw=1))

ax.legend(custom_lines, legendLabels, fontsize='12',  loc="upper center", bbox_to_anchor=(0.5, 0.95), ncol=5, bbox_transform=fig.transFigure, handlelength=0.3)

fig = plt.gcf()
fig.set_size_inches(15, 4)
fig.tight_layout()


plt.subplots_adjust(left=0.04,
                    bottom=0.02,
                    right=0.97,
                    top=0.5,
                    wspace=0.9,
                    hspace=0.5)

scriptName = '42z'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 