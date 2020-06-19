import numpy as np
from numpy import random
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns
sns.set()

def draw_heatmap():
      N = 5
      R = random.randn(N,N)
      fig = plt.figure()
      sns_plot = sns.heatmap(R, annot=True)
      plt.show()

draw_heatmap()
      
