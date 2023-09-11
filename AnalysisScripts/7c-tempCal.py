# importing the modules
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
  
# generating 2-D 10x10 matrix of random numbers
# from 1 to 100
# data = np.random.randint(low = 1,
#                          high = 100,
#                          size = (10, 10))
# print("The data to be plotted:\n")
# print(data)
 
ietc = 0
for i in range(720):
    for j in range(1,1501,4):
        ietc += 1

for i in range(720):
    for j in range(1,1501,17):
        ietc += 1

# ietc += 720
print(ietc)