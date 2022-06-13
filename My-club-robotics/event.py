import matplotlib.pyplot as plt
import numpy as np


re_0, cmt_0, share_0 = 108,  2, 57
re_1, cmt_1, share_1 =  56,  4, 35
re_2, cmt_2, share_2 =  38,  4,  8
re_3, cmt_3, share_3 =  21,  1,  8
re_4, cmt_4, share_4 =  77, 36, 13
re_5, cmt_5, share_5 =  18,  0,  7
re_6, cmt_6, share_6 =  21,  2,  6

likes= [72,38,16,11,20,12,11]
tyms = [31,12,12,6,17,5,7]
oms  = [3,0,2,0,1,0,0]
hahas= [1,1,6,3,7,0,1]
sads = [0,2,1,0,0,0,0]
wows = [1,3,1,0,1,1,1]



reacts = [re_0, re_1,re_2,re_3,re_4,re_5,re_6]
comments = [cmt_0,cmt_1,cmt_2,cmt_3,cmt_4,cmt_5,cmt_6]
shares = [share_0,share_1,share_2,share_3,share_4,share_5,share_6]

days = ['Day0','Day1','Day2','Day3','Day4','Day5','Day6']

colors = ['#19232D','red','blue','white','yellow','green',
		  'turquoise','lavender','brown','cyan','dodgerblue',
		  '#08F7FE','#09FBD3','#FE53BB','#F5D300']
neons = ['#7122FA','#560A86','#F148FB','#FFACFC','#75D5FD','#FF2281','blue']
def make_plot_small():
	numbers = np.arange(0,7)
	plt.style.use('dark_background')
	plt.plot(numbers, likes, color = colors[13], label = 'Likes',marker = 'D')
	plt.plot(numbers, tyms, color = colors[11], label = 'Loves',marker = 'D')
	plt.plot(numbers, hahas, color = colors[14], label = 'Haha',marker = 'D')
	# plt.plot(numbers, oms, color = colors[12], label = 'Thuong Thuong',marker = 'D')
	# plt.plot(numbers, sads, color = colors[10], label = 'Sads',marker = 'D')
	# plt.plot(numbers, wows, color = colors[9], label = 'Wows',marker = 'D')
	plt.xlabel('The days',font='monospace',fontsize = 15,color= colors[3])
	plt.ylabel('Number of interactions',font='sans',fontsize = 15,color= colors[3])
	plt.title("Event's Growth Chart",color= colors[3],font = "serif",fontsize = 20)
	plt.xticks(numbers,days,fontsize = 12)
	plt.yticks(fontsize = 12)
	plt.legend(fontsize = 10.5)
	plt.grid()
	plt.show()	
make_plot_small()

def make_plot_total():
	numbers = np.arange(0,7)
	plt.style.use('dark_background')
	plt.plot(numbers, reacts, color = colors[13], label = 'Reacts',marker = 'D')
	plt.plot(numbers, shares, color = colors[11], label = 'Shares',marker = 'D')
	plt.plot(numbers, comments, color = colors[14], label = 'Commemts',marker = 'D')
	plt.xlabel('The days',font='monospace',fontsize = 15,color= colors[3])
	plt.ylabel('Number of interactions',font='sans',fontsize = 15,color= colors[3])
	plt.title("Event's Growth Chart",color= colors[3],font = "serif",fontsize = 20)
	plt.xticks(numbers,days,fontsize = 12)
	plt.yticks(fontsize = 12)
	plt.legend(fontsize = 10.5)
	plt.grid()
	plt.show()
make_plot_total()

def plots():
	numbers = np.arange(0,7)
	plt.style.use('dark_background')
	fig, ax = plt.subplots(figsize = (7,5))
	
	ax.plot(numbers, reacts, color = colors[13], label = 'Reacts',marker = 'D')
	ax.plot(numbers, shares, color = colors[11], label = 'Shares',marker = 'D')
	ax.plot(numbers, comments, color = colors[14], label = 'Commemts',marker = 'D')
	plt.xticks(numbers,days,fontsize = 12,rotation = 0)
	plt.xlabel('The days',font='monospace',fontsize = 15,color= colors[3])
	plt.ylabel('Interactions',font='sans',fontsize = 15,color= colors[3])

	inner_ax = fig.add_axes([0.3,0.55,0.285,0.27])
	inner_ax.plot(numbers, likes, color = neons[5], label = 'Likes',marker = 'D')
	inner_ax.plot(numbers, tyms, color = neons[4], label = 'Loves',marker = 'D')
	inner_ax.plot(numbers, hahas, color = neons[3], label = 'Haha',marker = 'D')
	inner_ax.set(title = 'Like,Love,Haha',xticks = (np.arange(1,8)))
	#inner_ax.xticks(numbers,days,fontsize = 12)
	inner_ax.legend(fontsize = 6.5)
	inner_ax.grid()
	
	#ax.xlabel('The days',font='monospace',fontsize = 15,color= colors[3])
	#ax.ylabel('Number of interactions',font='sans',fontsize = 15,color= colors[3])
	ax.set_title("Event's Growth Chart",color= colors[3],font = "serif",fontsize = 20)
	#ax.xticks(numbers,days,fontsize = 12)
	#ax.yticks(fontsize = 12)
	ax.grid()
	ax.legend(fontsize = 10.5)	
	plt.xticks(numbers,days,fontsize = 7,rotation = 45)
	plt.show()
plots()
























