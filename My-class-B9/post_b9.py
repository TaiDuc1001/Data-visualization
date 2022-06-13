import matplotlib.pyplot as plt
import numpy as np

re_0, cmt_0, share_0 =  36,  7, 1
re_1, cmt_1, share_1 =  73, 22, 3
re_2, cmt_2, share_2 =  62, 10, 2
re_3, cmt_3, share_3 =  27,  2, 0
re_4, cmt_4, share_4 =  63, 23, 6
re_5, cmt_5, share_5 =  24,  7, 1
re_6, cmt_6, share_6 =  16,  1, 1
re_7, cmt_7, share_7 =  53,  7, 1
re_8, cmt_8, share_8 =  90, 20, 4
re_9, cmt_9, share_9 =  158,29, 15

likes= [9, 41,20,14,23, 6,18,36,56,71]
tyms = [2, 18, 2, 1,17, 1,10,16,30,50]
oms  = [0,  0, 0, 0, 0, 0, 0, 0, 0, 0]
hahas= [20,12,21, 2,15,11, 0, 0, 6,33]
sads = [5,  5, 1,20, 5, 5, 0, 0, 1, 6]
wows = [0,  3, 1, 0, 3,11, 0, 0, 1, 1]
phan = [0,  0, 0, 0, 0, 1, 0, 0, 0, 0]

colors = ['#19232D'  ,'red'     ,'blue'   ,'white','yellow'    ,'green',
		  'turquoise','lavender','brown'  ,'cyan' ,'dodgerblue',
		  '#08F7FE'  ,'#09FBD3' ,'#FE53BB','#F5D300']
neons = ['#7122FA','#560A86','#F148FB','#FFACFC','#75D5FD','#FF2281','blue']


reacts   = [re_0    , re_1  ,re_2   ,re_3   ,re_4   ,re_5   ,re_6   ,re_7   ,re_8   ,re_9   ]
comments = [cmt_0   ,cmt_1  ,cmt_2  ,cmt_3  ,cmt_4  ,cmt_5  ,cmt_6  ,cmt_7  ,cmt_8  ,cmt_9  ]
shares   = [share_0 ,share_1,share_2,share_3,share_4,share_5,share_6,share_7,share_8,share_9]


days = ['Day0','Day1','Day2','Day3','Day4','Day5','Day6','Day7','Day8','Day9']


def make_plot_total():
	numbers = np.arange(0,len(reacts))
	plt.style.use('dark_background')
	plt.plot(numbers, reacts  , color = colors[13], label = 'Reacts'  ,marker = 'D')
	plt.plot(numbers, shares  , color = colors[11], label = 'Shares'  ,marker = 'D')
	plt.plot(numbers, comments, color = colors[14], label = 'Comments',marker = 'D')
	plt.xlabel('The days'                             ,font='monospace',fontsize = 15,color= colors[3])
	plt.ylabel('Number of interactions'               ,font='sans'     ,fontsize = 15,color= colors[3])
	plt.title(f"Reactions of last {len(reacts)} posts",font = "serif"  ,fontsize = 20,color= colors[3])
	plt.xticks(numbers,days,fontsize = 12, rotation=45)
	plt.yticks(fontsize = 12  )
	plt.legend(fontsize = 10.5)
	plt.grid()
	plt.show()
make_plot_total()

def make_plot_small():
	numbers = np.arange(0,len(reacts))
	plt.style.use('dark_background')
	plt.plot(numbers, likes, color = colors[13], label = 'Likes',marker = 'D')
	plt.plot(numbers, tyms , color = colors[11], label = 'Loves',marker = 'D')
	plt.plot(numbers, hahas, color = colors[14], label = 'Haha' ,marker = 'D')
	#plt.plot(numbers, oms, color = colors[12], label = 'Thuong Thuong',marker = 'D')
	#plt.plot(numbers, sads, color = colors[10], label = 'Sads',marker = 'D')
	#plt.plot(numbers, wows, color = colors[9], label = 'Wows',marker = 'D')
	#plt.plot(numbers, phan, color = colors[8], label = 'Angry',marker = 'D')
	plt.xlabel('The days'              ,font='monospace',fontsize = 15,color= colors[3])
	plt.ylabel('Number of interactions',font='sans'     ,fontsize = 15,color= colors[3])
	plt.title("Event's Growth Chart"   ,font = "serif"  ,fontsize = 20,color= colors[3])
	plt.xticks(numbers,days,fontsize = 12, rotation=45)
	plt.yticks(fontsize = 12)
	plt.legend(fontsize = 10.5)
	plt.grid()
	plt.show()	
make_plot_small()

def plots():
	numbers = np.arange(0,len(reacts))
	plt.style.use('dark_background')
	fig, ax = plt.subplots(figsize = (7,5))
	
	ax.plot(numbers, reacts  , color = colors[13], label = 'Reacts'  ,marker = 'D')
	ax.plot(numbers, shares  , color = colors[11], label = 'Shares'  ,marker = 'D')
	ax.plot(numbers, comments, color = colors[14], label = 'Commemts',marker = 'D')
	plt.xticks(numbers,days,fontsize = 12,rotation = 45)
	plt.xlabel('The days'    ,font='monospace',fontsize = 18,color= colors[3])
	plt.ylabel('Interactions',font='sans'     ,fontsize = 18,color= colors[3])

	inner_ax = fig.add_axes([0.375,0.533,0.385,0.27])
	inner_ax.plot(numbers, likes, color = colors[13], label = 'Likes',marker = 'D')
	inner_ax.plot(numbers, tyms , color = colors[11], label = 'Loves',marker = 'D')
	inner_ax.plot(numbers, hahas, color = colors[14], label = 'Haha' ,marker = 'D')
	inner_ax.set(title = 'Like,Love,Haha',xticks = (np.arange(1,8)))
	#inner_ax.xticks(numbers,days,fontsize = 12)
	inner_ax.legend(fontsize = 9, loc = 'upper center')
	inner_ax.grid()
	
	#ax.xlabel('The days',font='monospace',fontsize = 15,color= colors[3])
	#ax.ylabel('Number of interactions',font='sans',fontsize = 15,color= colors[3])
	ax.set_title(f"Reactions of last {len(reacts)} posts",color= colors[3],font = "serif",fontsize = 20)
	#ax.xticks(numbers,days,fontsize = 12)
	#ax.yticks(fontsize = 12)
	ax.grid()
	ax.legend(fontsize = 10)	
	plt.xticks(numbers,days,fontsize = 8,rotation = 45)
	plt.show()
plots()

























