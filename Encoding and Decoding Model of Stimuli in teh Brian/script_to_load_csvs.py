import numpy as np
import pandas as pd

visual_cortex = np.loadtxt('vc.csv')
print(visual_cortex.shape)

# After removing 'rest', 720 is the number of timepoints x number of voxels in visual cortex

v1 = np.loadtxt('v1.csv')
print(v1.shape)

# Similarly, number of voxels in v1 area are less compared to whole visual cortex

v4 = np.loadtxt('v4.csv')
print(v4.shape)

# Corresponding experimental stimuli

stimuli = np.loadtxt('stimuli.csv')
print(stimuli.shape) # Shape is number of timepoints x 10x10 pixels flattened to 100

# plotting
import matplotlib.pyplot as plt

# 239th timepoint - end of geometrical shapes
plt.figure();plt.imshow(stimuli[239].reshape(10, 10), cmap='gray')

# 240th timepoints - start of alphabet
plt.figure();plt.imshow(stimuli[240].reshape(10, 10), cmap='gray')

# Each timepoint has some pattern either geometric or alphabet
# This will tell you which timepoint corresponds to which pattern in geometric or alphabet

conditions = pd.read_csv('conditions.csv', header=None).to_numpy().squeeze()
print(conditions.shape)
