import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\Graham\\Desktop\\DataScience\\'
file_name = 'ParticipationCsv.csv'
data_set = np.recfromcsv(file_path + file_name, delimiter=',')

state_rates = np.rec.fromarrays((data_set.state, (data_set.count/data_set.pop)), names=('state', 'rate'))


N = len(state_rates.state)
ind = np.arange(N)
width = 0.7

fig = plt.figure() 
ax = fig.add_subplot(111)

#get mean line
mean = np.mean(state_rates.rate)
means = [mean for x in state_rates]

#get standard deviation
stddev = np.std(state_rates.rate)

stddevs = [stddev for x in state_rates.rate]

#get below means
below_mean_rates = [x if x < mean else 0 for x in state_rates.rate]
above_mean_rates = [x if x > mean else 0 for x in state_rates.rate]

#states with higher than average participation
above_mean_rects = ax.bar(ind, above_mean_rates, width,
                          color='r',
                          align='center')
#mean participation
opacity = 0.5
meanrects = ax.bar(ind, means, width, 
                   alpha=opacity,
                   yerr=stddevs,
                   color='y',
                   align='center')

#below average participation
below_mean_rects = ax.bar(ind, below_mean_rates, width, 
                color='blue',
                align='center')

plt.legend((below_mean_rects[0], meanrects[0], above_mean_rects[0]), ('State with Less than Average Participation', 'Mean # Users', 'State with Above Average Participation'))
#rects = ax.bar(ind, state_rates.rate, width, 
#                color='blue',
#                align='center')

ax.set_xlim(-width, len(ind)+width)
ax.set_ylim(5, state_rates.rate.max() + 5)

#labels
plt.xticks(ind, state_rates.state)
plt.title('Participation By State')
plt.ylabel('Participants Per Million Residents')
plt.xlabel('States')

plt.show()

















