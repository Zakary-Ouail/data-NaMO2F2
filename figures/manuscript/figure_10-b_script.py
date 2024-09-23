#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.patches as mpatches
from matplotlib.ticker import MultipleLocator
import statsmodels.api as sm
plt.style.use("default") # set the plot style
plt.rcParams["font.family"] = "Times New Roman" # To globaly change the font POLICE
plt.rcParams["font.weight"] = "bold" # To write all font in bold
plt.rcParams["axes.labelweight"] = "bold" # To write all labels in bold

###############################################################################################################################
###########################################< Section n °1 : loading and plotting DATA >########################################
###############################################################################################################################

# loading the "to be used DATA"
data_1 = np.loadtxt("figure_10-b_NaNbO2F2_data.txt", skiprows = 1)
data_2 = np.loadtxt("figure_10-b_NaTaO2F2_data.txt", skiprows = 1)

# Defining figure area and plotting data with y-errorbars on each data point

# DATA n°1
f, axis = plt.subplots(3, 2, figsize=(8, 10), sharex=True)
axis[0, 0].errorbar(data_1[:, 0], data_1[:, 1], yerr = data_1[:, 2], fmt = 'o', linewidth = .8,
             elinewidth = 1, ecolor = 'k', color = 'r', capsize = 4, ms = 5, mec = 'k')
axis[1, 0].errorbar(data_1[:, 0], data_1[:, 5], yerr = data_1[:, 6], fmt="o", linewidth = .8, 
            elinewidth = 1, ecolor='k', color = 'r', capsize = 4, ms = 5, mec = 'k')
axis[2, 0].errorbar(data_1[:, 0], data_1[:, 7], yerr = data_1[:, 8], fmt = "o", linewidth = .8, 
             elinewidth = 1, ecolor = 'k', color = 'r', capsize = 4, ms = 5, mec = 'k')

# DATA n°2
axis[0, 1].errorbar(data_2[:, 0], data_2[:, 1], yerr = data_2[:, 2], fmt = 'o', linewidth = .8,
                    elinewidth = 1, ecolor = 'k', color = 'c', capsize = 4, ms = 5, mec = 'k')
axis[1, 1].errorbar(data_2[:, 0], data_2[:, 5], yerr = data_2[:, 6], fmt = 'o', linewidth = .8,
                    elinewidth = 1, ecolor = 'k', color = 'c', capsize = 4, ms = 5, mec = 'k')
axis[2, 1].errorbar(data_2[:, 0], data_2[:, 7], yerr = data_2[:, 8], fmt = "o", linewidth = .8, 
             elinewidth = 1, ecolor = 'k', color = 'c', capsize = 4, ms = 5, mec = 'k')

# Setting axis twins
ax00 = axis[0, 0].twinx()
ax10 = axis[1, 0].twinx()
ax20 = axis[2, 0].twinx()
ax01 = axis[0, 1].twinx()
ax11 = axis[1, 1].twinx()
ax21 = axis[2, 1].twinx()

# Hiding ticklabels
ax00.axes.get_yaxis().set_ticklabels([])
ax10.axes.get_yaxis().set_ticklabels([])
ax20.axes.get_yaxis().set_ticklabels([])
ax01.axes.get_yaxis().set_ticklabels([])
ax11.axes.get_yaxis().set_ticklabels([])
ax21.axes.get_yaxis().set_ticklabels([])

# hiding the spines between the different plots of the twin axis
ax00.spines['bottom'].set_visible(False)
ax10.spines['top'].set_visible(False)
ax10.spines['bottom'].set_visible(False)
ax20.spines['top'].set_visible(False)
ax01.spines['bottom'].set_visible(False)
ax11.spines['top'].set_visible(False)
ax11.spines['bottom'].set_visible(False)
ax21.spines['top'].set_visible(False)

# Setting limites of the twin axis

# DATA n°1
ax00.set_ylim(52, 64)
ax10.set_ylim(102, 114)
ax20.set_ylim(126, 138)

# DATA n°2
ax01.set_ylim(60, 72)
ax11.set_ylim(94, 106)
ax21.set_ylim(110, 122)

# Managing major ticks of the twin axis
ax00.tick_params(top = False, labeltop = False, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax10.tick_params(top = False, labeltop = False, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax20.tick_params(top = False, labeltop = False, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax01.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax11.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax21.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)

# Managing minor ticks of the twin axis
ax00.yaxis.set_minor_locator(MultipleLocator(.5))
ax00.tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
ax10.yaxis.set_minor_locator(MultipleLocator(.5))
ax10.tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
ax20.yaxis.set_minor_locator(MultipleLocator(.5))
ax20.tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")

ax01.yaxis.set_minor_locator(MultipleLocator(.5))
ax01.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'minor', length = 4, width = 1.5, direction = "in")
ax11.yaxis.set_minor_locator(MultipleLocator(.5))
ax11.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'minor', length = 4, width = 1.5, direction = "in")
ax21.yaxis.set_minor_locator(MultipleLocator(.5))
ax21.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'minor', length = 4, width = 1.5, direction = "in")

# Triangles

# DATA n°1
#axis[0, 0].plot([10, 320], [57.811, 57.811], '-', color='b', linewidth=1)
#axis[1, 0].plot([10, 320], [109.2, 104.8], '-', color='b', linewidth=1)
#axis[2, 0].plot([10, 320], [132.324, 132.324], '-', color='b', linewidth=1)
axis[0, 0].plot([25, 220, 220], [56.8, 56.8, 59], '--', color='b', linewidth=1)
axis[1, 0].plot([25, 220, 220], [109, 109, 106.4], '--', color='b', linewidth=1)
axis[2, 0].plot([25, 220, 220], [133, 133, 131.8], '--', color='b', linewidth=1)

# DATA n°2
#axis[0, 1].plot([10, 320], [62.5, 69], '-', color='b', linewidth=1)
#axis[1, 1].plot([10, 320], [102.8, 96.8], '-', color='b', linewidth=1)
#axis[2, 1].plot([10, 320], [121.5, 112.5], '-', color='b', linewidth=1)
axis[0, 1].plot([25, 220, 220], [62.6, 62.6, 67], '--', color='b', linewidth=1)
axis[1, 1].plot([25, 220, 220], [102.7, 102.7, 98.2], '--', color='b', linewidth=1)
axis[2, 1].plot([25, 220, 220], [120.3, 120.3, 116], '--', color='b', linewidth=1)

# Rectangles and texts
rect_1 = mpatches.Rectangle((170, 61.2), 50, 1, alpha=0.25, facecolor='b')
rect_2 = mpatches.Rectangle((170, 103), 50, 1, alpha=0.25, facecolor='b')
rect_3 = mpatches.Rectangle((170, 120.6), 50, 1, alpha=0.25, facecolor='b')
rect_4 = mpatches.Rectangle((170, 109.2), 50, 1, alpha=0.25, facecolor='b')
rect_5 = mpatches.Rectangle((170, 55.6), 50, 1, alpha=0.25, facecolor='b')
rect_6 = mpatches.Rectangle((170, 133.2), 50, 1, alpha=0.25, facecolor='b')
axis[0, 1].add_patch(rect_1)
axis[1, 1].add_patch(rect_2)
axis[2, 1].add_patch(rect_3)
axis[1, 0].add_patch(rect_4)
axis[0, 0].add_patch(rect_5)
axis[2, 0].add_patch(rect_6)
axis[0, 1].text(175, 61.4, '~4.8°', fontsize=14, color='b')
axis[1, 1].text(175, 103.2, '~3.3°', fontsize=14, color='b')
axis[2, 1].text(175, 120.8, '~4.3°', fontsize=14, color='b')
axis[1, 0].text(175, 109.4, '~2.5°', fontsize=14, color='b')
axis[0, 0].text(175, 55.8, '~2.2°', fontsize=14, color='b')
axis[2, 0].text(175, 133.4, '~1.2°', fontsize=14, color='b')

# Defining the Y-axis limits

# DATA n°1
axis[0, 0].set_xlim(15, 310)
axis[0, 0].set_ylim(52, 64)
axis[1, 0].set_ylim(102, 114)
axis[2, 0].set_ylim(126, 138)

# DATA n°2
axis[0, 1].set_ylim(60, 72)
axis[1, 1].set_ylim(94, 106)
axis[2, 1].set_ylim(110, 122)

# Labels and graphic texts

# DATA n°1
axis[0, 0].set_title('(b)', fontsize = 30, y = 1.22, x = -0.16)
axis[0, 0].set_xlabel('T (°C)', fontsize = 18)
axis[2, 0].set_xlabel('T (°C)', fontsize = 18)
axis[0, 0].set_ylabel(r'$\Phi$ (°)', fontsize = 18)
axis[1, 0].set_ylabel(r'$\Psi$ (°)', fontsize = 18)
axis[2, 0].set_ylabel(r'$\Omega$ (°)', fontsize = 18)

# DATA n°2
#axis[0, 1].set_title('NaTaO$_2$F$_2$', fontsize = 25, y = 1.22)
axis[0, 1].set_xlabel('T (°C)', fontsize = 18)
axis[2, 1].set_xlabel('T (°C)', fontsize = 18)
axis[0, 1].set_ylabel(r'$\Phi$ (°)', fontsize = 18)
axis[1, 1].set_ylabel(r'$\Psi$ (°)', fontsize = 18)
axis[2, 1].set_ylabel(r'$\Omega$ (°)', fontsize = 18)
axis[0, 1].yaxis.set_label_position("right")
axis[1, 1].yaxis.set_label_position("right")
axis[2, 1].yaxis.set_label_position("right")


# DATA n°1

# hiding the spines between the different plots
axis[0, 0].spines['bottom'].set_visible(False)
axis[1, 0].spines['top'].set_visible(False)
axis[1, 0].spines['bottom'].set_visible(False)
axis[2, 0].spines['top'].set_visible(False)
axis[0, 0].xaxis.set_label_coords(.5, 1.2)
axis[0, 1].xaxis.set_label_coords(.5, 1.2)

# Adjusting the major ticks
axis[0, 0].xaxis.tick_top() # moving the x axis tick to the top of
axis[0, 0].tick_params(top = True, labeltop = True, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
axis[1, 0].tick_params(which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[1, 0].get_xaxis().set_visible(False) # hiding the x axis ticks
axis[2, 0].xaxis.tick_bottom() # moving the x axis tick to the top of
axis[2, 0].tick_params(which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)

# Adjusting the number of major-ticks
axis[0, 0].locator_params(axis='y', nbins=6)
axis[0, 0].locator_params(axis='x', nbins=6)
axis[1, 0].locator_params(axis='y', nbins=6)
axis[1, 0].locator_params(axis='x', nbins=6)
axis[2, 0].locator_params(axis='y', nbins=6)
axis[2, 0].locator_params(axis='x', nbins=6)

# Adjusting the minor ticks
axis[0, 0].xaxis.set_minor_locator(MultipleLocator(10))
axis[0, 0].yaxis.set_minor_locator(MultipleLocator(.5))
axis[0, 0].tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
axis[1, 0].xaxis.set_minor_locator(MultipleLocator(10))
axis[1, 0].yaxis.set_minor_locator(MultipleLocator(.5))
axis[1, 0].tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
axis[2, 0].xaxis.set_minor_locator(MultipleLocator(10))
axis[2, 0].yaxis.set_minor_locator(MultipleLocator(.5))
axis[2, 0].tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")

# DATA n°2

# hiding the spines between the different plots
axis[0, 1].spines['bottom'].set_visible(False)
axis[1, 1].spines['top'].set_visible(False)
axis[1, 1].spines['bottom'].set_visible(False)
axis[2, 1].spines['top'].set_visible(False)

# Adjusting the major ticks
axis[0, 1].xaxis.tick_top() # moving the x axis tick to the top of
axis[0, 1].tick_params(top = True, labeltop = True, bottom = False, labelbottom = False, which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[0, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[1, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[2, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[1, 1].get_xaxis().set_visible(False) # hiding the x axis ticks
axis[2, 1].xaxis.tick_bottom() # moving the x axis tick to the top of

# Adjusting the number of major-ticks
axis[0, 1].locator_params(axis='y', nbins=6)
axis[0, 1].locator_params(axis='x', nbins=6)
axis[1, 1].locator_params(axis='y', nbins=6)
axis[1, 1].locator_params(axis='x', nbins=6)
axis[2, 1].locator_params(axis='y', nbins=6)
axis[2, 1].locator_params(axis='x', nbins=6)

# Adjusting the minor ticks
axis[0, 1].xaxis.set_minor_locator(MultipleLocator(10))
axis[0, 1].yaxis.set_minor_locator(MultipleLocator(.5))
axis[0, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'minor', length = 4, width = 1.5, direction = "in")
axis[1, 1].xaxis.set_minor_locator(MultipleLocator(10))
axis[1, 1].yaxis.set_minor_locator(MultipleLocator(.5))
axis[1, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'minor', length = 4, width = 1.5, direction = "in")
axis[2, 1].xaxis.set_minor_locator(MultipleLocator(10))
axis[2, 1].yaxis.set_minor_locator(MultipleLocator(.5))
axis[2, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'minor', length = 4, width = 1.5, direction = "in")

###############################################################################################################################
###########################################< Section n°2 : Adding breaks and rectangles >######################################
###############################################################################################################################

# DATA n°1
d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=axis[0, 0].transAxes, color='k', clip_on=False)
axis[0, 0].plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
axis[0, 0].plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=axis[1, 0].transAxes)  # switch to the bottom axes
axis[1, 0].plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
axis[1, 0].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
axis[1, 0].plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
axis[1, 0].plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=axis[2, 0].transAxes)  # switch to the bottom axes
axis[2, 0].plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
axis[2, 0].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# DATA n°2
d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=axis[0, 1].transAxes, color='k', clip_on=False)
axis[0, 1].plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
axis[0, 1].plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=axis[1, 1].transAxes)  # switch to the bottom axes
axis[1, 1].plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
axis[1, 1].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
axis[1, 1].plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
axis[1, 1].plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=axis[2, 1].transAxes)  # switch to the bottom axes
axis[2, 1].plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
axis[2, 1].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# What's cool about this is that now if we vary the distance between
# ax and ax2 via f.subplots_adjust(hspace=...) or plt.subplot_tool(),
# the diagonal lines will move accordingly, and stay right at the tips
# of the spines they are 'breaking'
f.subplots_adjust(wspace=.1, hspace=.08)

#to add the colored rectangles in the plots also the area between the figures
# DATA n°1
xmin, xmax = 220,300
_,top = f.transFigure.inverted().transform(axis[0, 0].transAxes.transform([0,1]))
_,bottom = f.transFigure.inverted().transform(axis[2, 0].transAxes.transform([0,0]))
trans = matplotlib.transforms.blended_transform_factory(axis[0, 0].transData, f.transFigure)
r_1 = matplotlib.patches.Rectangle(xy=(xmin,bottom), width=xmax-xmin, height=top-bottom, transform=trans,
                                 fc='Grey', alpha = .25, ec='C0', lw=0)
f.add_artist(r_1)

# DATA n°2
_,top = f.transFigure.inverted().transform(axis[0, 1].transAxes.transform([0,1]))
_,bottom = f.transFigure.inverted().transform(axis[2, 1].transAxes.transform([0,0]))
trans = matplotlib.transforms.blended_transform_factory(axis[0, 1].transData, f.transFigure)
r_2 = matplotlib.patches.Rectangle(xy=(xmin,bottom), width=xmax-xmin, height=top-bottom, transform=trans,
                                 fc='Grey', alpha = .25, ec='C0', lw=0)
f.add_artist(r_2)

###############################################################################################################################
###############################################< Section n°3 : Linear regressions >############################################
###############################################################################################################################

# DATA n°1

# Definnig the regression variables (x, y)
x1 = data_1[:11, 0]
y11 = data_1[:11, 1]
y13 = data_1[:11, 5]
y14 = data_1[:11, 7]

# Calculating the linear regression model
model11 = sm.OLS(y11, sm.add_constant(x1))
results11 = model11.fit()
model13 = sm.OLS(y13, sm.add_constant(x1))
results13 = model13.fit()
model14 = sm.OLS(y14, sm.add_constant(x1))
results14 = model14.fit()

# extract intercept b and slope m
b11, m11 = results11.params
b13, m13 = results13.params
b14, m14 = results14.params

# plot y = m*x + b
axis[0, 0].axline(xy1=(0, b11), slope = m11, linestyle='-', color='b', linewidth=1)
axis[1, 0].axline(xy1=(0, b13), slope = m13, linestyle='-', color='b', linewidth=1)
axis[2, 0].axline(xy1=(0, b14), slope = m14, linestyle='-', color='b', linewidth=1)

# DATA n°2

# Definnig the regression variables (x, y)
x2 = data_2[:11, 0]
y21 = data_2[:11, 1]
y23 = data_2[:11, 5]
y24 = data_2[:11, 7]

# Calculating the linear regression model
model21 = sm.OLS(y21, sm.add_constant(x2))
results21 = model21.fit()
model23 = sm.OLS(y23, sm.add_constant(x2))
results23 = model23.fit()
model24 = sm.OLS(y24, sm.add_constant(x2))
results24 = model24.fit()

# extract intercept b and slope m
b21, m21 = results21.params
b23, m23 = results23.params
b24, m24 = results24.params

# plot y = m*x + b
axis[0, 1].axline(xy1=(0, b21), slope = m21, linestyle='-', color='b', linewidth=1)
axis[1, 1].axline(xy1=(0, b23), slope = m23, linestyle='-', color='b', linewidth=1)
axis[2, 1].axline(xy1=(0, b24), slope = m24, linestyle='-', color='b', linewidth=1)

#plt.tight_layout()
f.savefig('figure_10-b.png', dpi=300, bbox_inches='tight')
plt.show()