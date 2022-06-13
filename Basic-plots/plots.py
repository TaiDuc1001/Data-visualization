import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import pandas as pd
# from tkinter import *

month = ['Jan','Feb','Mar','April','May','June','July','Aug','Sep','Oct','Nov','Dec']
customer1 = [12,13,9,8,7,8,8,7,6,5,8,10]
customer2 = [14,16,11,7,6,6,7,6,5,8,9,12]

# tk = Tk()
# #tk.title("Einstein")
# tk.geometry("550x250")
# tk.configure(background='lavender')

def button():
	Button(tk, text = "plot"   , width = 5, bg = "lavender", command = plot).place(x = 10,y= 22)
	Button(tk, text = "bar"    , width = 5, bg = "lavender", command = bar).place(x = 10,y= 51)
	Button(tk, text = "scatter", width = 5, bg = "lavender", command = scatter).place(x = 10,y= 80)
	Button(tk, text = "hist"   , width = 5, bg = "lavender", command = hist).place(x = 10,y= 110)
	Button(tk, text = "box"    , width = 5, bg = "lavender", command = box).place(x = 10,y= 161)

def plot():
	plt.plot(month, customer1, color = "royalblue", label = "customer1", marker = "h")
	plt.plot(month, customer2, color = "tomato", label = "customer2", marker = "D")
	plt.xlabel("month")
	plt.ylabel("electricity consumption")
	plt.title("Line Chart")
	plt.legend()
	plt.grid()
	plt.show()

def bar():
	month_n = np.arange(1,13)
	bar_width = 0.4
	plt.bar(month_n,customer1, width = bar_width, color = 'blue', label = 'customer1')
	plt.bar(month_n + bar_width, customer2, width = bar_width, color = 'red', label = 'customer2' )
	plt.xticks(month_n + bar_width/12, ('Jan','Feb','Mar','April','May','June','July','Aug','Sep','Oct','Nov','Dec'))
	plt.xlabel('month')
	plt.ylabel('Electricity consumption')
	plt.title('Bar Chart')
	plt.legend()
	plt.show()

def scatter():
	plt.scatter(month, customer1, color = 'royalblue', label='customer1',marker = 'D')
	plt.scatter(month,customer2, color = 'tomato', label = 'customer2', marker = 'D')
	plt.xlabel('Month')
	plt.ylabel('Electricity consumption')
	plt.title('Scatter of Buildings Consumption')
	plt.legend()
	plt.grid()
	plt.show()

def hist():
	plt.hist(customer1, bins = 21, color = 'green')
	plt.xlabel('month')
	plt.ylabel('customer1')
	plt.title('histogram')
	plt.show()

def box():
	plt.boxplot([ customer1, customer2],patch_artist=True, boxprops= dict(facecolor = 'yellow',color = 'red'), whiskerprops=dict(color = 'navy'), capprops=dict(color = 'red'), medianprops=dict(color = 'red'))      
	plt.grid()
	plt.show()

# button()
x = True
while True:
	c = input("nhap vao(scatter, hist, box, bar, plot): ")
	if c == "scatter":
		scatter()
	elif c == "hist":
		hist()
	elif c == "box":
		box()
	elif c == "bar":
		bar()
	elif c == "plot":
		plot()
	else:
		break
# tk.mainloop()







