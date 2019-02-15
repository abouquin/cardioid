import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import random
# FOR GREEK LETTERS
from matplotlib import rc
rc('text', usetex=True)
font = {'family'    : 'sans-serif',
		'style'     : 'normal',
        'weight'    : 'normal',
        'size'      : 12,
        'sans-serif': 'Verdana'
        }
rc('font', **font)


def f(num_var, tab_var):
	# CREATE FIGURE
	fig = plt.figure(num=None, figsize=(8, 8), facecolor='k', edgecolor='k')
	ax1 = fig.add_subplot(111)
	plt.axis('off')
	color = "#%06x" % random.randint(0, 0xFFFFFF)	#random

	# DRAW CIRCLE
	th = np.arange(-np.pi,np.pi,0.01)
	ax1.plot( np.cos(th), np.sin(th), color="black")

	xmin = -1
	xmax = 1
	ymin = -1
	ymax = 1
	ax1.set_xlim(xmin,xmax)
	ax1.set_ylim(ymin,ymax)

	# DRAW POINTS
	num = num_var
	table = tab_var			### PLAY HERE, TRY these: 2=cardioid, 3=nephroid, 34, 51, 99

	position = []
	for idx in range(num):
		theta = 2*np.pi*idx/num
		x = np.cos(theta)
		y = np.sin(theta)
		# ax1.scatter(x,y, s=50, color='red', marker='o')
		point = (x,y)
		position.append(point)

	# print position

	for idx in range(num):
		multip = (idx * table) % num
		theta2 = 2*np.pi * multip /num
		x2 = np.cos(theta2)
		y2 = np.sin(theta2)

		# print multip
		if 0<=multip< num:
			# print position[idx][1]
			# print position[multip][1]
			# first = [position[idx][0], position[multip][0]]
			# second = [position[idx][1], position[multip][1]]
			first = [position[idx][0], x2]
			second = [position[idx][1], y2]
			ax1.plot(first, second, color=color)
			ax1.text(0.75, 1, r'Points='+str(num)+'\n Table='+str(tab_var), color='w', horizontalalignment='left', verticalalignment='center', transform = ax1.transAxes, fontsize=18)
	filename = 'sequence3/table' + "%05d" % (tab_var*10)+ '.png'
	fig.savefig(filename, facecolor=fig.get_facecolor(), edgecolor='none')
	plt.close(fig)

# lim = np.arange(1, 200.1, 0.1)
# for idx, val in enumerate(lim):
# 	print val
# 	f(200, val)

f(200,200.0)