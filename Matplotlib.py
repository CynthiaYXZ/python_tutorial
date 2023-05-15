import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
fontP = font_manager.FontProperties()
fontP.set_family('SimHei')
fontP.set_size(14)

# 1. Input
#line
#xpoint = np.array([2,4,9])
#ypoint = np.array([3,6,10])

#pie chart
#y=np.array([35,25,25,15])

#scatterplot
#x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
#y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

#Histogram
x=np.random.normal(90,10,100)


# 2. Process

# 3. Output
plt.title("Histogram Plot: 姚小珍",fontproperties=fontP)
plt.xlabel("Distribution")
plt.ylabel("Score")

#line
#plt.plot(xpoint, ypoint)

#pie
#plt.pie(y)

#scatterplot
#plt.grid()
#plt.scatter(x,y)

#histogram
plt.xlim([0,100])
plt.hist(x)


plt.show()