import requests
import json
import time
from collections import OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = 'https://www.facebook.com/'
url_1 = 'https://coronavirus-19-api.herokuapp.com/all'
url_2 = 'https://www.facebook.com/profile.php?id=100053951509859'
url_3 = 'https://covidapi.info/api/v1/country/VNM'
r = requests.get(url_3)

Confirmers = []
Dates = []
Deaths = []
Recovers = []
data = r.json()['result']
for i in range(len(data)):
	date  = list(OrderedDict(sorted(data.items())))[i]
	info = data[date]
	# print(f"Date: {date} \nConfirmed: {info['confirmed']} \nDeaths: {info['deaths']} \nRecovered: {info['recovered']}")
	# print("=================")
	date = date[5:10].replace('-', '/')
	Dates.append(date)
	Deaths.append(info['deaths'])
	Recovers.append(info['recovered'])
	Confirmers.append(info['confirmed'])
#print(Dates[:][5:10].replace('-', '/'))
# print(Confirmers)

colors = ['#19232D','red','blue','white','yellow','green',
		  'turquoise','lavender','brown','cyan','dodgerblue',
		  '#08F7FE','#09FBD3','#FE53BB','#F5D300']

def make_plot_bar():
	day = np.arange(0,len(Dates))
	bar_width = 1
	plt.bar(day,Confirmers, width = bar_width, color = 'blue', label = 'Cases')
	plt.bar(day + bar_width*2,Recovers,  width = bar_width, color = 'green', label = 'Recovered' )
	plt.bar(day + bar_width,Deaths,  width = bar_width, color = 'red', label = 'deaths' )
	#plt.xticks( day + bar_width/576, Dates, rotation = 45, fontsize = 7.5 )
	plt.ylabel('Cases')
	plt.xlabel('Date')
	plt.title(f'Covid19 Vietnam Statics from {Dates[0]} to {Dates[-1]}')
	plt.legend()
	#plt.xlim([0,100])
	#plt.ylim([0,10000])
	plt.grid()
	plt.show()
make_plot_bar()

def make_plot_hist1():
	day = np.arange(0,len(Dates))
	plt.hist(Recovers,bins = 500, color = 'blue', label = 'Cases')
	#plt.bar(day + bar_width*2,Recovers,  width = bar_width, color = 'green', label = 'Recovered' )
	plt.ylabel('Cases')
	plt.xlabel('Date')
	plt.title(f'Covid19 Vietnam Statics from {Dates[0]} to {Dates[-1]}')
	plt.legend()
	plt.show()
make_plot_hist1()
	
def make_plot_line1():
	day = np.arange(0,len(Dates))
	bar_width = 1
	plt.style.use('dark_background')
	plt.plot(day,Confirmers, color = colors[13], label = 'Confirmed')
	plt.plot(day,Recovers, color = colors[11], label = 'Recovers')
	plt.plot(day,Deaths, color = colors[4], label = 'Deaths')
	#plt.bar(day + bar_width*2,Recovers,  width = bar_width, color = 'green', label = 'Recovered' )
	plt.ylabel('Cases')
	plt.xlabel('Date')
	#plt.xticks( day + bar_width/576, Dates, rotation = 45, fontsize = 7.5 )
	plt.title(f'Covid19 Vietnam Statics from {Dates[0]} to {Dates[-1]}')
	plt.legend()
	#plt.xlim([60,80])
	#plt.ylim([0,400])
	#plt.grid()
	plt.show()

make_plot_line1()

def make_plot_scatter():
	day = np.arange(0,len(Dates))
	bar_width = 1
	plt.style.use('grayscale')
	fig, ax = plt.subplots()
	plt.scatter(day,Confirmers, color = 'red', label = 'Confirmed',
			 cmap = 'Reds',alpha = 0.3,s = 150)
	plt.scatter(day,Recovers, color = 'green', label = 'Recovers',alpha = 0.2,s = 100)
	plt.scatter(day,Deaths, color = 'blue', label = 'Deaths',alpha = 0.4,s = 130)
	#plt.bar(day + bar_width*2,Recovers,  width = bar_width, color = 'green', label = 'Recovered' )
	plt.ylabel('Cases', fontsize = 13)
	plt.xlabel('Date', fontsize = 13)
	plt.xticks( day + bar_width/576, Dates, rotation = 45, fontsize = 7.5 )
	plt.title(f'Covid19 Vietnam Statics from {Dates[0]} to {Dates[-1]}', fontsize = 13)
	plt.legend(framealpha = 0.2,borderpad = 0.8)
	plt.colorbar()
	plt.xlim([60,80])
	plt.ylim([0,400])
	plt.grid()
	plt.show()

make_plot_scatter()


    


















