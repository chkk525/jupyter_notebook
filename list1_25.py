import os
import numpy as np
from matplotlib import pyplot as plt, rcParams, matplotlib_fname
matplotlib_fname()

# font_manager._rebuild()

font_dir = '/Users/chikaki/Library/Fonts'

# font_path = os.path.join(font_dir, 'SourceHanCodeJP-Regular.otf')
# font = font_manager.FontProperties(fname=font_path, size=14)

rcParams['font.sans-serif'] = 'Source Han Code JP'
rcParams['font.weight'] = 'regular'
rcParams['axes.titlesize'] = 15
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12

np.random.seed(0)
x = range(5)

y = 10 +  5 * np.random.randn(5)
fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title('にほんごを指定')
ax.bar(x,y)
plt.show()

#Box
