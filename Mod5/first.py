import matplotlib.pyplot as plt

years= [1903, 1912, 1915, 1916, 1918, 2004, 2007, 2013]
yanks_hr=[18,18,31,35,20,242,201,144]
homeRuns = [48,29,14,14,15,222,166,178]

# Function to plot
plt.plot(years,homeRuns,'r-o',label='Bo xox Homers')
plt.plot(years,yanks_hr,'b-X',label='Yanks Homers')

# function to show the plot
plt.legend()
plt.show()
