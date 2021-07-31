import numpy as np
from scipy import stats
#mean
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
#median
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.median(speed)

#mode
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)

print(x)