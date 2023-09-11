# importing the modules
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt


data = []

cities = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.', 'London', 'Liverpool']
cityShorty = ['LVX', 'LAX', 'MIA', 'NYC', 'WDC', 'LDN', 'LPL']
tG = [22/4905, 361/17710,103/9761, 236/10232, 118/5710, 0,0]
tE = [0,0,0,0,0,52/3610, 8/360]

totalOv = []
totalV = []

data = [tG,tE]
for i in range(0,len(data)):
    for j in range(0,len(data[i])):
        data[i][j] = round(data[i][j]*100,2)
# plotting the heatmap

for i in range(0,len(data)):
    for j in range(0,len(data[i])):
        if data[i][j] != 0:
            totalOv.append(data[i][j])
print(np.average(totalOv))
# sn.set(font_scale = 1.2)

hm = sn.heatmap(data = data, xticklabels=cityShorty, yticklabels=['TR-GA','TR-GRE'], annot=True,linewidth=.5,cmap='gist_gray_r', cbar_kws={"orientation": "horizontal", "pad": 0.3},  annot_kws={"fontsize":19},cbar=False)

hm.set_yticklabels(['TR-GA','TR-GRE'], size = 14, rotation=30)
hm.set_xticklabels(cityShorty, size = 14, rotation=30)

# displaying the plotted heatmap
# plt.show()

fig = plt.gcf()
fig.set_size_inches(7, 2.4)

plt.title('Percentage of Overlaping Vehicles', size = 15)

# hm.set(xlabel="Cities", ylabel='PRVPs Pair',  weight='bold')

hm.set_xlabel('Cities', size = 15)
hm.set_ylabel('Platform Pairs',weight = 'bold',size = 15 )

# hm.set_ylabel(hm.get_ylabel(), fontdict={'weight': 'bold'})
# hm.set_xlabel(hm.get_xlabel(), fontdict={'weight': 'bold'})

plt.subplots_adjust(left=0.18,
                    bottom=0.32,
                    right=0.98,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)

scriptName = '7b'
fig.savefig('plots/'+scriptName+'.png')
fig.savefig('plots/'+scriptName+'.eps')
