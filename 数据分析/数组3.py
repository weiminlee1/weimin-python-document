import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#####################
##Series
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()
##plt.plot(x=,y=)

#########################
##DataFrame
data = pd.DataFrame(np.random.randn(1000,4), index=np.arange(1000),
columns=list('ABCD')
