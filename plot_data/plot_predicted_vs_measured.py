import os
import matplotlib
import numpy as np
import data_parser
import matplotlib.pyplot as plt
from mean_error import mean_error
import data_analysis.printout_tools as ptools

def get_steps(gmin, gmax, resolution=4):
    grange = (gmax - gmin)
    gstep = grange / float(resolution) #
    if gstep > 1000:
        roundnum = -3
    elif gstep > 100:
        roundnum = -2
    elif gstep > 10:
        roundnum = -1
    elif gstep > 1:
        roundnum = 0
    elif gstep > 0.1:
        roundnum = 1
    elif gstep > 0.01:
        roundnum = 2
    gstep = np.round(gstep, roundnum)
    gstart = np.round(gmin - gstep, roundnum)
    gend = np.round(gmax + gstep, roundnum)
    steplist = np.arange(gstart, gend, gstep)
    return steplist

def best_worst(Ydata, Y_predicted_best, Y_predicted_worst, 
        xlabel="Measured",
        ylabel="Predicted",
        savepath="",
        stepsize = 1,
        notelist_best=list(), 
        notelist_worst=list(), 
        *args, **kwargs):
    """Plot best (left) and worst (right) Predicted vs. Measured values.
    """
    matplotlib.rcParams.update({'font.size': 18})
    notestep = 0.07
    f, ax = plt.subplots(1, 2, figsize = (11,5))
    ax[0].scatter(Ydata, Y_predicted_best, c='black', s=10)
    [minx,maxx] = ax[0].get_xlim()
    [miny,maxy] = ax[0].get_ylim()
    gmax = max(maxx, maxy)
    gmin = min(minx, miny)
    steplist0 = np.arange(gmin, gmax, stepsize)
    ax[0].set_xticks(steplist0)
    ax[0].set_yticks(steplist0)
    ax[0].plot(steplist0, steplist0, ls="--", c=".3")
    ax[0].set_title('Best Fit')
    notey = 0.88
    for note in notelist_best:
        ax[0].text(.05, notey, note, transform=ax[0].transAxes)
        notey = notey - notestep
    ax[0].set_xlabel(xlabel)
    ax[0].set_ylabel(ylabel)

    ax[1].scatter(Ydata, Y_predicted_worst, c='black', s=10)
    [minx,maxx] = ax[1].get_xlim()
    [miny,maxy] = ax[1].get_ylim()
    gmax = max(maxx, maxy)
    gmin = min(minx, miny)
    steplist1 = np.arange(gmin, gmax, stepsize)
    ax[1].set_xticks(steplist1)
    ax[1].set_yticks(steplist1)
    ax[1].plot(steplist1, steplist1, ls="--", c=".3")
    ax[1].set_title('Worst Fit')
    notey = 0.88
    for note in notelist_worst:
        ax[1].text(.05, notey, note, transform=ax[1].transAxes)
        notey = notey - notestep
    ax[1].set_xlabel(xlabel)
    ax[1].set_ylabel(ylabel)

    f.tight_layout()
    f.savefig(os.path.join(savepath, "cv_best_worst"), dpi=200, bbox_inches='tight')
    plt.clf()
    plt.close()
    return

def single(Ydata, Y_predicted, 
        xlabel="Measured",
        ylabel="Predicted",
        stepsize=1,
        savepath="",
        notelist=list(), 
        *args, **kwargs):
    """Plot Predicted vs. Measured values.
    """
    matplotlib.rcParams.update({'font.size': 18})
    smallfont = 0.85*matplotlib.rcParams['font.size']
    notestep = 0.07
    plt.figure()
    plt.scatter(Ydata, Y_predicted, c='black', s=10)
    [minx,maxx] = plt.xlim()
    [miny,maxy] = plt.ylim()
    gmax = max(maxx, maxy)
    gmin = min(minx, miny)
    steplist = np.arange(gmin, gmax, stepsize)
    plt.xticks(steplist)
    plt.yticks(steplist)
    plt.plot(steplist, steplist, ls="--", c=".3")
    notey = 0.88
    for note in notelist:
        plt.annotate(note, xy=(0.05, notey), xycoords="axes fraction",
                    fontsize=smallfont)
        notey = notey - notestep
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(os.path.join(savepath, "cv_singleplot"), dpi=200, bbox_inches='tight')
    plt.close()
    return
